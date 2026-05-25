from pathlib import Path

# ==================================================
# BASE PROJECT
# ==================================================

BASE_DIR = Path(
    __file__
).resolve().parents[2]

# ==================================================
# DATA LAYER
# ==================================================

DATA_PATH = (
    BASE_DIR
    / "data"
)

# ==================================================
# RAW LAYER
# ==================================================

RAW_PATH = (
    DATA_PATH
    / "raw"
)

RAW_SALES_PATH = (
    RAW_PATH
    / "sales"
)

# ==================================================
# LEGACY PARQUET LAYER
# ==================================================

PARQUET_PATH = (
    DATA_PATH
    / "parquet"
)

SALES_PATH = (
    PARQUET_PATH
    / "sales"
)

PRODUCTS_PATH = (
    PARQUET_PATH
    / "products"
    / "dim_producto.parquet"
)

AGENCIES_PATH = (
    PARQUET_PATH
    / "agencies"
    / "dim_agencia.parquet"
)

DATE_PATH = (
    PARQUET_PATH
    / "date"
    / "dim_date.parquet"
)

# ==================================================
# WAREHOUSE LAYER
# ==================================================

WAREHOUSE_PATH = (
    DATA_PATH
    / "warehouse"
)

# ==================================================
# WAREHOUSE FACTS
# ==================================================

WAREHOUSE_FACTS_PATH = (
    WAREHOUSE_PATH
    / "facts"
)

WAREHOUSE_SALES_PATH = (
    WAREHOUSE_FACTS_PATH
    / "sales"
)

# ==================================================
# WAREHOUSE DIMENSIONS
# ==================================================

WAREHOUSE_DIMENSIONS_PATH = (
    WAREHOUSE_PATH
    / "dimensions"
)

WAREHOUSE_PRODUCTS_PATH = (
    WAREHOUSE_DIMENSIONS_PATH
    / "products"
    / "dim_producto.parquet"
)

WAREHOUSE_AGENCIES_PATH = (
    WAREHOUSE_DIMENSIONS_PATH
    / "agencies"
    / "dim_agencia.parquet"
)

WAREHOUSE_DATE_PATH = (
    WAREHOUSE_DIMENSIONS_PATH
    / "date"
    / "dim_date.parquet"
)

# ==================================================
# DUCKDB
# ==================================================

DUCKDB_PATH = (
    DATA_PATH
    / "duckdb"
    / "sales_dwh.duckdb"
)

# ==================================================
# MARTS
# ==================================================

MARTS_PATH = (
    DATA_PATH
    / "marts"
)

MART_SALES_MONTHLY_PATH = (
    MARTS_PATH
    / "mart_sales_monthly.parquet"
)

MART_BRAND_PERFORMANCE_PATH = (
    MARTS_PATH
    / "mart_brand_performance.parquet"
)

MART_SALES_WEEKLY_BIMBO_PATH = (
    MARTS_PATH
    / "mart_sales_weekly_bimbo.parquet"
)

MART_CATEGORY_PERFORMANCE_PATH = (
    MARTS_PATH
    / "mart_category_performance.parquet"
)

MART_CHANNEL_PERFORMANCE_PATH = (
    MARTS_PATH
    / "mart_channel_performance.parquet"
)

# ==================================================
# EXPORTS
# ==================================================

EXPORTS_PATH = (
    BASE_DIR
    / "outputs"
)

# ==================================================
# METADATA
# ==================================================

METADATA_PATH = (
    DATA_PATH
    / "metadata"
)

PROCESSED_FILES_PATH = (
    METADATA_PATH
    / "processed_files.parquet"
)

# ==================================================
# LOGGING
# ==================================================

LOGS_PATH = (
    DATA_PATH
    / "logs"
)