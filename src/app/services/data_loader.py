import pandas as pd

from src.config.settings import (
    MARTS_PATH
)

# ==================================================
# SALES MONTHLY
# ==================================================

def load_sales_monthly():

    path = MARTS_PATH / "mart_sales_monthly.parquet"

    return pd.read_parquet(path)

# ==================================================
# BRAND PERFORMANCE
# ==================================================

def load_brand_performance():

    path = MARTS_PATH / "mart_brand_performance.parquet"

    return pd.read_parquet(path)

# ==================================================
# CATEGORY PERFORMANCE
# ==================================================

def load_category_performance():

    path = MARTS_PATH / "mart_category_performance.parquet"

    return pd.read_parquet(path)

# ==================================================
# CHANNEL PERFORMANCE
# ==================================================

def load_channel_performance():

    path = MARTS_PATH / "mart_channel_performance.parquet"

    return pd.read_parquet(path)

# ==================================================
# SALES ENRICHED
# ==================================================

def load_sales_enriched():

    import duckdb

    from src.config.settings import DUCKDB_PATH

    con = duckdb.connect(
        str(DUCKDB_PATH)
    )

    query = """

    SELECT *

    FROM vw_sales_enriched

    """

    df = con.execute(query).fetchdf()

    con.close()

    return df