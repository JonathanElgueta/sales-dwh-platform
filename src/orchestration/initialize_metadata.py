from pathlib import Path
from datetime import datetime
import pandas as pd

from src.config.settings import (
    RAW_SALES_PATH,
    PROCESSED_FILES_PATH
)

# ==================================================
# START
# ==================================================

print("\n===================================")
print("INITIALIZING METADATA")
print("===================================\n")

# ==================================================
# SCAN SALES FILES
# ==================================================

sales_files = sorted(
    RAW_SALES_PATH.glob("*.xlsx")
)

print(f"Archivos detectados: {len(sales_files)}\n")

# ==================================================
# BUILD METADATA
# ==================================================

metadata_rows = []

# último archivo = ACTIVE

latest_file = sales_files[-1].name

for file_path in sales_files:

    file_name = file_path.name

    # ----------------------------------------------
    # EXTRAER PERÍODO
    # ----------------------------------------------

    period = (
        file_name
        .split("(")[1]
        .split(")")[0]
    )

    # ----------------------------------------------
    # STATUS
    # ----------------------------------------------

    status = (
        "ACTIVE"
        if file_name == latest_file
        else "CLOSED"
    )

    # ----------------------------------------------
    # FILE SIZE
    # ----------------------------------------------

    file_size_mb = round(
        file_path.stat().st_size / (1024 * 1024),
        2
    )

    # ----------------------------------------------
    # ROW
    # ----------------------------------------------

    metadata_rows.append({

        "file_name": file_name,

        "source": "sales",

        "period": period,

        "status": status,

        "rows_processed": None,

        "processed_at": datetime.now(),

        "warehouse_partition": period,

        "file_size_mb": file_size_mb

    })

# ==================================================
# DATAFRAME
# ==================================================

metadata_df = pd.DataFrame(
    metadata_rows
)

# ==================================================
# VALIDATE
# ==================================================

print("===================================")
print("METADATA PREVIEW")
print("===================================\n")

print(metadata_df)

# ==================================================
# EXPORT
# ==================================================

metadata_df.to_parquet(
    PROCESSED_FILES_PATH,
    index=False
)

# ==================================================
# END
# ==================================================

print("\n===================================")
print("METADATA CREATED")
print("===================================\n")

print(f"Ruta:\n{PROCESSED_FILES_PATH}")