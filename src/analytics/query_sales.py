import duckdb

from src.config.settings import (
    SALES_PARQUET_PATH
)

# --------------------------------------------------
# CONEXIÓN DUCKDB
# --------------------------------------------------

print("\n===================================")
print("CONECTANDO A DUCKDB")
print("===================================\n")

con = duckdb.connect()

# --------------------------------------------------
# QUERY SQL
# --------------------------------------------------

query = f"""

SELECT

    year,
    month,

    COUNT(*) AS total_registros,

    ROUND(
        SUM("Venta Neta $"),
        2
    ) AS venta_total

FROM read_parquet(
    '{SALES_PARQUET_PATH}/**/*.parquet'
)

GROUP BY
    year,
    month

ORDER BY
    year,
    month

"""

# --------------------------------------------------
# EJECUTAR QUERY
# --------------------------------------------------

print("Ejecutando consulta SQL...\n")

result = con.execute(
    query
).fetchdf()

# --------------------------------------------------
# MOSTRAR RESULTADOS
# --------------------------------------------------

print("===================================")
print("RESULTADO QUERY")
print("===================================\n")

print(result)

# --------------------------------------------------
# CERRAR CONEXIÓN
# --------------------------------------------------

con.close()

print("\nConexión cerrada.")