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
    load_channel_performance,
    load_daily_sales

)

# ==================================================
# AUTH IMPORTS
# ==================================================

from src.app.auth.auth_service import (

    create_auth_database,
    create_user

)

from src.app.auth.session_manager import (

    init_session,
    is_authenticated,
    logout_user,
    get_username,
    get_role

)

from src.app.auth.login import (

    render_login

)

from src.app.auth.permissions import (

    has_permission

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

from src.app.views.forecast_dashboard import (

    render_forecast_dashboard

)

from src.app.views.anomaly_dashboard import (

    render_anomaly_dashboard

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
# INIT AUTH SYSTEM
# ==================================================

init_session()

create_auth_database()

# ==================================================
# CREATE USERS
# ==================================================

from src.app.auth.auth_service import (

    user_exists

)

# ==================================================
# CREATE USERS
# ==================================================

if not user_exists("admin"):

    create_user(

        "admin",
        "admin123",
        "admin"

    )

if not user_exists("qa_user"):

    create_user(

        "qa_user",
        "qa123",
        "qa"

    )

if not user_exists("ejecutivo_user"):

    create_user(

        "ejecutivo_user",
        "exec123",
        "ejecutivo"

    )

if not user_exists("ops_user"):

    create_user(

        "ops_user",
        "ops123",
        "operaciones"

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
</style>
""",

    unsafe_allow_html=True

)

# ==================================================
# AUTHENTICATION
# ==================================================

if not is_authenticated():

    render_login()

    st.stop()

# ==================================================
# LOAD DATA
# ==================================================

sales_monthly_df = load_sales_monthly()

daily_sales_df = load_daily_sales()

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

    f"👤 {get_username()}"

)

st.sidebar.caption(

    f"Rol: {get_role()}"

)

if st.sidebar.button(

    "Cerrar Sesión"

):

    logout_user()

    st.rerun()

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
# ROLE-BASED NAVIGATION
# ==================================================

st.sidebar.markdown("---")

available_pages = []

if has_permission(

    get_role(),
    "home"

):

    available_pages.append(

        "🏠 Inicio"

    )

if has_permission(

    get_role(),
    "dashboard"

):

    available_pages.append(

        "📊 Dashboard Ejecutivo"

    )

if has_permission(

    get_role(),
    "brands"

):

    available_pages.append(

        "📈 Analytics Marcas"

    )

if has_permission(

    get_role(),
    "forecast"

):

    available_pages.append(

        "🤖 AI Forecasting"

    )    

if has_permission(

    get_role(),
    "anomaly"

):

    available_pages.append(

        "🤖 AI Anomaly Detection"

    )


if has_permission(

    get_role(),
    "pipeline"

):

    available_pages.append(

        "🚀 Ejecutar Pipeline"

    )

if has_permission(

    get_role(),
    "qa"

):

    available_pages.append(

        "⚙️ Monitor QA"

    )

selected_page = st.sidebar.radio(

    "Navegación",

    available_pages

)

# ==================================================
# ROUTER
# ==================================================

if selected_page == "🏠 Inicio":

    render_home(

        filtered_sales_df,
        filtered_brand_df,
        daily_sales_df

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

elif selected_page == "🤖 AI Forecasting":

    render_forecast_dashboard(

        filtered_sales_df

    )    

elif selected_page == "🤖 AI Anomaly Detection":

    render_anomaly_dashboard(

        filtered_sales_df

    )    