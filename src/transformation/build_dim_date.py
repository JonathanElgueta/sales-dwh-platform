from pathlib import Path
import pandas as pd

# --------------------------------------------------
# RUTAS
# --------------------------------------------------

OUTPUT_PATH = Path(
    r"C:\sales-dwh\data\parquet\date"
)

OUTPUT_FILE = OUTPUT_PATH / "dim_date.parquet"

# --------------------------------------------------
# CREAR CARPETA
# --------------------------------------------------

OUTPUT_PATH.mkdir(
    parents=True,
    exist_ok=True
)

# --------------------------------------------------
# RANGO FECHAS
# --------------------------------------------------

START_DATE = "2023-01-01"
END_DATE = "2030-12-31"

# --------------------------------------------------
# CREAR DATAFRAME
# --------------------------------------------------

print("\n===================================")
print("CREANDO DIM_DATE")
print("===================================\n")

date_range = pd.date_range(
    start=START_DATE,
    end=END_DATE,
    freq="D"
)

df = pd.DataFrame({
    "date": date_range
})

# --------------------------------------------------
# CALENDARIO NORMAL
# --------------------------------------------------

df["year"] = df["date"].dt.year

df["quarter"] = df["date"].dt.quarter

df["month"] = df["date"].dt.month

df["month_name"] = (
    df["date"]
    .dt
    .month_name()
)

# SEMANA NORMAL ISO

df["week"] = (
    df["date"]
    .dt
    .isocalendar()
    .week
    .astype(int)
)

df["iso_year"] = (
    df["date"]
    .dt
    .isocalendar()
    .year
    .astype(int)
)

# --------------------------------------------------
# SEMANA BIMBO
# JUEVES A MIÉRCOLES
# --------------------------------------------------

df["fecha_semana_bimbo"] = (
    df["date"]
    - pd.to_timedelta(3, unit="D")
)

df["semana_bimbo"] = (
    df["fecha_semana_bimbo"]
    .dt
    .isocalendar()
    .week
    .astype(int)
)

df["year_semana_bimbo"] = (
    df["fecha_semana_bimbo"]
    .dt
    .isocalendar()
    .year
    .astype(int)
)

# --------------------------------------------------
# ATRIBUTOS DÍA
# --------------------------------------------------

df["day"] = df["date"].dt.day

df["day_of_week"] = (
    df["date"]
    .dt
    .dayofweek
)

df["day_name"] = (
    df["date"]
    .dt
    .day_name()
)

# --------------------------------------------------
# FLAGS
# --------------------------------------------------

df["is_weekend"] = (
    df["day_of_week"]
    .isin([5, 6])
)

# --------------------------------------------------
# DATE KEY
# --------------------------------------------------

df["date_key"] = (
    df["date"]
    .dt
    .strftime("%Y%m%d")
    .astype(int)
)

# --------------------------------------------------
# ORDEN FINAL COLUMNAS
# --------------------------------------------------

df = df[
    [
        "date_key",

        "date",

        # CALENDARIO NORMAL
        "year",
        "quarter",
        "month",
        "month_name",
        "week",
        "iso_year",

        # CALENDARIO BIMBO
        "semana_bimbo",
        "year_semana_bimbo",

        # ATRIBUTOS DÍA
        "day",
        "day_of_week",
        "day_name",

        # FLAGS
        "is_weekend"
    ]
]

# --------------------------------------------------
# VALIDACIONES
# --------------------------------------------------

print("===================================")
print("DIMENSIONES")
print("===================================\n")

print(df.shape)

print("\n===================================")
print("COLUMNAS")
print("===================================\n")

print(df.columns)

print("\n===================================")
print("PRIMERAS FILAS")
print("===================================\n")

print(df.head(15))

print("\n===================================")
print("ÚLTIMAS FILAS")
print("===================================\n")

print(df.tail())

print("\n===================================")
print("NULOS")
print("===================================\n")

print(df.isnull().sum())

print("\n===================================")
print("EJEMPLO SEMANA BIMBO")
print("===================================\n")

sample = df[
    [
        "date",
        "day_name",
        "week",
        "semana_bimbo"
    ]
].head(15)

print(sample)

# --------------------------------------------------
# EXPORTAR PARQUET
# --------------------------------------------------

print("\n===================================")
print("EXPORTANDO DIM_DATE")
print("===================================\n")

df.to_parquet(
    OUTPUT_FILE,
    engine="pyarrow",
    compression="snappy",
    index=False
)

print("Dimensión exportada correctamente\n")

print(f"Ruta:\n{OUTPUT_FILE}")

print("\n===================================")
print("DIM_DATE FINALIZADA")
print("===================================\n")