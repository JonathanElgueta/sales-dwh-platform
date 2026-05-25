from pathlib import Path
import shutil
import duckdb

from src.config.settings import (

    # LEGACY
    PRODUCTS_PATH,
    AGENCIES_PATH,
    DATE_PATH,
    SALES_PATH,

    # WAREHOUSE
    WAREHOUSE_PATH

)

# ==================================================
# START
# ==================================================

print("\n===================================")
print("MIGRATING TO WAREHOUSE")
print("===================================\n")

# ==================================================
# CREATE WAREHOUSE STRUCTURE
# ==================================================

dimensions_path = (
    WAREHOUSE_PATH / "dimensions"
)

facts_path = (
    WAREHOUSE_PATH / "facts"
)

sales_fact_path = (
    facts_path / "sales"
)

products_dim_path = (
    dimensions_path / "products"
)

agencies_dim_path = (
    dimensions_path / "agencies"
)

date_dim_path = (
    dimensions_path / "date"
)

# CREATE DIRS

products_dim_path.mkdir(
    parents=True,
    exist_ok=True
)

agencies_dim_path.mkdir(
    parents=True,
    exist_ok=True
)

date_dim_path.mkdir(
    parents=True,
    exist_ok=True
)

sales_fact_path.mkdir(
    parents=True,
    exist_ok=True
)

print("Warehouse structure creada.\n")

# ==================================================
# COPY DIMENSIONS
# ==================================================

print("===================================")
print("COPYING DIMENSIONS")
print("===================================\n")

# PRODUCTS

shutil.copy2(

    PRODUCTS_PATH,

    products_dim_path / "dim_producto.parquet"

)

print("dim_producto copiada")

# AGENCIES

shutil.copy2(

    AGENCIES_PATH,

    agencies_dim_path / "dim_agencia.parquet"

)

print("dim_agencia copiada")

# DATE

shutil.copy2(

    DATE_PATH,

    date_dim_path / "dim_date.parquet"

)

print("dim_date copiada")

# ==================================================
# CONNECT DUCKDB
# ==================================================

print("\n===================================")
print("CONNECTING DUCKDB")
print("===================================\n")

con = duckdb.connect()

# ==================================================
# LOAD SALES
# ==================================================

print("Leyendo sales parquet...\n")

query = f"""

SELECT *
FROM read_parquet(
    '{SALES_PATH}/**/*.parquet'
)

"""

sales_df = con.execute(
    query
).fetchdf()

print(f"Rows cargadas: {len(sales_df)}")

# ==================================================
# PARTITION SALES
# ==================================================

print("\n===================================")
print("CREATING FACT PARTITIONS")
print("===================================\n")

grouped = sales_df.groupby(
    ["year", "month"]
)

for (year, month), partition_df in grouped:

    # ----------------------------------------------
    # PARTITION PATH
    # ----------------------------------------------

    partition_path = (

        sales_fact_path
        / f"year={year}"
        / f"month={month:02d}"

    )

    partition_path.mkdir(
        parents=True,
        exist_ok=True
    )

    # ----------------------------------------------
    # OUTPUT FILE
    # ----------------------------------------------

    output_file = (
        partition_path
        / "data.parquet"
    )

    # ----------------------------------------------
    # EXPORT
    # ----------------------------------------------

    partition_df.to_parquet(
        output_file,
        index=False
    )

    print(
        f"Partition creada: "
        f"{year}-{month:02d}"
    )

# ==================================================
# CLOSE
# ==================================================

con.close()

# ==================================================
# END
# ==================================================

print("\n===================================")
print("WAREHOUSE MIGRATION COMPLETED")
print("===================================\n")

print(f"Warehouse path:\n{WAREHOUSE_PATH}")