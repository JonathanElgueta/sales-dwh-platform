import duckdb

from src.config.settings import (

    DUCKDB_PATH,
    MARTS_PATH,

    MART_SALES_MONTHLY_PATH,
    MART_BRAND_PERFORMANCE_PATH,
    MART_SALES_WEEKLY_BIMBO_PATH,
    MART_CATEGORY_PERFORMANCE_PATH,
    MART_CHANNEL_PERFORMANCE_PATH

)

# --------------------------------------------------
# CREATE MARTS DIRECTORY
# --------------------------------------------------

MARTS_PATH.mkdir(
    parents=True,
    exist_ok=True
)

# --------------------------------------------------
# CONEXIÓN
# --------------------------------------------------

print("\n===================================")
print("BUILDING ANALYTICAL MARTS")
print("===================================\n")

con = duckdb.connect(
    str(DUCKDB_PATH)
)

# --------------------------------------------------
# MART 1
# SALES MONTHLY
# --------------------------------------------------

print("===================================")
print("BUILDING MART: SALES MONTHLY")
print("===================================\n")

query_sales_monthly = """

SELECT

    year,
    month,

    ROUND(
        SUM("Venta Neta $"),
        0
    ) AS venta_total,

    ROUND(
        SUM("Venta Neta Tn"),
        2
    ) AS venta_toneladas,

    ROUND(
        SUM("Venta Neta UE"),
        0
    ) AS venta_unidades_equivalentes,

    ROUND(
        SUM("Venta Neta Pz"),
        0
    ) AS venta_piezas,

    ROUND(
        SUM("Devolución $"),
        0
    ) AS devolucion_total,

    ROUND(
        SUM("Devolución Tn"),
        2
    ) AS devolucion_toneladas,

    ROUND(
        SUM("Devolución UE"),
        0
    ) AS devolucion_unidades_equivalentes,

    ROUND(
        SUM("Devolución Pz"),
        0
    ) AS devolucion_piezas,

    ROUND(

        (
            SUM("Devolución $")
            /

            NULLIF(
                SUM("Venta Neta $"),
                0
            )
        ) * 100,

        2

    ) AS pct_devolucion

FROM vw_sales_enriched

GROUP BY
    year,
    month

ORDER BY
    year,
    month

"""

sales_monthly_df = con.execute(
    query_sales_monthly
).fetchdf()

sales_monthly_df.to_parquet(
    MART_SALES_MONTHLY_PATH,
    index=False
)

print("SALES MONTHLY OK")

# --------------------------------------------------
# MART 2
# BRAND PERFORMANCE
# --------------------------------------------------

print("===================================")
print("BUILDING MART: BRAND PERFORMANCE")
print("===================================\n")

query_brand_performance = """

SELECT

    year,
    month,

    marca,

    ROUND(
        SUM("Venta Neta $"),
        0
    ) AS venta_total,

    ROUND(
        SUM("Venta Neta Tn"),
        2
    ) AS venta_toneladas,

    ROUND(
        SUM("Venta Neta UE"),
        0
    ) AS venta_unidades_equivalentes,

    ROUND(
        SUM("Venta Neta Pz"),
        0
    ) AS venta_piezas,

    ROUND(
        SUM("Devolución $"),
        0
    ) AS devolucion_total,

    ROUND(

        (
            SUM("Devolución $")
            /

            NULLIF(
                SUM("Venta Neta $"),
                0
            )
        ) * 100,

        2

    ) AS pct_devolucion,

    ROUND(

        (
            SUM("Venta Neta $")
            /

            SUM(SUM("Venta Neta $")) OVER(

                PARTITION BY
                    year,
                    month

            )

        ) * 100,

        2

    ) AS market_share_pct,

    RANK() OVER(

        PARTITION BY
            year,
            month

        ORDER BY
            SUM("Venta Neta $") DESC

    ) AS ranking_venta

FROM vw_sales_enriched

GROUP BY

    year,
    month,
    marca

ORDER BY

    year,
    month,
    venta_total DESC

"""

brand_performance_df = con.execute(
    query_brand_performance
).fetchdf()

brand_performance_df.to_parquet(
    MART_BRAND_PERFORMANCE_PATH,
    index=False
)

print("BRAND PERFORMANCE OK")

# --------------------------------------------------
# MART 3
# SALES WEEKLY BIMBO
# --------------------------------------------------

print("===================================")
print("BUILDING MART: SALES WEEKLY BIMBO")
print("===================================\n")

query_sales_weekly_bimbo = """

SELECT

    year_semana_bimbo,
    semana_bimbo,

    ROUND(
        SUM("Venta Neta $"),
        0
    ) AS venta_total,

    ROUND(
        SUM("Venta Neta Tn"),
        2
    ) AS venta_toneladas,

    ROUND(
        SUM("Venta Neta UE"),
        0
    ) AS venta_unidades_equivalentes,

    ROUND(
        SUM("Venta Neta Pz"),
        0
    ) AS venta_piezas,

    ROUND(
        SUM("Devolución $"),
        0
    ) AS devolucion_total,

    ROUND(
        SUM("Devolución Tn"),
        2
    ) AS devolucion_toneladas,

    ROUND(
        SUM("Devolución UE"),
        0
    ) AS devolucion_unidades_equivalentes,

    ROUND(
        SUM("Devolución Pz"),
        0
    ) AS devolucion_piezas,

    ROUND(

        (
            SUM("Devolución $")
            /

            NULLIF(
                SUM("Venta Neta $"),
                0
            )
        ) * 100,

        2

    ) AS pct_devolucion

FROM vw_sales_enriched

GROUP BY
    year_semana_bimbo,
    semana_bimbo

ORDER BY
    year_semana_bimbo,
    semana_bimbo

"""

sales_weekly_bimbo_df = con.execute(
    query_sales_weekly_bimbo
).fetchdf()

sales_weekly_bimbo_df.to_parquet(
    MART_SALES_WEEKLY_BIMBO_PATH,
    index=False
)

print("SALES WEEKLY BIMBO OK")

# --------------------------------------------------
# MART 4
# CATEGORY PERFORMANCE
# --------------------------------------------------

print("===================================")
print("BUILDING MART: CATEGORY PERFORMANCE")
print("===================================\n")

query_category_performance = """

SELECT

    year,
    month,

    categoria,

    ROUND(
        SUM("Venta Neta $"),
        0
    ) AS venta_total,

    ROUND(
        SUM("Venta Neta Tn"),
        2
    ) AS venta_toneladas,

    ROUND(
        SUM("Venta Neta UE"),
        0
    ) AS venta_unidades_equivalentes,

    ROUND(
        SUM("Venta Neta Pz"),
        0
    ) AS venta_piezas,

    ROUND(
        SUM("Devolución $"),
        0
    ) AS devolucion_total,

    ROUND(

        (
            SUM("Devolución $")
            /

            NULLIF(
                SUM("Venta Neta $"),
                0
            )
        ) * 100,

        2

    ) AS pct_devolucion,

    ROUND(

        (
            SUM("Venta Neta $")
            /

            SUM(SUM("Venta Neta $")) OVER(

                PARTITION BY
                    year,
                    month

            )

        ) * 100,

        2

    ) AS market_share_pct,

    RANK() OVER(

        PARTITION BY
            year,
            month

        ORDER BY
            SUM("Venta Neta $") DESC

    ) AS ranking_categoria

FROM vw_sales_enriched

GROUP BY

    year,
    month,
    categoria

ORDER BY

    year,
    month,
    venta_total DESC

"""

category_performance_df = con.execute(
    query_category_performance
).fetchdf()

category_performance_df.to_parquet(
    MART_CATEGORY_PERFORMANCE_PATH,
    index=False
)

print("CATEGORY PERFORMANCE OK")

# --------------------------------------------------
# MART 5
# CHANNEL PERFORMANCE
# --------------------------------------------------

print("===================================")
print("BUILDING MART: CHANNEL PERFORMANCE")
print("===================================\n")

query_channel_performance = """

SELECT

    year,
    month,

    Canal AS canal,
    Subcanal AS subcanal,
    Cadena AS cadena,

    ROUND(
        SUM("Venta Neta $"),
        0
    ) AS venta_total,

    ROUND(
        SUM("Venta Neta Tn"),
        2
    ) AS venta_toneladas,

    ROUND(
        SUM("Venta Neta UE"),
        0
    ) AS venta_unidades_equivalentes,

    ROUND(
        SUM("Venta Neta Pz"),
        0
    ) AS venta_piezas,

    ROUND(
        SUM("Devolución $"),
        0
    ) AS devolucion_total,

    ROUND(

        (
            SUM("Devolución $")
            /

            NULLIF(
                SUM("Venta Neta $"),
                0
            )
        ) * 100,

        2

    ) AS pct_devolucion,

    ROUND(

        (
            SUM("Venta Neta $")
            /

            SUM(SUM("Venta Neta $")) OVER(

                PARTITION BY
                    year,
                    month

            )

        ) * 100,

        2

    ) AS market_share_pct,

    RANK() OVER(

        PARTITION BY
            year,
            month

        ORDER BY
            SUM("Venta Neta $") DESC

    ) AS ranking_canal

FROM vw_sales_enriched

GROUP BY

    year,
    month,
    Canal,
    Subcanal,
    Cadena

ORDER BY

    year,
    month,
    venta_total DESC

"""

channel_performance_df = con.execute(
    query_channel_performance
).fetchdf()

channel_performance_df.to_parquet(
    MART_CHANNEL_PERFORMANCE_PATH,
    index=False
)

print("CHANNEL PERFORMANCE OK")

# --------------------------------------------------
# CLOSE
# --------------------------------------------------

con.close()

print("\n===================================")
print("MART BUILD FINALIZADO")
print("===================================\n")