import streamlit as st
import plotly.express as px

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
    # TITLE
    # ==================================================

    st.title(
        "📊 Dashboard Ejecutivo"
    )

    st.markdown("---")

    # ==================================================
    # TOP BRANDS
    # ==================================================

    st.subheader(
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

        paper_bgcolor="#0E1117",

        plot_bgcolor="#1C1F26",

        font=dict(color="white")

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # ==================================================
    # TOP CATEGORIES
    # ==================================================

    st.markdown("---")

    st.subheader(
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

        paper_bgcolor="#0E1117",

        plot_bgcolor="#1C1F26",

        font=dict(color="white")

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # ==================================================
    # TOP CHANNELS
    # ==================================================

    st.markdown("---")

    st.subheader(
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

        paper_bgcolor="#0E1117",

        plot_bgcolor="#1C1F26",

        font=dict(color="white")

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # ==================================================
    # MARKET SHARE
    # ==================================================

    st.markdown("---")

    st.subheader(
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

        paper_bgcolor="#0E1117",

        font=dict(color="white")

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # ==================================================
    # HEATMAP
    # ==================================================

    st.markdown("---")

    st.subheader(
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

        paper_bgcolor="#0E1117",

        plot_bgcolor="#1C1F26",

        font=dict(color="white")

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # ==================================================
    # EXECUTIVE INSIGHTS
    # ==================================================

    st.markdown("---")

    st.subheader(
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

    st.success(

        f"""
🚀 {top_brand_name} lidera el mercado con
{top_brand_share}% de market share.

📦 La categoría dominante es:
{top_category_name}

🏪 El canal más fuerte es:
{top_channel_name}
"""

    )