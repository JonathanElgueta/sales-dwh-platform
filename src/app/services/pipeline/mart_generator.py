import pandas as pd

import duckdb

from pathlib import Path

# ==================================================
# PATHS
# ==================================================

DUCKDB_PATH = Path(

    "data/duckdb/sales_dwh.duckdb"

)

MART_PATH = Path(

    "data/marts"

)

MART_PATH.mkdir(

    parents=True,
    exist_ok=True

)

# ==================================================
# LOAD ENRICHED SALES
# ==================================================

def load_consolidated_sales():

    con = duckdb.connect(

        str(DUCKDB_PATH)

    )

    query = """

    SELECT *

    FROM vw_sales_enriched

    """

    df = con.execute(

        query

    ).fetchdf()

    con.close()

    return df

# ==================================================
# MART SALES MONTHLY
# ==================================================

def generate_sales_monthly_mart(df):

    mart = (

        df
        .groupby(

            ["year", "month"],

            as_index=False

        )
        .agg({

            "venta_total": "sum"

        })

        .sort_values(

            ["year", "month"]

        )

    )

    path = MART_PATH / "mart_sales_monthly.parquet"

    mart.to_parquet(

        path,
        index=False

    )

# ==================================================
# MART BRAND PERFORMANCE
# ==================================================

def generate_brand_performance_mart(df):

    mart = (

        df
        .groupby(

            ["year", "month", "marca"],

            as_index=False

        )
        .agg({

            "venta_total": "sum"

        })

    )

    total_sales = mart["venta_total"].sum()

    mart["market_share_pct"] = (

        mart["venta_total"]

        /

        total_sales

    ) * 100

    mart["ranking_venta"] = (

        mart["venta_total"]
        .rank(

            ascending=False,
            method="dense"

        )

    )

    path = MART_PATH / "mart_brand_performance.parquet"

    mart.to_parquet(

        path,
        index=False

    )

# ==================================================
# MART DAILY SALES
# ==================================================

def generate_daily_sales_mart(df):

    mart = (

        df
        .groupby(

            ["fecha"],

            as_index=False

        )
        .agg({

            "venta_total": "sum"

        })

        .sort_values(

            "fecha"

        )

    )

    path = MART_PATH / "mart_daily_sales.parquet"

    mart.to_parquet(

        path,
        index=False

    )

# ==================================================
# GENERATE ALL MARTS
# ==================================================

def generate_all_marts():

    try:

        df = load_consolidated_sales()

        generate_sales_monthly_mart(df)

        generate_brand_performance_mart(df)

        generate_daily_sales_mart(df)

        return {

            "success": True,

            "rows": len(df)

        }

    except Exception as e:

        return {

            "success": False,

            "message": str(e)

        }