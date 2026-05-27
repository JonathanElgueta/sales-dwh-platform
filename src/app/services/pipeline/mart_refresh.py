import pandas as pd

from pathlib import Path

# ==================================================
# PATHS
# ==================================================

PARQUET_PATH = Path(

    "data/parquet/sales"

)

MART_PATH = Path(

    "data/marts"

)

MART_PATH.mkdir(

    parents=True,
    exist_ok=True

)

# ==================================================
# REFRESH SALES MART
# ==================================================

def refresh_sales_mart():

    parquet_files = list(

        PARQUET_PATH.glob("*.parquet")

    )

    if len(parquet_files) == 0:

        return {

            "success": False,
            "message": "No existen archivos parquet."

        }

    # ==================================================
    # CONCAT DATA
    # ==================================================

    df_list = []

    for file in parquet_files:

        df = pd.read_parquet(file)

        df_list.append(df)

    final_df = pd.concat(

        df_list,
        ignore_index=True

    )

    # ==================================================
    # SAVE MART
    # ==================================================

    mart_file = (

        MART_PATH
        /
        "sales_monthly.parquet"

    )

    final_df.to_parquet(

        mart_file,
        index=False

    )

    # ==================================================
    # RESULT
    # ==================================================

    return {

        "success": True,
        "rows": len(final_df),
        "mart": str(mart_file)

    }