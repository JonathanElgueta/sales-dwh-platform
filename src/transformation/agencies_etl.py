from pathlib import Path
import pandas as pd

# --------------------------------------------------
# RUTAS
# --------------------------------------------------

SALES_PATH = Path(
    r"C:\sales-dwh\data\parquet\sales"
)

PARQUET_PATH = Path(
    r"C:\sales-dwh\data\parquet\agencies"
)

# --------------------------------------------------
# CREAR CARPETA OUTPUT
# --------------------------------------------------

PARQUET_PATH.mkdir(
    parents=True,
    exist_ok=True
)

# --------------------------------------------------
# INICIO
# --------------------------------------------------

print("\n===================================")
print("INICIANDO ETL DIM_AGENCIA")
print("===================================\n")

# --------------------------------------------------
# LEER PARQUET SALES
# --------------------------------------------------

print("Leyendo fact sales...\n")

sales_df = pd.read_parquet(
    SALES_PATH
)

# --------------------------------------------------
# EXTRAER DIMENSIÓN
# --------------------------------------------------

print("Extrayendo columnas dimensión...\n")

agency_df = sales_df[
    [
        "Agencia_ID",
        "Agencia"
    ]
].copy()

# --------------------------------------------------
# RENOMBRAR COLUMNAS
# --------------------------------------------------

print("Renombrando columnas...\n")

agency_df = agency_df.rename(
    columns={
        "Agencia_ID": "agencia_id",
        "Agencia": "agencia_nombre"
    }
)

# --------------------------------------------------
# NORMALIZAR TIPOS
# --------------------------------------------------

print("Normalizando tipos...\n")

agency_df["agencia_id"] = (
    agency_df["agencia_id"]
    .astype(str)
)

# --------------------------------------------------
# ELIMINAR DUPLICADOS
# --------------------------------------------------

print("Eliminando duplicados...\n")

before_rows = len(agency_df)

agency_df = agency_df.drop_duplicates()

after_rows = len(agency_df)

# --------------------------------------------------
# VALIDACIONES
# --------------------------------------------------

print("===================================")
print("VALIDACIONES")
print("===================================\n")

print(f"Filas antes: {before_rows}")
print(f"Filas después: {after_rows}")

print("\nDimensiones finales:")
print(agency_df.shape)

print("\nNulos:")
print(agency_df.isnull().sum())

print("\nDuplicados agencia_id:")
print(
    agency_df["agencia_id"]
    .duplicated()
    .sum()
)

# --------------------------------------------------
# EXPORTAR PARQUET
# --------------------------------------------------

print("\n===================================")
print("EXPORTANDO PARQUET")
print("===================================\n")

agency_df.to_parquet(
    PARQUET_PATH / "dim_agencia.parquet",
    engine="pyarrow",
    compression="snappy",
    index=False
)

# --------------------------------------------------
# FIN
# --------------------------------------------------

print("ETL DIM_AGENCIA FINALIZADO\n")

print(f"Archivo generado en:\n{PARQUET_PATH}")