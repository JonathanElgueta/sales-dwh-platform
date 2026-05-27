import pandas as pd

from pathlib import Path

from src.app.services.pipeline.schema_mapper import (

    normalize_columns

)

# ==================================================
# PATHS
# ==================================================

RAW_PATH = Path(

    "data/raw/incremental"

)

PARQUET_PATH = Path(

    "data/parquet/sales"

)

RAW_PATH.mkdir(

    parents=True,
    exist_ok=True

)

PARQUET_PATH.mkdir(

    parents=True,
    exist_ok=True

)

# ==================================================
# REQUIRED COLUMNS
# ==================================================

REQUIRED_COLUMNS = [

    "fecha",
    "cadena",
    "producto",
    "venta_total"

]

# ==================================================
# VALIDATE FILE
# ==================================================

def validate_sales_file(df):

    missing_columns = [

        col

        for col in REQUIRED_COLUMNS

        if col not in df.columns

    ]

    if missing_columns:

        return False, missing_columns

    return True, []

# ==================================================
# PROCESS XLSX
# ==================================================

def process_incremental_file(

    uploaded_file

):

    try:

        # ==================================================
        # READ XLSX
        # ==================================================

        df = pd.read_excel(

            uploaded_file

        )

        # ==================================================
        # NORMALIZE COLUMNS
        # ==================================================

        df = normalize_columns(df)

        # ==================================================
        # VALIDATE
        # ==================================================

        is_valid, missing = validate_sales_file(df)

        if not is_valid:

            return {

                "success": False,

                "message": (

                    f"Faltan columnas requeridas: "

                    f"{missing}"

                )

            }

        # ==================================================
        # DATE
        # ==================================================

        df["fecha"] = pd.to_datetime(

            df["fecha"]

        )

        df["year"] = (

            df["fecha"].dt.year

        )

        df["month"] = (

            df["fecha"].dt.month

        )

        # ==================================================
        # OPTIONAL FIELDS
        # ==================================================

        optional_columns = [

            "marca",
            "categoria",
            "pct_devolucion"

        ]

        for col in optional_columns:

            if col not in df.columns:

                df[col] = 0

        # ==================================================
        # SAVE RAW
        # ==================================================

        raw_file = (

            RAW_PATH
            /
            uploaded_file.name

        )

        with open(raw_file, "wb") as f:

            f.write(

                uploaded_file.getbuffer()

            )

        # ==================================================
        # SAVE PARQUET
        # ==================================================

        parquet_file = (

            PARQUET_PATH
            /
            f"{uploaded_file.name}.parquet"

        )

        df.to_parquet(

            parquet_file,
            index=False

        )

        # ==================================================
        # RESULT
        # ==================================================

        return {

            "success": True,

            "rows": len(df),

            "file": str(parquet_file),

            "data": df

        }

    except Exception as e:

        return {

            "success": False,

            "message": str(e)

        }