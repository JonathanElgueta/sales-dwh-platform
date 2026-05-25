import duckdb

from src.config.settings import (
    DUCKDB_PATH
)

# --------------------------------------------------
# CONEXIÓN
# --------------------------------------------------

print("\n===================================")
print("DATA QUALITY CHECKS")
print("===================================\n")

con = duckdb.connect(
    str(DUCKDB_PATH)
)

# --------------------------------------------------
# VALIDAR TOTAL REGISTROS
# --------------------------------------------------

print("1. VALIDANDO TOTAL REGISTROS\n")

query_total = """

SELECT
    COUNT(*) AS total_registros
FROM vw_sales_enriched

"""

result_total = con.execute(
    query_total
).fetchdf()

print(result_total)

# --------------------------------------------------
# VALIDAR MATCH PRODUCTOS
# --------------------------------------------------

print("\n===================================")
print("2. VALIDANDO MATCH PRODUCTOS")
print("===================================\n")

query_match = """

SELECT

    COUNT(*) AS total_registros,

    COUNT(categoria) AS registros_con_match,

    COUNT(*) - COUNT(categoria) AS registros_sin_match,

    ROUND(
        100.0 * COUNT(categoria) / COUNT(*),
        2
    ) AS porcentaje_match

FROM vw_sales_enriched

"""

result_match = con.execute(
    query_match
).fetchdf()

print(result_match)

# --------------------------------------------------
# PRODUCTOS SIN MATCH
# --------------------------------------------------

print("\n===================================")
print("3. PRODUCTOS SIN MATCH")
print("===================================\n")

query_unmatched = """

SELECT

    Producto_ID,
    Producto,

    COUNT(*) AS cantidad_registros

FROM vw_sales_enriched

WHERE categoria IS NULL

GROUP BY
    Producto_ID,
    Producto

ORDER BY cantidad_registros DESC

"""

result_unmatched = con.execute(
    query_unmatched
).fetchdf()

print(result_unmatched)

# --------------------------------------------------
# TOP CATEGORÍAS
# --------------------------------------------------

print("\n===================================")
print("4. TOP CATEGORÍAS")
print("===================================\n")

query_categories = """

SELECT

    categoria,

    ROUND(
        SUM("Venta Neta $"),
        2
    ) AS venta_total

FROM vw_sales_enriched

GROUP BY categoria

ORDER BY venta_total DESC

LIMIT 10

"""

result_categories = con.execute(
    query_categories
).fetchdf()

print(result_categories)

# --------------------------------------------------
# CERRAR CONEXIÓN
# --------------------------------------------------

con.close()

print("\n===================================")
print("VALIDACIONES FINALIZADAS")
print("===================================\n")