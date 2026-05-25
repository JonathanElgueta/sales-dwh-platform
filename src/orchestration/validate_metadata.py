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
    logger.info("VALIDATING METADATA")
    logger.info("===================================")

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
    # 1. TOTAL FILES
    # ==================================================

    logger.info("===================================")
    logger.info("1. TOTAL FILES")
    logger.info("===================================")

    logger.info(
        f"Total archivos metadata: {len(metadata_df)}"
    )

    # ==================================================
    # 2. ACTIVE FILE VALIDATION
    # ==================================================

    logger.info("===================================")
    logger.info("2. ACTIVE FILE VALIDATION")
    logger.info("===================================")

    active_files = metadata_df[
        metadata_df["status"] == "ACTIVE"
    ]

    logger.info(f"\n{active_files}")

    logger.info(
        f"Cantidad ACTIVE detectados: {len(active_files)}"
    )

    if len(active_files) != 1:

        logger.error(
            "Debe existir SOLO 1 ACTIVE."
        )

        raise ValueError(
            "ERROR: Debe existir SOLO 1 archivo ACTIVE"
        )

    logger.info(
        "OK: solo existe 1 ACTIVE"
    )

    # ==================================================
    # 3. UNIQUE PERIODS
    # ==================================================

    logger.info("===================================")
    logger.info("3. UNIQUE PERIODS")
    logger.info("===================================")

    duplicated_periods = metadata_df[
        metadata_df["period"].duplicated()
    ]

    if len(duplicated_periods) > 0:

        logger.error(
            "Se detectaron períodos duplicados."
        )

        logger.info(
            f"\n{duplicated_periods}"
        )

        raise ValueError(
            "ERROR: períodos duplicados detectados"
        )

    logger.info(
        "OK: períodos únicos"
    )

    # ==================================================
    # 4. ACTIVE IS LATEST
    # ==================================================

    logger.info("===================================")
    logger.info("4. ACTIVE IS LATEST")
    logger.info("===================================")

    latest_period = max(
        metadata_df["period"]
    )

    active_period = active_files.iloc[0][
        "period"
    ]

    logger.info(
        f"Último período detectado: {latest_period}"
    )

    logger.info(
        f"ACTIVE período actual: {active_period}"
    )

    if latest_period != active_period:

        logger.error(
            "ACTIVE no corresponde al último período."
        )

        raise ValueError(
            "ERROR: ACTIVE no corresponde al último período"
        )

    logger.info(
        "OK: ACTIVE correcto"
    )

    # ==================================================
    # 5. VALIDATE PERIOD CONTINUITY
    # ==================================================

    logger.info("===================================")
    logger.info("5. VALIDATE PERIOD CONTINUITY")
    logger.info("===================================")

    periods = sorted(
        metadata_df["period"].tolist()
    )

    missing_periods = []

    for i in range(len(periods) - 1):

        current = periods[i]
        next_period = periods[i + 1]

        current_year = int(
            current.split("_")[0]
        )

        current_month = int(
            current.split("_")[1]
        )

        expected_month = current_month + 1
        expected_year = current_year

        if expected_month > 12:

            expected_month = 1
            expected_year += 1

        expected_period = (
            f"{expected_year}_{expected_month:02d}"
        )

        if next_period != expected_period:

            missing_periods.append(
                expected_period
            )

    if len(missing_periods) > 0:

        logger.error(
            "Se detectaron gaps temporales."
        )

        logger.info(
            f"\nPeríodos faltantes:\n{missing_periods}"
        )

        raise ValueError(
            "ERROR: gaps detectados"
        )

    logger.info(
        "OK: continuidad correcta"
    )

    # ==================================================
    # SUMMARY
    # ==================================================

    logger.info("===================================")
    logger.info("METADATA SUMMARY")
    logger.info("===================================")

    logger.info(
        f"Total períodos procesados: {len(periods)}"
    )

    logger.info(
        f"Primer período: {periods[0]}"
    )

    logger.info(
        f"Último período: {periods[-1]}"
    )

    logger.info(
        f"ACTIVE actual: {active_period}"
    )

    # ==================================================
    # END
    # ==================================================

    logger.info("===================================")
    logger.info("METADATA VALIDATION SUCCESS")
    logger.info("===================================")


# ==================================================
# ENTRYPOINT
# ==================================================

if __name__ == "__main__":

    main()