from pathlib import Path
import pandas as pd

# --------------------------------------------------
# RUTAS
# --------------------------------------------------

RAW_FILE = Path(
    r"C:\sales-dwh\data\raw\products\Dim_Productos.xlsx"
)

PARQUET_PATH = Path(
    r"C:\sales-dwh\data\parquet\products"
)

# --------------------------------------------------
# CREAR CARPETA PARQUET
# --------------------------------------------------

PARQUET_PATH.mkdir(
    parents=True,
    exist_ok=True
)

# --------------------------------------------------
# INICIO
# --------------------------------------------------

print("\n===================================")
print("INICIANDO ETL DIM_PRODUCTO")
print("===================================\n")

# --------------------------------------------------
# LEER EXCEL
# --------------------------------------------------

print("Leyendo archivo productos...\n")

df = pd.read_excel(
    RAW_FILE,
    sheet_name="Hoja1"
)

# --------------------------------------------------
# RENOMBRAR COLUMNAS
# --------------------------------------------------

print("Renombrando columnas...\n")

df = df.rename(
    columns={
        "CODIGO": "producto_id",
        "DESCRIPCION": "producto_nombre",
        "MARCA": "marca",
        "CATEGORIA": "categoria",
        "LINEA": "linea",
        "CUPO_CONTENEDOR": "cupo_contenedor",
        "UNIDAD_EQUIVALENTE": "unidad_equivalente",
        "GRAMAJE": "gramaje",
        "CLUSTER": "cluster",
        "NEGOCIO": "negocio",
        "CATEGORIA_PROPIA": "categoria_propia",
        "CATEGORIA_OR": "categoria_or"
    }
)

# --------------------------------------------------
# NORMALIZAR TIPOS
# --------------------------------------------------

print("Normalizando tipos...\n")

df["producto_id"] = df["producto_id"].astype(str)

# --------------------------------------------------
# LIMPIEZA NULOS
# --------------------------------------------------

print("Tratando valores nulos...\n")

df["linea"] = df["linea"].fillna(
    "SIN_LINEA"
)

# --------------------------------------------------
# VALIDACIONES
# --------------------------------------------------

print("===================================")
print("VALIDACIONES")
print("===================================\n")

print("Dimensiones:")
print(df.shape)

print("\nNulos:")
print(df.isnull().sum())

print("\nDuplicados producto_id:")
print(df["producto_id"].duplicated().sum())

# --------------------------------------------------
# EXPORTAR PARQUET
# --------------------------------------------------

print("\n===================================")
print("EXPORTANDO PARQUET")
print("===================================\n")

df.to_parquet(
    PARQUET_PATH / "dim_producto.parquet",
    engine="pyarrow",
    index=False,
    compression="snappy"
)

# --------------------------------------------------
# FIN
# --------------------------------------------------

print("ETL DIM_PRODUCTO FINALIZADO\n")

print(f"Archivo generado en:\n{PARQUET_PATH}")