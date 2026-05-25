from pathlib import Path
from loguru import logger
import sys

# --------------------------------------------------
# LOG PATH
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parents[2]

LOGS_PATH = (
    BASE_DIR
    / "data"
    / "logs"
)

LOGS_PATH.mkdir(
    parents=True,
    exist_ok=True
)

LOG_FILE = (
    LOGS_PATH
    / "sales_dwh.log"
)

# --------------------------------------------------
# REMOVE DEFAULT LOGGER
# --------------------------------------------------

logger.remove()

# --------------------------------------------------
# CONSOLE LOGGER
# --------------------------------------------------

logger.add(
    sys.stdout,
    level="INFO",
    format=(
        "{time:YYYY-MM-DD HH:mm:ss} | "
        "{level} | "
        "{message}"
    )
)

# --------------------------------------------------
# FILE LOGGER
# --------------------------------------------------

logger.add(
    LOG_FILE,
    level="INFO",
    rotation="10 MB",
    retention="30 days",
    compression="zip",
    format=(
        "{time:YYYY-MM-DD HH:mm:ss} | "
        "{level} | "
        "{message}"
    )
)

# --------------------------------------------------
# EXPORT LOGGER
# --------------------------------------------------

__all__ = ["logger"]