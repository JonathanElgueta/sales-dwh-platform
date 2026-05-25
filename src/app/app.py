import sys
from pathlib import Path

# ==================================================
# PATH FIX
# ==================================================

ROOT_PATH = Path(__file__).resolve().parents[2]

if str(ROOT_PATH) not in sys.path:
    sys.path.append(str(ROOT_PATH))

# ==================================================
# IMPORTS
# ==================================================

import streamlit as st

from src.app.services.data_loader import (

    load_sales_monthly,
    load_brand_performance,
    load_category_performance,
    load_channel_performance

)

# ==================================================
# PAGE IMPORTS
# ==================================================

from src.app.views.home import render_home

from src.app.views.executive_dashboard import (
    render_executive_dashboard
)

from src.app.views.brand_analytics import (
    render_brand_analytics
)

from src.app.views.pipeline_monitor import (
    render_pipeline_monitor
)

from src.app.views.qa_monitor import (
    render_qa_monitor
)

# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(

    page_title="Sales DWH Platform",

    page_icon="🚀",

    layout="wide",

    initial_sidebar_state="expanded"

)

# ==================================================
# GLOBAL CSS
# ==================================================

st.markdown(

    """
<style>

.main {
    background-color: #0B1120;
}

section[data-testid="stSidebar"] {

    background: linear-gradient(
        180deg,
        #161B26 0%,
        #0F172A 100%
    );

    border-right: 1px solid #1E293B;
}

.section-title {

    color: white;

    font-size: 48px;

    font-weight: 800;

    margin-bottom: 10px;

    letter-spacing: -1px;
}

.kpi-card {

    background: linear-gradient(
        145deg,
        #1E293B,
        #111827
    );

    padding: 28px;

    border-radius: 18px;

    border: 1px solid #334155;

    box-shadow:
        0px 10px 30px rgba(0,0,0,0.35);

    min-height: 180px;
}

.kpi-title {

    color: #94A3B8;

    font-size: 15px;

    font-weight: 600;

    margin-bottom: 14px;

    text-transform: uppercase;

    letter-spacing: 1px;
}

.kpi-value {

    color: white;

    font-size: 40px;

    font-weight: 800;

    line-height: 1.1;
}

</style>
""",

    unsafe_allow_html=True

)

# ==================================================
# LOAD DATA
# ==================================================

sales_monthly_df = load_sales_monthly()

brand_df = load_brand_performance()

category_df = load_category_performance()

channel_df = load_channel_performance()

# ==================================================
# SIDEBAR
# ==================================================

st.sidebar.title(
    "🚀 SALES DWH"
)

st.sidebar.markdown("---")

st.sidebar.success(
    "Plataforma Operacional"
)

# ==================================================
# FILTERS
# ==================================================

st.sidebar.markdown("---")

st.sidebar.subheader(
    "🎯 Filtros Globales"
)

available_years = sorted(
    sales_monthly_df["year"].unique()
)

selected_years = st.sidebar.multiselect(

    "Seleccionar Año",

    available_years,

    default=available_years

)

available_months = sorted(
    sales_monthly_df["month"].unique()
)

selected_months = st.sidebar.multiselect(

    "Seleccionar Mes",

    available_months,

    default=available_months

)

# ==================================================
# FILTER DATA
# ==================================================

filtered_sales_df = sales_monthly_df[

    (sales_monthly_df["year"].isin(selected_years))
    &

    (sales_monthly_df["month"].isin(selected_months))

]

filtered_brand_df = brand_df[

    (brand_df["year"].isin(selected_years))
    &

    (brand_df["month"].isin(selected_months))

]

filtered_category_df = category_df[

    (category_df["year"].isin(selected_years))
    &

    (category_df["month"].isin(selected_months))

]

filtered_channel_df = channel_df[

    (channel_df["year"].isin(selected_years))
    &

    (channel_df["month"].isin(selected_months))

]

# ==================================================
# NAVIGATION
# ==================================================

st.sidebar.markdown("---")

selected_page = st.sidebar.radio(

    "Navegación",

    [

        "🏠 Inicio",

        "📊 Dashboard Ejecutivo",

        "📈 Analytics Marcas",

        "🚀 Ejecutar Pipeline",

        "⚙️ Monitor QA"

    ]

)

# ==================================================
# ROUTER
# ==================================================

if selected_page == "🏠 Inicio":

    render_home(
        filtered_sales_df,
        filtered_brand_df
    )

elif selected_page == "📊 Dashboard Ejecutivo":

    render_executive_dashboard(
        filtered_brand_df,
        filtered_category_df,
        filtered_channel_df,
        filtered_sales_df
    )

elif selected_page == "📈 Analytics Marcas":

    render_brand_analytics(
        filtered_brand_df,
        filtered_category_df
    )

elif selected_page == "🚀 Ejecutar Pipeline":

    render_pipeline_monitor()

elif selected_page == "⚙️ Monitor QA":

    render_qa_monitor()