import duckdb

from loguru import logger

from src.config.settings import (

    DUCKDB_PATH,

    WAREHOUSE_SALES_PATH,

    WAREHOUSE_PRODUCTS_PATH,

    WAREHOUSE_AGENCIES_PATH,

    WAREHOUSE_DATE_PATH

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
    logger.info("CONECTANDO A DUCKDB")
    logger.info("===================================")

    logger.info(
        f"DuckDB path: {DUCKDB_PATH}"
    )

    con = duckdb.connect(
        str(DUCKDB_PATH)
    )

    logger.info(
        "DuckDB connection successful."
    )

    # ==================================================
    # CREATE VIEW
    # ==================================================

    logger.info("===================================")
    logger.info("CREATING VIEW vw_sales_enriched")
    logger.info("===================================")

    query = f"""

    CREATE OR REPLACE VIEW vw_sales_enriched AS

    SELECT

        -- ==================================================
        -- FACT
        -- ==================================================

        s.*,

        -- ==================================================
        -- PRODUCT DIMENSION
        -- ==================================================

        p.producto_nombre,
        p.categoria,
        p.marca,

        -- ==================================================
        -- AGENCY DIMENSION
        -- ==================================================

        a.agencia_nombre,

        -- ==================================================
        -- DATE DIMENSION
        -- ==================================================

        d.date_key,
        d.year,
        d.quarter,
        d.month,
        d.month_name,
        d.week,
        d.iso_year,
        d.semana_bimbo,
        d.year_semana_bimbo,
        d.day,
        d.day_of_week,
        d.day_name,
        d.is_weekend

    FROM read_parquet(
        '{WAREHOUSE_SALES_PATH}/year=*/month=*/*.parquet'
    ) s

    LEFT JOIN read_parquet(
        '{WAREHOUSE_PRODUCTS_PATH}'
    ) p

        ON s.Producto_ID = p.producto_id

    LEFT JOIN read_parquet(
        '{WAREHOUSE_AGENCIES_PATH}'
    ) a

        ON s.Agencia_ID = a.agencia_id

    LEFT JOIN read_parquet(
        '{WAREHOUSE_DATE_PATH}'
    ) d

        ON s.Fecha = d.date

    """

    logger.info(
        "Executing CREATE VIEW statement..."
    )

    con.execute(query)

    logger.info(
        "View creada correctamente."
    )

    # ==================================================
    # VALIDATION
    # ==================================================

    logger.info("===================================")
    logger.info("VALIDATING VIEW")
    logger.info("===================================")

    validation_query = """

    SELECT
        COUNT(*) AS total_registros
    FROM vw_sales_enriched

    """

    result = con.execute(
        validation_query
    ).fetchdf()

    total_rows = result.iloc[0][
        "total_registros"
    ]

    logger.info(
        f"Total registros semantic layer: {total_rows}"
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
    logger.info("SEMANTIC LAYER CREATED")
    logger.info("===================================")

    logger.info(
        f"Base DuckDB: {DUCKDB_PATH}"
    )


# ==================================================
# ENTRYPOINT
# ==================================================

if __name__ == "__main__":

    main()