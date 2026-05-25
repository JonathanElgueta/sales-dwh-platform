from loguru import logger

# ==================================================
# IMPORT MODULES
# ==================================================

from src.orchestration.validate_metadata import main as validate_metadata

from src.orchestration.plan_incremental_load import main as plan_incremental_load

from src.orchestration.execute_incremental_load import main as execute_incremental_load

from src.semantic.create_views import main as create_views

from src.marts.build_marts import main as build_marts

from src.qa.validate_sales_enriched import main as validate_sales_enriched

from src.qa.validate_dim_date import main as validate_dim_date

# ==================================================
# LOGGER CONFIG
# ==================================================

logger.remove()

logger.add(
    sink=lambda msg: print(msg, end=""),
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}"
)

# ==================================================
# MAIN PIPELINE
# ==================================================

def main():

    logger.info("===================================")
    logger.info("STARTING SALES DWH PIPELINE")
    logger.info("===================================")

    try:

        # ==================================================
        # STEP 1
        # VALIDATE METADATA
        # ==================================================

        logger.info(" ")
        logger.info("STEP 1 → VALIDATE METADATA")

        validate_metadata()

        # ==================================================
        # STEP 2
        # PLAN INCREMENTAL
        # ==================================================

        logger.info(" ")
        logger.info("STEP 2 → PLAN INCREMENTAL LOAD")

        plan_incremental_load()

        # ==================================================
        # STEP 3
        # EXECUTE INCREMENTAL
        # ==================================================

        logger.info(" ")
        logger.info("STEP 3 → EXECUTE INCREMENTAL LOAD")

        execute_incremental_load()

        # ==================================================
        # STEP 4
        # CREATE SEMANTIC LAYER
        # ==================================================

        logger.info(" ")
        logger.info("STEP 4 → CREATE SEMANTIC LAYER")

        create_views()

        # ==================================================
        # STEP 5
        # BUILD MARTS
        # ==================================================

        logger.info(" ")
        logger.info("STEP 5 → BUILD MARTS")

        build_marts()

        # ==================================================
        # STEP 6
        # QA SALES
        # ==================================================

        logger.info(" ")
        logger.info("STEP 6 → QA SALES")

        validate_sales_enriched()

        # ==================================================
        # STEP 7
        # QA DIM DATE
        # ==================================================

        logger.info(" ")
        logger.info("STEP 7 → QA DIM DATE")

        validate_dim_date()

        # ==================================================
        # PIPELINE SUCCESS
        # ==================================================

        logger.info(" ")
        logger.info("===================================")
        logger.info("PIPELINE COMPLETED SUCCESSFULLY")
        logger.info("===================================")

    except Exception as e:

        logger.error(" ")
        logger.error("===================================")
        logger.error("PIPELINE FAILED")
        logger.error("===================================")

        logger.exception(e)

        raise


# ==================================================
# ENTRYPOINT
# ==================================================

if __name__ == "__main__":

    main()