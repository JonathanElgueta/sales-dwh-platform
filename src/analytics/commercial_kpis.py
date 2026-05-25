import duckdb

from src.config.settings import (
    DUCKDB_PATH,
    EXPORTS_PATH
)

# --------------------------------------------------
# CONEXIÓN
# --------------------------------------------------

print("\n===================================")
print("COMMERCIAL KPIs")
print("===================================\n")

con = duckdb.connect(
    str(DUCKDB_PATH)
)

# --------------------------------------------------
# KPI 1
# VENTAS MENSUALES
# --------------------------------------------------

print("===================================")
print("KPI 1 - VENTAS MENSUALES")
print("===================================\n")

query_monthly_sales = """

SELECT

    year,
    month,

    ROUND(
        SUM("Venta Neta $"),
        0
    ) AS venta_total

FROM vw_sales_enriched

GROUP BY
    year,
    month

ORDER BY
    year,
    month

"""

monthly_sales_df = con.execute(
    query_monthly_sales
).fetchdf()

print(monthly_sales_df)

# --------------------------------------------------
# KPI 2
# CRECIMIENTO YOY
# --------------------------------------------------

print("\n===================================")
print("KPI 2 - CRECIMIENTO YoY")
print("===================================\n")

query_yoy = """

WITH monthly_sales AS (

    SELECT

        year,
        month,

        SUM("Venta Neta $") AS venta_total

    FROM vw_sales_enriched

    GROUP BY
        year,
        month
)

SELECT

    year,
    month,

    ROUND(
        venta_total,
        0
    ) AS venta_actual,

    ROUND(

        LAG(venta_total, 12)
        OVER (
            ORDER BY year, month
        ),

        0

    ) AS venta_año_anterior,

    ROUND(

        (
            (
                venta_total
                /

                LAG(venta_total, 12)
                OVER (
                    ORDER BY year, month
                )
            ) - 1
        ) * 100,

        2

    ) AS crecimiento_yoy_pct

FROM monthly_sales

ORDER BY
    year,
    month

"""

yoy_df = con.execute(
    query_yoy
).fetchdf()

print(yoy_df)

# --------------------------------------------------
# KPI 3
# TOP CATEGORÍAS
# --------------------------------------------------

print("\n===================================")
print("KPI 3 - TOP CATEGORÍAS")
print("===================================\n")

query_top_categories = """

SELECT

    categoria,

    ROUND(
        SUM("Venta Neta $"),
        0
    ) AS venta_total

FROM vw_sales_enriched

GROUP BY categoria

ORDER BY venta_total DESC

LIMIT 10

"""

top_categories_df = con.execute(
    query_top_categories
).fetchdf()

print(top_categories_df)

# --------------------------------------------------
# KPI 4
# TOP MARCAS
# --------------------------------------------------

print("\n===================================")
print("KPI 4 - TOP MARCAS")
print("===================================\n")

query_top_brands = """

SELECT

    marca,

    ROUND(
        SUM("Venta Neta $"),
        0
    ) AS venta_total

FROM vw_sales_enriched

GROUP BY marca

ORDER BY venta_total DESC

LIMIT 10

"""

top_brands_df = con.execute(
    query_top_brands
).fetchdf()

print(top_brands_df)

# --------------------------------------------------
# KPI 5
# TOP AGENCIAS
# --------------------------------------------------

print("\n===================================")
print("KPI 5 - TOP AGENCIAS")
print("===================================\n")

query_top_agencies = """

SELECT

    agencia_nombre,

    ROUND(
        SUM("Venta Neta $"),
        0
    ) AS venta_total

FROM vw_sales_enriched

GROUP BY agencia_nombre

ORDER BY venta_total DESC

LIMIT 10

"""

top_agencies_df = con.execute(
    query_top_agencies
).fetchdf()

print(top_agencies_df)

# --------------------------------------------------
# EXPORTAR RESULTADOS
# --------------------------------------------------

OUTPUT_PATH = EXPORTS_PATH

monthly_sales_df.to_csv(
    OUTPUT_PATH / "monthly_sales.csv",
    index=False
)

yoy_df.to_csv(
    OUTPUT_PATH / "yoy_growth.csv",
    index=False
)

top_categories_df.to_csv(
    OUTPUT_PATH / "top_categories.csv",
    index=False
)

top_brands_df.to_csv(
    OUTPUT_PATH / "top_brands.csv",
    index=False
)

top_agencies_df.to_csv(
    OUTPUT_PATH / "top_agencies.csv",
    index=False
)

# --------------------------------------------------
# CERRAR CONEXIÓN
# --------------------------------------------------

con.close()

print("\n===================================")
print("KPIs FINALIZADOS")
print("===================================\n")

print(f"Archivos exportados en:\n{OUTPUT_PATH}")