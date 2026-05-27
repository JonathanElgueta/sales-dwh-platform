import pandas as pd

from pathlib import Path

from datetime import datetime

# ==================================================
# LOG PATH
# ==================================================

LOG_PATH = Path(

    "data/logs"

)

LOG_PATH.mkdir(

    parents=True,
    exist_ok=True

)

LOG_FILE = (

    LOG_PATH
    /
    "pipeline_audit_log.csv"

)

# ==================================================
# CREATE LOG FILE
# ==================================================

def initialize_audit_log():

    if not LOG_FILE.exists():

        df = pd.DataFrame(columns=[

            "timestamp",
            "user",
            "file_name",
            "rows",
            "status",
            "message"

        ])

        df.to_csv(

            LOG_FILE,
            index=False

        )

# ==================================================
# WRITE AUDIT LOG
# ==================================================

def write_pipeline_log(

    user,
    file_name,
    rows,
    status,
    message

):

    initialize_audit_log()

    log_entry = pd.DataFrame([{

        "timestamp": datetime.now().strftime(

            "%Y-%m-%d %H:%M:%S"

        ),

        "user": user,

        "file_name": file_name,

        "rows": rows,

        "status": status,

        "message": message

    }])

    log_entry.to_csv(

        LOG_FILE,

        mode="a",

        header=False,

        index=False

    )

# ==================================================
# READ AUDIT LOG
# ==================================================

def read_pipeline_logs():

    initialize_audit_log()

    return pd.read_csv(

        LOG_FILE

    )