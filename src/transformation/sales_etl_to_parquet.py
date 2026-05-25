from pathlib import Path
import pandas as pd

# --------------------------------------------------
# RUTAS
# --------------------------------------------------

RAW_PATH = Path(r"C:\sales-dwh\data\raw\sales")

PARQUET_PATH = Path(r"C:\sales-dwh\data\parquet\sales")

# --------------------------------------------------
# CREAR CARPETA PARQUET
# --------------------------------------------------

PARQUET_PATH.mkdir(
    parents=True,
    exist_ok=True
)

# --------------------------------------------------
# BUSCAR ARCHIVOS
# --------------------------------------------------

files = list(RAW_PATH.glob("*.xlsx"))

print("\n===================================")
print("INICIO ETL SALES")
print("===================================\n")

print(f"Archivos encontrados: {len(files)}\n")

# --------------------------------------------------
# LEER ARCHIVOS
# --------------------------------------------------

df_list = []

for file in files:

    print(f"Leyendo archivo: {file.name}")

    df = pd.read_excel(
        file,
        sheet_name="Hoja1"
    )

    df_list.append(df)

# --------------------------------------------------
# UNIFICAR DATA
# --------------------------------------------------

print("\nUnificando datasets...\n")

sales_df = pd.concat(
    df_list,
    ignore_index=True
)

# --------------------------------------------------
# VALIDAR DIMENSIONES
# --------------------------------------------------

print("===================================")
print("DIMENSIONES")
print("===================================\n")

print(sales_df.shape)

# --------------------------------------------------
# NORMALIZAR TIPOS
# --------------------------------------------------

print("\nNormalizando tipos de datos...\n")

sales_df["Producto_ID"] = sales_df["Producto_ID"].astype(str)

# --------------------------------------------------
# CREAR PARTICIONES
# --------------------------------------------------

print("\nCreando columnas de partición...\n")

sales_df["year"] = sales_df["Fecha"].dt.year

sales_df["month"] = sales_df["Fecha"].dt.month

# --------------------------------------------------
# EXPORTAR PARQUET
# --------------------------------------------------

print("\n===================================")
print("EXPORTANDO PARQUET")
print("===================================\n")

sales_df.to_parquet(
    PARQUET_PATH,
    engine="pyarrow",
    partition_cols=["year", "month"],
    index=False,
    compression="snappy"
)

# --------------------------------------------------
# FIN
# --------------------------------------------------

print("\n===================================")
print("ETL FINALIZADO")
print("===================================\n")

print(f"Parquet generado en:\n{PARQUET_PATH}")