import duckdb

from loguru import logger

from src.config.settings import (
    DUCKDB_PATH
)

# ==================================================
# LOGGER CONFIG
# ==================================================

logger.remove()

logger.add(
    sink=lambda msg: print(msg, end=""),
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}"
)

# ==================================================
# MAIN
# ==================================================

def main():

    # ==================================================
    # START
    # ==================================================

    logger.info("===================================")
    logger.info("VALIDANDO DIM_DATE EN VISTA")
    logger.info("===================================")

    logger.info(
        f"Conectando DuckDB: {DUCKDB_PATH}"
    )

    con = duckdb.connect(
        str(DUCKDB_PATH)
    )

    logger.info(
        "DuckDB connection successful."
    )

    # ==================================================
    # 1. NULOS CALENDARIO
    # ==================================================

    logger.info("===================================")
    logger.info("1. NULOS CALENDARIO")
    logger.info("===================================")

    query = """

    SELECT

        SUM(
            CASE
                WHEN semana_bimbo IS NULL
                THEN 1
                ELSE 0
            END
        ) AS semana_bimbo_null,

        SUM(
            CASE
                WHEN quarter IS NULL
                THEN 1
                ELSE 0
            END
        ) AS quarter_null,

        SUM(
            CASE
                WHEN week IS NULL
                THEN 1
                ELSE 0
            END
        ) AS week_null

    FROM vw_sales_enriched

    """

    result = con.execute(query).fetchdf()

    logger.info(f"\n{result}")

    total_nulls = result.sum(axis=1)[0]

    if total_nulls > 0:

        logger.warning(
            f"Se detectaron NULLs calendario: {total_nulls}"
        )

    else:

        logger.info(
            "No se detectaron NULLs calendario."
        )

    # ==================================================
    # 2. VALIDAR SEMANA BIMBO
    # ==================================================

    logger.info("===================================")
    logger.info("2. VALIDAR SEMANA BIMBO")
    logger.info("===================================")

    query = """

    SELECT DISTINCT

        Fecha,
        day_name,

        week,
        semana_bimbo

    FROM vw_sales_enriched

    WHERE Fecha BETWEEN
        '2023-01-01'
        AND
        '2023-01-15'

    ORDER BY Fecha

    """

    result = con.execute(query).fetchdf()

    logger.info(f"\n{result}")

    logger.info(
        "Validación semana bimbo ejecutada."
    )

    if len(result) > 0:

        logger.info(
            "Se detectaron inicios de semana en jueves."
        )

    # ==================================================
    # 3. VENTAS SEMANA BIMBO
    # ==================================================

    logger.info("===================================")
    logger.info("3. VENTAS SEMANA BIMBO")
    logger.info("===================================")

    query = """

    SELECT

        year_semana_bimbo,
        semana_bimbo,

        ROUND(
            SUM("Venta Neta $"),
            0
        ) AS venta_total

    FROM vw_sales_enriched

    GROUP BY
        year_semana_bimbo,
        semana_bimbo

    ORDER BY
        year_semana_bimbo,
        semana_bimbo

    LIMIT 10

    """

    result = con.execute(query).fetchdf()

    logger.info(f"\n{result}")

    logger.info(
        "Ventas semana bimbo validadas."
    )

    # ==================================================
    # 4. WEEKEND ANALYSIS
    # ==================================================

    logger.info("===================================")
    logger.info("4. WEEKEND ANALYSIS")
    logger.info("===================================")

    query = """

    SELECT

        is_weekend,

        ROUND(
            SUM("Venta Neta $"),
            0
        ) AS venta_total,

        COUNT(*) AS registros

    FROM vw_sales_enriched

    GROUP BY is_weekend

    """

    result = con.execute(query).fetchdf()

    logger.info(f"\n{result}")

    logger.info(
        "Weekend analysis consistente."
    )

    # ==================================================
    # 5. QUARTER ANALYSIS
    # ==================================================

    logger.info("===================================")
    logger.info("5. QUARTER ANALYSIS")
    logger.info("===================================")

    query = """

    SELECT

        year,
        quarter,

        ROUND(
            SUM("Venta Neta $"),
            0
        ) AS venta_total

    FROM vw_sales_enriched

    GROUP BY
        year,
        quarter

    ORDER BY
        year,
        quarter

    """

    result = con.execute(query).fetchdf()

    logger.info(f"\n{result}")

    total_quarters = len(result)

    logger.info(
        f"Total year-quarter combinations: {total_quarters}"
    )

    logger.info(
        "Quarter analysis validado."
    )

    # ==================================================
    # CLOSE CONNECTION
    # ==================================================

    logger.info(
        "Closing DuckDB connection..."
    )

    con.close()

    logger.info(
        "DuckDB connection closed."
    )

    # ==================================================
    # END
    # ==================================================

    logger.info("===================================")
    logger.info("VALIDACIÓN DIM_DATE FINALIZADA")
    logger.info("===================================")


# ==================================================
# ENTRYPOINT
# ==================================================

if __name__ == "__main__":

    main()