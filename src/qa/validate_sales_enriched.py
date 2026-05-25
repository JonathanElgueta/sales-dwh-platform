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
    logger.info("VALIDANDO VW_SALES_ENRICHED")
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
    # 1. TOTAL REGISTROS
    # ==================================================

    logger.info("===================================")
    logger.info("1. TOTAL REGISTROS")
    logger.info("===================================")

    query = """

    SELECT
        COUNT(*) AS total_registros
    FROM vw_sales_enriched

    """

    result = con.execute(query).fetchdf()

    logger.info(f"\n{result}")

    total_registros = result.iloc[0][
        "total_registros"
    ]

    logger.info(
        f"Total registros semantic layer: {total_registros}"
    )

    # ==================================================
    # 2. PRODUCTOS UNKNOWN
    # ==================================================

    logger.info("===================================")
    logger.info("2. PRODUCTOS UNKNOWN")
    logger.info("===================================")

    query = """

    SELECT

        COUNT(*) AS registros_unknown,

        ROUND(

            COUNT(*) * 100.0 /

            (
                SELECT COUNT(*)
                FROM vw_sales_enriched
            ),

            4

        ) AS pct_unknown

    FROM vw_sales_enriched

    WHERE producto_nombre = 'UNKNOWN'

    """

    result = con.execute(query).fetchdf()

    logger.info(f"\n{result}")

    pct_unknown = result.iloc[0][
        "pct_unknown"
    ]

    if pct_unknown > 1:

        logger.warning(
            f"PRODUCTOS: porcentaje UNKNOWN alto ({pct_unknown}%)."
        )

    else:

        logger.info(
            f"PRODUCTOS: porcentaje UNKNOWN bajo ({pct_unknown}%)."
        )

    # ==================================================
    # 3. AGENCIAS UNKNOWN
    # ==================================================

    logger.info("===================================")
    logger.info("3. AGENCIAS UNKNOWN")
    logger.info("===================================")

    query = """

    SELECT

        COUNT(*) AS registros_unknown,

        ROUND(

            COUNT(*) * 100.0 /

            (
                SELECT COUNT(*)
                FROM vw_sales_enriched
            ),

            4

        ) AS pct_unknown

    FROM vw_sales_enriched

    WHERE agencia_nombre = 'UNKNOWN'

    """

    result = con.execute(query).fetchdf()

    logger.info(f"\n{result}")

    pct_unknown = result.iloc[0][
        "pct_unknown"
    ]

    if pct_unknown > 0:

        logger.warning(
            f"AGENCIAS: existen UNKNOWN ({pct_unknown}%)."
        )

    else:

        logger.info(
            "AGENCIAS: sin registros UNKNOWN."
        )

    # ==================================================
    # 4. DUPLICADOS
    # ==================================================

    logger.info("===================================")
    logger.info("4. DUPLICADOS")
    logger.info("===================================")

    query = """

    SELECT

        COUNT(*) AS filas_originales,

        COUNT(

            DISTINCT (

                CAST(Fecha AS VARCHAR) ||
                Canal ||
                Subcanal ||
                Cadena ||
                CAST(Agencia_ID AS VARCHAR) ||
                Producto_ID

            )

        ) AS filas_unicas

    FROM vw_sales_enriched

    """

    result = con.execute(query).fetchdf()

    logger.info(f"\n{result}")

    duplicados = (

        result["filas_originales"][0]
        -
        result["filas_unicas"][0]

    )

    logger.info(
        f"Posibles duplicados detectados: {duplicados}"
    )

    if duplicados > 0:

        logger.warning(
            "Existen posibles duplicados."
        )

    else:

        logger.info(
            "No se detectaron duplicados."
        )

    # ==================================================
    # 5. NULOS
    # ==================================================

    logger.info("===================================")
    logger.info("5. NULOS")
    logger.info("===================================")

    query = """

    SELECT

        SUM(
            CASE
                WHEN Fecha IS NULL
                THEN 1
                ELSE 0
            END
        ) AS fecha_null,

        SUM(
            CASE
                WHEN Producto_ID IS NULL
                THEN 1
                ELSE 0
            END
        ) AS producto_id_null,

        SUM(
            CASE
                WHEN Agencia_ID IS NULL
                THEN 1
                ELSE 0
            END
        ) AS agencia_id_null,

        SUM(
            CASE
                WHEN "Venta Neta $" IS NULL
                THEN 1
                ELSE 0
            END
        ) AS venta_null

    FROM vw_sales_enriched

    """

    result = con.execute(query).fetchdf()

    logger.info(f"\n{result}")

    total_nulls = result.sum(axis=1)[0]

    if total_nulls > 0:

        logger.warning(
            f"Se detectaron NULLs críticos: {total_nulls}"
        )

    else:

        logger.info(
            "No se detectaron NULLs críticos."
        )

    # ==================================================
    # 6. GRANULARIDAD
    # ==================================================

    logger.info("===================================")
    logger.info("6. GRANULARIDAD")
    logger.info("===================================")

    query = """

    SELECT

        COUNT(DISTINCT Producto_ID) AS productos,
        COUNT(DISTINCT Agencia_ID) AS agencias,
        COUNT(DISTINCT Fecha) AS fechas,
        COUNT(DISTINCT categoria) AS categorias,
        COUNT(DISTINCT marca) AS marcas

    FROM vw_sales_enriched

    """

    result = con.execute(query).fetchdf()

    logger.info(f"\n{result}")

    logger.info(
        "Granularidad validada correctamente."
    )

    # ==================================================
    # 7. TOP UNKNOWN PRODUCTS
    # ==================================================

    logger.info("===================================")
    logger.info("7. TOP UNKNOWN PRODUCTS")
    logger.info("===================================")

    query = """

    SELECT

        Producto_ID,
        Producto,

        COUNT(*) AS registros

    FROM vw_sales_enriched

    WHERE producto_nombre = 'UNKNOWN'

    GROUP BY
        1,
        2

    ORDER BY registros DESC

    LIMIT 20

    """

    result = con.execute(query).fetchdf()

    logger.info(f"\n{result}")

    if len(result) > 0:

        logger.warning(
            "Existen productos no homologados en dimensión."
        )

    # ==================================================
    # 8. VALIDACIÓN FINANCIERA
    # ==================================================

    logger.info("===================================")
    logger.info("8. VALIDACIÓN FINANCIERA")
    logger.info("===================================")

    query = """

    SELECT

        ROUND(
            SUM("Venta Neta $"),
            2
        ) AS venta_total,

        ROUND(
            SUM("Devolución $"),
            2
        ) AS devolucion_total,

        ROUND(

            SUM("Devolución $") * 100.0
            /

            NULLIF(
                SUM("Venta Neta $"),
                0
            ),

            2

        ) AS pct_devolucion

    FROM vw_sales_enriched

    """

    result = con.execute(query).fetchdf()

    logger.info(f"\n{result}")

    pct_devolucion = result.iloc[0][
        "pct_devolucion"
    ]

    logger.info(
        f"Pct devolución global: {pct_devolucion}%"
    )

    logger.info(
        "Validación financiera OK."
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
    logger.info("VALIDACIÓN FINALIZADA")
    logger.info("===================================")


# ==================================================
# ENTRYPOINT
# ==================================================

if __name__ == "__main__":

    main()