import pandas as pd

from pathlib import Path

from src.app.services.pipeline.schema_mapper import (

    normalize_columns

)

from src.app.services.pipeline.warehouse_loader import (

    update_sales_warehouse

)

# ==================================================
# PATHS
# ==================================================

RAW_PATH = Path(

    "data/raw/sales"

)

# ==================================================
# REBUILD WAREHOUSE
# ==================================================

def rebuild_sales_warehouse():

    try:

        # ==================================================
        # XLSX FILES
        # ==================================================

        xlsx_files = list(

            RAW_PATH.glob("*.xlsx")

        )

        if len(xlsx_files) == 0:

            return {

                "success": False,

                "message": "No existen archivos XLSX históricos."

            }

        # ==================================================
        # CONSOLIDATED DF
        # ==================================================

        df_list = []

        # ==================================================
        # PROCESS FILES
        # ==================================================

        for file in xlsx_files:

            print(

                f"Procesando: {file.name}"

            )

            # ==================================================
            # READ XLSX
            # ==================================================

            df = pd.read_excel(

                file

            )

            # ==================================================
            # NORMALIZE COLUMNS
            # ==================================================

            df = normalize_columns(

                df

            )

            # ==================================================
            # FORCE STRING IDS
            # ==================================================

            string_columns = [

                "producto_id",
                "agencia_id"

            ]

            for col in string_columns:

                if col in df.columns:

                    df[col] = df[col].astype(str)

            # ==================================================
            # APPEND
            # ==================================================

            df_list.append(

                df

            )

        # ==================================================
        # CONCAT DATA
        # ==================================================

        final_df = pd.concat(

            df_list,

            ignore_index=True

        )

        # ==================================================
        # UPDATE WAREHOUSE
        # ==================================================

        warehouse_result = update_sales_warehouse(

            final_df

        )

        if not warehouse_result["success"]:

            return warehouse_result

        # ==================================================
        # RESULT
        # ==================================================

        return {

            "success": True,

            "rows": len(final_df),

            "files": len(xlsx_files),

            "partitions": warehouse_result["partitions"]

        }

    except Exception as e:

        return {

            "success": False,

            "message": str(e)

        }

# ==================================================
# EXECUTE
# ==================================================

if __name__ == "__main__":

    result = rebuild_sales_warehouse()

    print(

        "\n=================================="

    )

    print(

        "REBUILD RESULT"

    )

    print(

        "=================================="

    )

    print(result)