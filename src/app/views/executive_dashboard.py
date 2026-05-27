import streamlit as st

import plotly.express as px

from src.app.components.section_header import (

    render_section_header

)

from src.app.components.alerts import (

    render_executive_alert

)

from src.app.styles.theme import (

    CHART_THEME

)

# ==================================================
# EXECUTIVE DASHBOARD
# ==================================================

def render_executive_dashboard(

    filtered_brand_df,
    filtered_category_df,
    filtered_channel_df,
    filtered_sales_df

):

    # ==================================================
    # HEADER
    # ==================================================

    render_section_header(

        "📊 Dashboard Ejecutivo",

        "Executive Business Intelligence Overview"

    )

    # ==================================================
    # TOP BRANDS
    # ==================================================

    render_section_header(

        "🏆 Top Marcas"

    )

    top_brands = (

        filtered_brand_df
        .groupby("marca", as_index=False)
        .agg({

            "venta_total": "sum",
            "market_share_pct": "mean"

        })
        .sort_values(
            by="venta_total",
            ascending=False
        )
        .head(10)

    )

    fig = px.bar(

        top_brands,

        x="marca",

        y="venta_total",

        text_auto=".2s",

        title="Top 10 Marcas"

    )

    fig.update_layout(

        **CHART_THEME

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

    # ==================================================
    # TOP CATEGORIES
    # ==================================================

    render_section_header(

        "📦 Top Categorías"

    )

    top_categories = (

        filtered_category_df
        .groupby("categoria", as_index=False)
        .agg({

            "venta_total": "sum"

        })
        .sort_values(
            by="venta_total",
            ascending=False
        )
        .head(10)

    )

    fig = px.bar(

        top_categories,

        x="categoria",

        y="venta_total",

        text_auto=".2s",

        title="Top Categorías"

    )

    fig.update_layout(

        **CHART_THEME

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

    # ==================================================
    # TOP CHANNELS
    # ==================================================

    render_section_header(

        "🏪 Top Canales"

    )

    top_channels = (

        filtered_channel_df
        .groupby("cadena", as_index=False)
        .agg({

            "venta_total": "sum"

        })
        .sort_values(
            by="venta_total",
            ascending=False
        )
        .head(10)

    )

    fig = px.bar(

        top_channels,

        x="cadena",

        y="venta_total",

        text_auto=".2s",

        title="Top Canales"

    )

    fig.update_layout(

        **CHART_THEME

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

    # ==================================================
    # MARKET SHARE
    # ==================================================

    render_section_header(

        "🥧 Market Share"

    )

    fig = px.pie(

        top_brands,

        names="marca",

        values="market_share_pct",

        hole=0.5,

        title="Participación Mercado"

    )

    fig.update_layout(

        **CHART_THEME

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

    # ==================================================
    # HEATMAP
    # ==================================================

    render_section_header(

        "🔥 Heatmap Ventas"

    )

    heatmap_df = filtered_sales_df.copy()

    heatmap_pivot = heatmap_df.pivot_table(

        index="year",

        columns="month",

        values="venta_total",

        aggfunc="sum"

    )

    fig = px.imshow(

        heatmap_pivot,

        text_auto=".2s",

        aspect="auto",

        title="Heatmap Ventas"

    )

    fig.update_layout(

        **CHART_THEME

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

    # ==================================================
    # EXECUTIVE INSIGHTS
    # ==================================================

    render_section_header(

        "🧠 Insights Ejecutivos"

    )

    top_brand_name = top_brands.iloc[0]["marca"]

    top_brand_share = round(

        top_brands.iloc[0]["market_share_pct"],

        2

    )

    top_category_name = (

        top_categories.iloc[0]["categoria"]

    )

    top_channel_name = (

        top_channels.iloc[0]["cadena"]

    )

    render_executive_alert(

        "Executive Insights",

        f"""

🚀 {top_brand_name} lidera el mercado con
{top_brand_share}% de market share.

📦 La categoría dominante es:
{top_category_name}

🏪 El canal más fuerte es:
{top_channel_name}

"""

    )