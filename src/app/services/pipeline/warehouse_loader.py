import pandas as pd

from pathlib import Path

# ==================================================
# PATHS
# ==================================================

WAREHOUSE_PATH = Path(
    "data/warehouse/facts/sales"
)

WAREHOUSE_PATH.mkdir(
    parents=True,
    exist_ok=True
)

# ==================================================
# UPDATE SALES WAREHOUSE
# ==================================================

def update_sales_warehouse(df):

    try:

        # ==================================================
        # VALIDATE FECHA
        # ==================================================

        if "fecha" not in df.columns:

            return {

                "success": False,

                "message": "La columna fecha no existe."

            }

        # ==================================================
        # DATE FORMAT
        # ==================================================

        df["fecha"] = pd.to_datetime(
            df["fecha"]
        )

        # ==================================================
        # YEAR / MONTH
        # ==================================================

        df["year"] = (
            df["fecha"].dt.year
        )

        df["month"] = (
            df["fecha"].dt.month
        )

        # ==================================================
        # GET PARTITIONS
        # ==================================================

        partitions = (

            df[["year", "month"]]
            .drop_duplicates()

        )

        total_rows = 0

        # ==================================================
        # PROCESS PARTITIONS
        # ==================================================

        for _, row in partitions.iterrows():

            year = int(row["year"])

            month = int(row["month"])

            # ==================================================
            # FILTER PARTITION
            # ==================================================

            partition_df = df[

                (df["year"] == year)
                &
                (df["month"] == month)

            ]

            # ==================================================
            # PARTITION PATH
            # ==================================================

            partition_path = (

                WAREHOUSE_PATH
                /
                f"year={year}"
                /
                f"month={month:02d}"

            )

            partition_path.mkdir(

                parents=True,
                exist_ok=True

            )

            # ==================================================
            # PARQUET FILE
            # ==================================================

            parquet_file = (

                partition_path
                /
                "data.parquet"

            )

            # ==================================================
            # OVERWRITE PARTITION
            # ==================================================

            partition_df.to_parquet(

                parquet_file,

                index=False

            )

            total_rows += len(partition_df)

        # ==================================================
        # RESULT
        # ==================================================

        return {

            "success": True,

            "rows": total_rows,

            "partitions": len(partitions)

        }

    except Exception as e:

        return {

            "success": False,

            "message": str(e)

        }