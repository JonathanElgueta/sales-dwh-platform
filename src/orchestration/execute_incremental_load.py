from pathlib import Path
from datetime import datetime

import pandas as pd
import shutil

from loguru import logger

from src.config.settings import (

    RAW_SALES_PATH,

    WAREHOUSE_SALES_PATH,

    PROCESSED_FILES_PATH

)

# ==================================================
# LOGGER CONFIG
# ==================================================

logger.remove()

logger.add(
    sink=lambda msg: print(msg, end=""),
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}"
)

# ==================================================
# MAIN
# ==================================================

def main():

    # ==================================================
    # START
    # ==================================================

    logger.info("===================================")
    logger.info("EXECUTING INCREMENTAL LOAD")
    logger.info("===================================")

    # ==================================================
    # LOAD METADATA
    # ==================================================

    logger.info("Loading metadata parquet...")

    metadata_df = pd.read_parquet(
        PROCESSED_FILES_PATH
    )

    logger.info(
        f"Metadata rows loaded: {len(metadata_df)}"
    )

    # ==================================================
    # FIND ACTIVE FILE
    # ==================================================

    logger.info("Searching ACTIVE period...")

    active_df = metadata_df[
        metadata_df["status"] == "ACTIVE"
    ]

    if len(active_df) != 1:

        logger.error(
            "Debe existir SOLO 1 ACTIVE."
        )

        raise ValueError(
            "ERROR: debe existir SOLO 1 ACTIVE"
        )

    active_row = active_df.iloc[0]

    file_name = active_row["file_name"]
    period = active_row["period"]

    logger.info(f"ACTIVE period: {period}")
    logger.info(f"Archivo ACTIVE: {file_name}")

    # ==================================================
    # RAW FILE PATH
    # ==================================================

    raw_file_path = (
        RAW_SALES_PATH
        / file_name
    )

    if not raw_file_path.exists():

        logger.error(
            f"No existe archivo: {raw_file_path}"
        )

        raise FileNotFoundError(
            f"No existe archivo: {raw_file_path}"
        )

    logger.info(
        f"Raw file encontrado: {raw_file_path}"
    )

    # ==================================================
    # EXTRACT YEAR / MONTH
    # ==================================================

    year = period.split("_")[0]
    month = period.split("_")[1]

    logger.info(f"Year detectado: {year}")
    logger.info(f"Month detectado: {month}")

    # ==================================================
    # DELETE OLD PARTITION
    # ==================================================

    partition_path = (

        WAREHOUSE_SALES_PATH
        / f"year={year}"
        / f"month={month}"

    )

    logger.info("===================================")
    logger.info("REMOVING OLD PARTITION")
    logger.info("===================================")

    if partition_path.exists():

        shutil.rmtree(
            partition_path
        )

        logger.info(
            f"Partición eliminada: {partition_path}"
        )

    else:

        logger.warning(
            "No existe partición previa."
        )

    # ==================================================
    # LOAD XLSX
    # ==================================================

    logger.info("===================================")
    logger.info("READING XLSX")
    logger.info("===================================")

    sales_df = pd.read_excel(
        raw_file_path
    )

    logger.info(
        f"Rows leídas: {len(sales_df)}"
    )

    # ==================================================
    # ADD PARTITIONS
    # ==================================================

    sales_df["year"] = int(year)
    sales_df["month"] = int(month)

    logger.info(
        "Columnas partición agregadas."
    )

    # ==================================================
    # CREATE PARTITION
    # ==================================================

    partition_path.mkdir(
        parents=True,
        exist_ok=True
    )

    output_file = (
        partition_path
        / "data.parquet"
    )

    # ==================================================
    # EXPORT PARQUET
    # ==================================================

    logger.info("===================================")
    logger.info("WRITING PARTITION")
    logger.info("===================================")

    sales_df.to_parquet(
        output_file,
        index=False
    )

    logger.info(
        f"Partition creada: {output_file}"
    )

    # ==================================================
    # UPDATE METADATA
    # ==================================================

    logger.info("===================================")
    logger.info("UPDATING METADATA")
    logger.info("===================================")

    metadata_df.loc[

        metadata_df["period"] == period,

        "processed_at"

    ] = datetime.now()

    metadata_df.loc[

        metadata_df["period"] == period,

        "rows_processed"

    ] = len(sales_df)

    metadata_df.to_parquet(
        PROCESSED_FILES_PATH,
        index=False
    )

    logger.info(
        "Metadata actualizada."
    )

    # ==================================================
    # END
    # ==================================================

    logger.info("===================================")
    logger.info("INCREMENTAL LOAD COMPLETED")
    logger.info("===================================")


# ==================================================
# ENTRYPOINT
# ==================================================

if __name__ == "__main__":

    main()