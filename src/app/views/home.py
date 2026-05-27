import streamlit as st

import pandas as pd

import plotly.express as px

from src.app.components.kpi_card import (

    render_kpi_card

)

from src.app.components.section_header import (

    render_section_header

)

from src.app.components.alerts import (

    render_executive_alert,
    render_info_alert,
    render_warning_alert,
    render_success_alert,
    render_error_alert

)

from src.app.styles.theme import (

    CHART_THEME

)

# ==================================================
# HOME PAGE
# ==================================================

def render_home(

    filtered_sales_df,
    filtered_brand_df,
    daily_sales_df

):

    # ==================================================
    # KPIS
    # ==================================================

    venta_total = int(

        filtered_sales_df["venta_total"].sum()

    )

    venta_promedio = int(

        filtered_sales_df["venta_total"].mean()

    )

    top_brand = (

        filtered_brand_df
        .groupby("marca")["venta_total"]
        .sum()
        .sort_values(ascending=False)
        .index[0]

    )

    # ==================================================
    # KPI VARIATION
    # ==================================================

    if len(filtered_sales_df) >= 2:

        current_sales = (

            filtered_sales_df.iloc[-1]["venta_total"]

        )

        previous_sales = (

            filtered_sales_df.iloc[-2]["venta_total"]

        )

        variacion_pct = round(

            (

                (current_sales - previous_sales)

                /

                previous_sales

            ) * 100,

            2

        )

    else:

        variacion_pct = 0

    # ==================================================
    # KPI ICON
    # ==================================================

    if variacion_pct >= 0:

        variation_icon = "📈"

    else:

        variation_icon = "📉"

    # ==================================================
    # HEADER
    # ==================================================

    render_section_header(

        "🚀 SALES DWH PLATFORM",

        "Enterprise Analytics Platform"

    )

    render_info_alert(

        "Sistema analítico empresarial basado en Data Warehouse."

    )

    # ==================================================
    # KPI ROW
    # ==================================================

    col1, col2, col3 = st.columns(3)

    with col1:

        render_kpi_card(

            "Venta Total",

            f"${venta_total:,.0f}",

            f"{variation_icon} {variacion_pct}%"

        )

    with col2:

        render_kpi_card(

            "Venta Promedio",

            f"${venta_promedio:,.0f}"

        )

    with col3:

        render_kpi_card(

            "Top Marca",

            top_brand

        )

    # ==================================================
    # DATA FRESHNESS
    # ==================================================

    daily_sales_df["fecha"] = pd.to_datetime(

        daily_sales_df["fecha"]

    )

    latest_date = daily_sales_df["fecha"].max()

    latest_date = latest_date.strftime(

        "%d-%m-%Y"

    )

    render_info_alert(

        f"📅 Data Venta Sell In actualizada hasta: {latest_date}"

    )

    # ==================================================
    # EXECUTIVE SUMMARY
    # ==================================================

    render_section_header(

        "🧠 Executive Summary"

    )

    if variacion_pct >= 0:

        sales_message = (

            f"📈 Las ventas crecieron "

            f"{variacion_pct}% "

            f"vs período anterior."

        )

    else:

        sales_message = (

            f"📉 Las ventas cayeron "

            f"{abs(variacion_pct)}% "

            f"vs período anterior."

        )

    brand_message = (

        f"🏆 {top_brand} lidera actualmente las ventas."

    )

    render_executive_alert(

        "Resumen Ejecutivo",

        f"""

{sales_message}

{brand_message}

"""

    )

    # ==================================================
    # SALES TREND
    # ==================================================

    render_section_header(

        "📈 Tendencia Ventas Mensuales"

    )

    chart_df = filtered_sales_df.copy()

    chart_df["periodo"] = (

        chart_df["year"].astype(str)
        +
        "-"
        +
        chart_df["month"].astype(str)

    )

    fig = px.line(

        chart_df,

        x="periodo",

        y="venta_total",

        markers=True,

        title="Ventas Mensuales"

    )

    fig.update_layout(

        **CHART_THEME

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

    # ==================================================
    # YOY COMPARISON
    # ==================================================

    render_section_header(

        "📊 Comparativo Year over Year"

    )

    yoy_df = (

        filtered_sales_df
        .groupby("year", as_index=False)
        .agg({

            "venta_total": "sum"

        })
        .sort_values("year")

    )

    if len(yoy_df) >= 2:

        yoy_df["growth_pct"] = (

            yoy_df["venta_total"]
            .pct_change()

        ) * 100

        fig = px.bar(

            yoy_df,

            x="year",

            y="venta_total",

            text_auto=".2s",

            color="growth_pct",

            title="Ventas por Año"

        )

        fig.update_layout(

            **CHART_THEME

        )

        st.plotly_chart(

            fig,

            use_container_width=True

        )

    # ==================================================
    # EXECUTIVE ALERTS
    # ==================================================

    render_section_header(

        "🚨 Alertas Ejecutivas"

    )

    top_market_share = round(

        filtered_brand_df["market_share_pct"]
        .max(),

        2

    )

    if top_market_share >= 40:

        render_warning_alert(

            "🏆 Alta concentración de market share."

        )

    else:

        render_info_alert(

            "✅ No se detectaron alertas críticas."

        )