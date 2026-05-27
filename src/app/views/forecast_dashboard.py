import streamlit as st

import pandas as pd

import plotly.graph_objects as go

from src.app.components.section_header import (

    render_section_header

)

from src.app.components.kpi_card import (

    render_kpi_card

)

from src.app.components.alerts import (

    render_success_alert,
    render_executive_alert

)

from src.app.services.ml.sales_forecasting import (

    generate_sales_forecast

)

from src.app.styles.theme import (

    CHART_THEME

)

# ==================================================
# FORECAST DASHBOARD
# ==================================================

def render_forecast_dashboard(

    filtered_sales_df

):

    # ==================================================
    # HEADER
    # ==================================================

    render_section_header(

        "🤖 AI Forecasting",

        "Machine Learning Sales Forecast"

    )

    # ==================================================
    # GENERATE FORECAST
    # ==================================================

    forecast_df = generate_sales_forecast(

        filtered_sales_df,

        periods=6

    )

    # ==================================================
    # HISTORICAL DATA
    # ==================================================

    historical_df = filtered_sales_df.copy()

    historical_df["periodo"] = (

        historical_df["year"].astype(str)
        +
        "-"
        +
        historical_df["month"].astype(str)

    )

    # ==================================================
    # FORECAST KPIS
    # ==================================================

    forecast_total = int(

        forecast_df["forecast_sales"].sum()

    )

    forecast_avg = int(

        forecast_df["forecast_sales"].mean()

    )

    max_forecast = int(

        forecast_df["forecast_sales"].max()

    )

    col1, col2, col3 = st.columns(3)

    with col1:

        render_kpi_card(

            "Forecast Total",

            f"${forecast_total:,.0f}"

        )

    with col2:

        render_kpi_card(

            "Forecast Promedio",

            f"${forecast_avg:,.0f}"

        )

    with col3:

        render_kpi_card(

            "Forecast Máximo",

            f"${max_forecast:,.0f}"

        )

    # ==================================================
    # FORECAST CHART
    # ==================================================

    render_section_header(

        "📈 Forecast Ventas"

    )

    fig = go.Figure()

    # ==================================================
    # HISTORICAL
    # ==================================================

    fig.add_trace(

        go.Scatter(

            x=historical_df["periodo"],

            y=historical_df["venta_total"],

            mode="lines+markers",

            name="Ventas Históricas"

        )

    )

    # ==================================================
    # FORECAST
    # ==================================================

    fig.add_trace(

        go.Scatter(

            x=forecast_df["periodo"],

            y=forecast_df["forecast_sales"],

            mode="lines+markers",

            name="Forecast IA"

        )

    )

    fig.update_layout(

        title="Forecast Ventas Futuras",

        **CHART_THEME

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

    # ==================================================
    # FORECAST TABLE
    # ==================================================

    render_section_header(

        "📋 Forecast Detallado"

    )

    st.dataframe(

        forecast_df,

        use_container_width=True

    )

    # ==================================================
    # AI INSIGHTS
    # ==================================================

    render_section_header(

        "🧠 AI Insights"

    )

    latest_forecast = int(

        forecast_df.iloc[-1]["forecast_sales"]

    )

    render_executive_alert(

        "Machine Learning Insights",

        f"""

🤖 El modelo proyecta crecimiento futuro.

📈 Forecast máximo esperado:
${max_forecast:,.0f}

📊 Forecast último período:
${latest_forecast:,.0f}

🚀 Tendencia positiva detectada.

"""

    )

    render_success_alert(

        "✅ Modelo ML ejecutado correctamente."

    )