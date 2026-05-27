import pandas as pd

# ==================================================
# QA VALIDATIONS
# ==================================================

def run_qa_validations(df):

    validations = []

    errors = 0

    # ==================================================
    # REQUIRED RAW COLUMNS
    # ==================================================

    required_columns = [

        "fecha",
        "producto",
        "cadena"

    ]

    missing_columns = [

        col

        for col in required_columns

        if col not in df.columns

    ]

    if len(missing_columns) == 0:

        validations.append({

            "validacion": "Required Columns",
            "estado": "PASS",
            "detalle": "Columnas requeridas presentes"

        })

    else:

        errors += 1

        validations.append({

            "validacion": "Required Columns",
            "estado": "FAIL",
            "detalle": f"Faltan columnas: {missing_columns}"

        })

    # ==================================================
    # NULL CHECK
    # ==================================================

    nulls = int(

        df.isnull().sum().sum()

    )

    if nulls == 0:

        validations.append({

            "validacion": "Null Check",
            "estado": "PASS",
            "detalle": "Sin valores nulos"

        })

    else:

        errors += 1

        validations.append({

            "validacion": "Null Check",
            "estado": "FAIL",
            "detalle": f"{nulls} valores nulos"

        })

    # ==================================================
    # DUPLICATES
    # ==================================================

    duplicates = int(

        df.duplicated().sum()

    )

    if duplicates == 0:

        validations.append({

            "validacion": "Duplicates",
            "estado": "PASS",
            "detalle": "Sin duplicados"

        })

    else:

        errors += 1

        validations.append({

            "validacion": "Duplicates",
            "estado": "FAIL",
            "detalle": f"{duplicates} duplicados"

        })

    # ==================================================
    # DATE VALIDATION
    # ==================================================

    if "fecha" in df.columns:

        try:

            pd.to_datetime(df["fecha"])

            validations.append({

                "validacion": "Date Format",
                "estado": "PASS",
                "detalle": "Formato fecha válido"

            })

        except:

            errors += 1

            validations.append({

                "validacion": "Date Format",
                "estado": "FAIL",
                "detalle": "Fechas inválidas"

            })

    # ==================================================
    # SALES VALIDATION
    # ==================================================

    if "venta_total" in df.columns:

        negative_sales = int(

            (df["venta_total"] < 0).sum()

        )

        validations.append({

            "validacion": "Negative Sales",
            "estado": "PASS",
            "detalle": f"{negative_sales} registros negativos detectados"

        })

    # ==================================================
    # QA SCORE
    # ==================================================

    total_validations = len(validations)

    passed = len([

        x

        for x in validations

        if x["estado"] == "PASS"

    ])

    qa_score = round(

        (passed / total_validations) * 100,

        2

    )

    # ==================================================
    # RESULT
    # ==================================================

    return {

        "success": errors == 0,
        "errors": errors,
        "qa_score": qa_score,
        "validations": validations

    }