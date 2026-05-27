import pandas as pd

import streamlit as st

import duckdb

from pathlib import Path

from src.config.settings import (

    MARTS_PATH,
    DUCKDB_PATH

)

# ==================================================
# GENERIC PARQUET LOADER
# ==================================================

@st.cache_data

def load_parquet_file(

    filename

):

    try:

        path = MARTS_PATH / filename

        if not path.exists():

            raise FileNotFoundError(

                f"Archivo no encontrado: {path}"

            )

        df = pd.read_parquet(path)

        return df

    except Exception as e:

        st.error(

            f"Error cargando {filename}: {e}"

        )

        return pd.DataFrame()

# ==================================================
# SALES MONTHLY
# ==================================================

@st.cache_data

def load_sales_monthly():

    return load_parquet_file(

        "mart_sales_monthly.parquet"

    )

# ==================================================
# DAILY SALES
# ==================================================

@st.cache_data

def load_daily_sales():

    return load_parquet_file(

        "mart_daily_sales.parquet"

    )

# ==================================================
# BRAND PERFORMANCE
# ==================================================

@st.cache_data

def load_brand_performance():

    return load_parquet_file(

        "mart_brand_performance.parquet"

    )

# ==================================================
# CATEGORY PERFORMANCE
# ==================================================

@st.cache_data

def load_category_performance():

    return load_parquet_file(

        "mart_category_performance.parquet"

    )

# ==================================================
# CHANNEL PERFORMANCE
# ==================================================

@st.cache_data

def load_channel_performance():

    return load_parquet_file(

        "mart_channel_performance.parquet"

    )

# ==================================================
# SALES ENRICHED
# ==================================================

@st.cache_data

def load_sales_enriched():

    try:

        con = duckdb.connect(

            str(DUCKDB_PATH)

        )

        query = """

        SELECT *

        FROM vw_sales_enriched

        """

        df = con.execute(

            query

        ).fetchdf()

        con.close()

        return df

    except Exception as e:

        st.error(

            f"Error cargando semantic layer: {e}"

        )

        return pd.DataFrame()

# ==================================================
# CLEAR CACHE
# ==================================================

def clear_all_caches():

    st.cache_data.clear()