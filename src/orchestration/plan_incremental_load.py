import pandas as pd

from loguru import logger

from src.config.settings import (
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
    logger.info("PLANNING INCREMENTAL LOAD")
    logger.info("===================================")

    # ==================================================
    # LOAD METADATA
    # ==================================================

    logger.info(
        f"Loading metadata: {PROCESSED_FILES_PATH}"
    )

    metadata_df = pd.read_parquet(
        PROCESSED_FILES_PATH
    )

    logger.info(
        f"Metadata rows loaded: {len(metadata_df)}"
    )

    # ==================================================
    # SORT PERIODS
    # ==================================================

    metadata_df = metadata_df.sort_values(
        by="period"
    )

    logger.info(
        "Metadata sorted by period."
    )

    # ==================================================
    # IDENTIFY LATEST PERIOD
    # ==================================================

    latest_period = metadata_df[
        "period"
    ].max()

    logger.info(
        f"Latest detected period: {latest_period}"
    )

    # ==================================================
    # BUILD EXECUTION PLAN
    # ==================================================

    execution_plan = []

    logger.info(
        "Building execution plan..."
    )

    for _, row in metadata_df.iterrows():

        period = row["period"]
        status = row["status"]

        # ----------------------------------------------
        # ACTION LOGIC
        # ----------------------------------------------

        if period == latest_period:

            action = "REPROCESS"

        elif status == "CLOSED":

            action = "SKIP"

        else:

            action = "REVIEW"

        # ----------------------------------------------
        # PLAN ROW
        # ----------------------------------------------

        execution_plan.append({

            "period": period,
            "status": status,
            "action": action

        })

    # ==================================================
    # PLAN DATAFRAME
    # ==================================================

    plan_df = pd.DataFrame(
        execution_plan
    )

    # ==================================================
    # SHOW PLAN
    # ==================================================

    logger.info("===================================")
    logger.info("EXECUTION PLAN")
    logger.info("===================================")

    logger.info(f"\n{plan_df}")

    # ==================================================
    # SUMMARY
    # ==================================================

    logger.info("===================================")
    logger.info("SUMMARY")
    logger.info("===================================")

    summary = (
        plan_df["action"]
        .value_counts()
    )

    logger.info(f"\n{summary}")

    # ==================================================
    # VALIDATION
    # ==================================================

    if "REPROCESS" not in summary.index:

        logger.warning(
            "No se detectó período REPROCESS."
        )

    else:

        logger.info(
            "Execution plan validado correctamente."
        )

    # ==================================================
    # END
    # ==================================================

    logger.info("===================================")
    logger.info("INCREMENTAL PLAN READY")
    logger.info("===================================")


# ==================================================
# ENTRYPOINT
# ==================================================

if __name__ == "__main__":

    main()