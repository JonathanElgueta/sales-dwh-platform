from pathlib import Path
import pandas as pd

# --------------------------------------------------
# RUTA ARCHIVOS SALES
# --------------------------------------------------

SALES_PATH = Path(r"C:\sales-dwh\data\raw\sales")

# --------------------------------------------------
# BUSCAR ARCHIVOS XLSX
# --------------------------------------------------

files = list(SALES_PATH.glob("*.xlsx"))

print("\n===================================")
print("VALIDACIÓN ESTRUCTURAL")
print("===================================\n")

print(f"Cantidad archivos: {len(files)}\n")

# --------------------------------------------------
# ESTRUCTURA BASE
# --------------------------------------------------

base_columns = None

# --------------------------------------------------
# RECORRER ARCHIVOS
# --------------------------------------------------

for index, file in enumerate(files):

    print("--------------------------------------------------")
    print(f"Archivo: {file.name}")
    print("--------------------------------------------------")

    try:

        # ------------------------------------------
        # LEER SOLO ENCABEZADOS
        # ------------------------------------------

        df = pd.read_excel(
            file,
            sheet_name="Hoja1",
            nrows=0
        )

        current_columns = list(df.columns)

        # ------------------------------------------
        # PRIMER ARCHIVO = BASE COMPARACIÓN
        # ------------------------------------------

        if index == 0:

            base_columns = current_columns

            print("Archivo base establecido")
            print(f"Cantidad columnas: {len(base_columns)}")

        else:

            # --------------------------------------
            # VALIDAR DIFERENCIAS
            # --------------------------------------

            if current_columns == base_columns:

                print("ESTRUCTURA OK")

            else:

                print("DIFERENCIAS DETECTADAS")

                missing = set(base_columns) - set(current_columns)
                extra = set(current_columns) - set(base_columns)

                if missing:

                    print("\nColumnas faltantes:")
                    for col in missing:
                        print(f"- {col}")

                if extra:

                    print("\nColumnas extra:")
                    for col in extra:
                        print(f"- {col}")

    except Exception as e:

        print(f"ERROR: {e}")

    print("\n")