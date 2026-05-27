import streamlit as st

import plotly.express as px

from src.app.components.kpi_card import (

    render_kpi_card

)

from src.app.components.section_header import (

    render_section_header

)

from src.app.components.alerts import (

    render_executive_alert,
    render_success_alert

)

from src.app.styles.theme import (

    CHART_THEME

)

# ==================================================
# BRAND ANALYTICS
# ==================================================

def render_brand_analytics(

    filtered_brand_df,
    filtered_category_df

):

    # ==================================================
    # HEADER
    # ==================================================

    render_section_header(

        "📈 Analytics Marcas",

        "Brand Performance Analytics"

    )

    # ==================================================
    # SELECT BRAND
    # ==================================================

    available_brands = sorted(

        filtered_brand_df["marca"]
        .dropna()
        .astype(str)
        .unique()

    )

    selected_brand = st.selectbox(

        "Seleccionar Marca",

        available_brands

    )

    # ==================================================
    # FILTER BRAND
    # ==================================================

    brand_analysis_df = filtered_brand_df[

        filtered_brand_df["marca"]
        == selected_brand

    ]

    # ==================================================
    # KPIS
    # ==================================================

    venta_total_brand = int(

        brand_analysis_df["venta_total"].sum()

    )

    devolucion_brand = round(

        brand_analysis_df["pct_devolucion"].mean(),

        2

    )

    market_share_brand = round(

        brand_analysis_df["market_share_pct"].mean(),

        2

    )

    ranking_brand = int(

        brand_analysis_df["ranking_venta"].mean()

    )

    # ==================================================
    # KPI ROW
    # ==================================================

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        render_kpi_card(

            "Venta Total",

            f"${venta_total_brand:,.0f}"

        )

    with col2:

        render_kpi_card(

            "% Devolución",

            f"{devolucion_brand}%"

        )

    with col3:

        render_kpi_card(

            "Market Share",

            f"{market_share_brand}%"

        )

    with col4:

        render_kpi_card(

            "Ranking",

            f"#{ranking_brand}"

        )

    # ==================================================
    # SALES TREND
    # ==================================================

    render_section_header(

        "📈 Evolución Mensual"

    )

    brand_chart_df = brand_analysis_df.copy()

    brand_chart_df["periodo"] = (

        brand_chart_df["year"].astype(str)
        +
        "-"
        +
        brand_chart_df["month"].astype(str)

    )

    fig = px.line(

        brand_chart_df,

        x="periodo",

        y="venta_total",

        markers=True,

        title=f"Evolución {selected_brand}"

    )

    fig.update_layout(

        **CHART_THEME

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

    # ==================================================
    # MARKET SHARE TREND
    # ==================================================

    render_section_header(

        "🥧 Evolución Market Share"

    )

    fig = px.area(

        brand_chart_df,

        x="periodo",

        y="market_share_pct",

        title="Market Share Mensual"

    )

    fig.update_layout(

        **CHART_THEME

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

    # ==================================================
    # CATEGORY DRILLDOWN
    # ==================================================

    render_section_header(

        "📦 Mix Categorías"

    )

    brand_category_df = (

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

    fig = px.treemap(

        brand_category_df,

        path=["categoria"],

        values="venta_total",

        title=f"Mix Categorías — {selected_brand}"

    )

    fig.update_layout(

        **CHART_THEME

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

    # ==================================================
    # YOY BRAND
    # ==================================================

    render_section_header(

        "📊 Comparativo YoY Marca"

    )

    yoy_brand_df = (

        brand_analysis_df
        .groupby("year", as_index=False)
        .agg({

            "venta_total": "sum"

        })
        .sort_values("year")

    )

    if len(yoy_brand_df) >= 2:

        yoy_brand_df["growth_pct"] = (

            yoy_brand_df["venta_total"]
            .pct_change()

        ) * 100

        fig = px.bar(

            yoy_brand_df,

            x="year",

            y="venta_total",

            color="growth_pct",

            text_auto=".2s",

            title=f"YoY {selected_brand}"

        )

        fig.update_layout(

            **CHART_THEME

        )

        st.plotly_chart(

            fig,

            use_container_width=True

        )

    # ==================================================
    # INSIGHTS
    # ==================================================

    render_section_header(

        "🧠 Insights Marca"

    )

    max_sales = int(

        brand_chart_df["venta_total"].max()

    )

    best_period = brand_chart_df.loc[

        brand_chart_df["venta_total"].idxmax()

    ]

    render_executive_alert(

        "Brand Insights",

        f"""

🚀 {selected_brand} alcanzó su mejor desempeño en:

📅 {best_period['year']}-{best_period['month']}

💰 Venta máxima:
${max_sales:,.0f}

🥧 Market Share promedio:
{market_share_brand}%

"""

    )

    # ==================================================
    # DETAIL TABLE
    # ==================================================

    render_section_header(

        "📋 Detalle Marca"

    )

    st.dataframe(

        brand_analysis_df,

        use_container_width=True

    )

    # ==================================================
    # PERFORMANCE STATUS
    # ==================================================

    if market_share_brand >= 30:

        render_success_alert(

            "🏆 Marca con liderazgo sólido en market share."

        )