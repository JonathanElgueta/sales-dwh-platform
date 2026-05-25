from pathlib import Path
import pandas as pd

# --------------------------------------------------
# CONFIGURACIÓN
# --------------------------------------------------

SALES_PATH = Path(r"C:\sales-dwh\data\raw\sales")

# --------------------------------------------------
# BUSCAR ARCHIVOS
# --------------------------------------------------

files = list(SALES_PATH.glob("*.xlsx"))

print("\n===================================")
print("CARGANDO ARCHIVOS")
print("===================================\n")

# --------------------------------------------------
# LEER Y UNIR ARCHIVOS
# --------------------------------------------------

df_list = []

for file in files:

    print(f"Leyendo: {file.name}")

    df = pd.read_excel(
        file,
        sheet_name="Hoja1"
    )

    df_list.append(df)

# --------------------------------------------------
# UNIFICAR DATA
# --------------------------------------------------

sales_df = pd.concat(
    df_list,
    ignore_index=True
)

# --------------------------------------------------
# INFORMACIÓN GENERAL
# --------------------------------------------------

print("\n===================================")
print("DIMENSIONES DATASET")
print("===================================\n")

print(sales_df.shape)

# --------------------------------------------------
# TIPOS DE DATOS
# --------------------------------------------------

print("\n===================================")
print("TIPOS DATOS")
print("===================================\n")

print(sales_df.dtypes)

# --------------------------------------------------
# NULOS
# --------------------------------------------------

print("\n===================================")
print("VALORES NULOS")
print("===================================\n")

nulls = sales_df.isnull().sum()

print(nulls)

# --------------------------------------------------
# DUPLICADOS
# --------------------------------------------------

print("\n===================================")
print("DUPLICADOS")
print("===================================\n")

duplicates = sales_df.duplicated().sum()

print(f"Filas duplicadas: {duplicates}")

# --------------------------------------------------
# ESTADÍSTICAS NUMÉRICAS
# --------------------------------------------------

print("\n===================================")
print("ESTADÍSTICAS")
print("===================================\n")

print(sales_df.describe())

# --------------------------------------------------
# RANGO FECHAS
# --------------------------------------------------

print("\n===================================")
print("RANGO FECHAS")
print("===================================\n")

print(f"Fecha mínima: {sales_df['Fecha'].min()}")
print(f"Fecha máxima: {sales_df['Fecha'].max()}")

# --------------------------------------------------
# VALORES ÚNICOS
# --------------------------------------------------

print("\n===================================")
print("CARDINALIDAD")
print("===================================\n")

columns_to_check = [
    "Canal",
    "Subcanal",
    "Cadena"
]

for col in columns_to_check:

    print(f"\n{col}")

    print(f"Valores únicos: {sales_df[col].nunique()}")