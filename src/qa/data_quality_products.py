import duckdb

from src.config.settings import (
    DUCKDB_PATH
)

# --------------------------------------------------
# CONEXIÓN
# --------------------------------------------------

print("===================================")
print("PRODUCT DATA QUALITY")
print("===================================\n")

con = duckdb.connect(
    str(DUCKDB_PATH)
)

# --------------------------------------------------
# 1. PRODUCTOS SIN MATCH
# --------------------------------------------------

print("===================================")
print("1. PRODUCTOS SIN MATCH")
print("===================================\n")

query_no_match = """

SELECT

    Producto_ID,
    Producto,

    COUNT(*) AS registros

FROM vw_sales_enriched

WHERE producto_nombre = 'UNKNOWN'

GROUP BY
    Producto_ID,
    Producto

ORDER BY registros DESC

"""

df_no_match = con.execute(
    query_no_match
).fetchdf()

print(df_no_match)

# --------------------------------------------------
# 2. PRODUCTOS SIN MARCA
# --------------------------------------------------

print("\n===================================")
print("2. PRODUCTOS SIN MARCA")
print("===================================\n")

query_no_brand = """

SELECT

    Producto_ID,
    Producto,
    producto_nombre,
    marca,

    COUNT(*) AS registros

FROM vw_sales_enriched

WHERE marca = 'UNKNOWN'

GROUP BY
    Producto_ID,
    Producto,
    producto_nombre,
    marca

ORDER BY registros DESC

"""

df_no_brand = con.execute(
    query_no_brand
).fetchdf()

print(df_no_brand)

# --------------------------------------------------
# 3. PRODUCTOS SIN CATEGORÍA
# --------------------------------------------------

print("\n===================================")
print("3. PRODUCTOS SIN CATEGORÍA")
print("===================================\n")

query_no_category = """

SELECT

    Producto_ID,
    Producto,
    producto_nombre,
    categoria,

    COUNT(*) AS registros

FROM vw_sales_enriched

WHERE categoria = 'UNKNOWN'

GROUP BY
    Producto_ID,
    Producto,
    producto_nombre,
    categoria

ORDER BY registros DESC

"""

df_no_category = con.execute(
    query_no_category
).fetchdf()

print(df_no_category)

# --------------------------------------------------
# 4. PRODUCTOS SIN LÍNEA
# --------------------------------------------------

print("\n===================================")
print("4. PRODUCTOS SIN LÍNEA")
print("===================================\n")

query_no_line = """

SELECT

    Producto_ID,
    Producto,
    producto_nombre,
    linea,

    COUNT(*) AS registros

FROM vw_sales_enriched

WHERE linea = 'UNKNOWN'

GROUP BY
    Producto_ID,
    Producto,
    producto_nombre,
    linea

ORDER BY registros DESC

"""

df_no_line = con.execute(
    query_no_line
).fetchdf()

print(df_no_line)

# --------------------------------------------------
# CERRAR CONEXIÓN
# --------------------------------------------------

con.close()

print("\n===================================")
print("DATA QUALITY FINALIZADO")
print("===================================")