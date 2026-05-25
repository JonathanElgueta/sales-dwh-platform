import streamlit as st
import plotly.express as px

# ==================================================
# HOME PAGE
# ==================================================

def render_home(

    filtered_sales_df,
    filtered_brand_df

):

    # ==================================================
    # KPIS
    # ==================================================

    venta_total = int(
        filtered_sales_df["venta_total"].sum()
    )

    pct_devolucion = round(
        filtered_sales_df["pct_devolucion"].mean(),
        2
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
    # KPI COLORS
    # ==================================================

    if variacion_pct >= 0:

        variation_color = "#00FF99"

        variation_icon = "▲"

    else:

        variation_color = "#FF4B4B"

        variation_icon = "▼"

    # ==================================================
    # TITLE
    # ==================================================

    st.markdown(

        """
<div class='section-title'>
🚀 SALES DWH PLATFORM
</div>
""",

        unsafe_allow_html=True

    )

    st.info(
        "Sistema analítico empresarial basado en Data Warehouse."
    )

    st.markdown("---")

    # ==================================================
    # KPI ROW
    # ==================================================

    col1, col2, col3, col4 = st.columns(4)

    # KPI 1

    with col1:

        st.markdown(

            f"""
<div class="kpi-card">

<div class="kpi-title">
Venta Total
</div>

<div class="kpi-value">
${venta_total:,.0f}
</div>

<div style="
color:{variation_color};
margin-top:10px;
font-size:18px;
font-weight:bold;
">

{variation_icon} {variacion_pct}%

</div>

</div>
""",

            unsafe_allow_html=True

        )

    # KPI 2

    with col2:

        st.markdown(

            f"""
<div class="kpi-card">

<div class="kpi-title">
% Devolución
</div>

<div class="kpi-value">
{pct_devolucion}%
</div>

</div>
""",

            unsafe_allow_html=True

        )

    # KPI 3

    with col3:

        st.markdown(

            f"""
<div class="kpi-card">

<div class="kpi-title">
Venta Promedio
</div>

<div class="kpi-value">
${venta_promedio:,.0f}
</div>

</div>
""",

            unsafe_allow_html=True

        )

    # KPI 4

    with col4:

        st.markdown(

            f"""
<div class="kpi-card">

<div class="kpi-title">
Top Marca
</div>

<div class="kpi-value">
{top_brand}
</div>

</div>
""",

            unsafe_allow_html=True

        )

    st.markdown("---")

    # ==================================================
    # EXECUTIVE SUMMARY
    # ==================================================

    st.subheader(
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

    if pct_devolucion >= 10:

        devolucion_message = (
            "🚨 Nivel de devoluciones ALTO."
        )

    elif pct_devolucion >= 5:

        devolucion_message = (
            "⚠️ Nivel de devoluciones moderado."
        )

    else:

        devolucion_message = (
            "✅ Devoluciones controladas."
        )

    brand_message = (
        f"🏆 {top_brand} lidera actualmente las ventas."
    )

    st.success(

        f"""
{sales_message}

{devolucion_message}

{brand_message}
"""

    )

    # ==================================================
    # SALES TREND
    # ==================================================

    st.markdown("---")

    st.subheader(
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

        paper_bgcolor="#0E1117",

        plot_bgcolor="#1C1F26",

        font=dict(color="white")

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # ==================================================
    # YOY COMPARISON
    # ==================================================

    st.markdown("---")

    st.subheader(
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

            paper_bgcolor="#0E1117",

            plot_bgcolor="#1C1F26",

            font=dict(color="white")

        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        latest_growth = round(

            yoy_df.iloc[-1]["growth_pct"],

            2

        )

        if latest_growth >= 0:

            st.success(

                f"""
📈 Crecimiento YoY:

{latest_growth}% vs año anterior.
"""

            )

        else:

            st.error(

                f"""
📉 Caída YoY:

{abs(latest_growth)}% vs año anterior.
"""

            )

    # ==================================================
    # EXECUTIVE ALERTS
    # ==================================================

    st.markdown("---")

    st.subheader(
        "🚨 Alertas Ejecutivas"
    )

    alerts = []

    if pct_devolucion >= 10:

        alerts.append(
            "🚨 Devoluciones críticas detectadas."
        )

    if variacion_pct < 0:

        alerts.append(
            "📉 Caída de ventas vs período anterior."
        )

    top_market_share = round(

        filtered_brand_df["market_share_pct"]
        .max(),

        2

    )

    if top_market_share >= 40:

        alerts.append(
            "🏆 Alta concentración de market share."
        )

    if len(alerts) == 0:

        st.info(
            "✅ No se detectaron alertas críticas."
        )

    else:

        for alert in alerts:

            st.warning(alert)