import streamlit as st

import plotly.express as px

from src.app.components.section_header import (

    render_section_header

)

from src.app.components.alerts import (

    render_warning_alert,
    render_success_alert,
    render_executive_alert

)

from src.app.components.kpi_card import (

    render_kpi_card

)

from src.app.services.ml.anomaly_detection import (

    detect_sales_anomalies

)

from src.app.styles.theme import (

    CHART_THEME

)

# ==================================================
# ANOMALY DASHBOARD
# ==================================================

def render_anomaly_dashboard(

    filtered_sales_df

):

    # ==================================================
    # HEADER
    # ==================================================

    render_section_header(

        "🤖 AI Anomaly Detection",

        "Enterprise AI Monitoring"

    )

    # ==================================================
    # DETECT ANOMALIES
    # ==================================================

    anomaly_df = detect_sales_anomalies(

        filtered_sales_df

    )

    # ==================================================
    # KPI METRICS
    # ==================================================

    total_anomalies = len(

        anomaly_df[
            anomaly_df["anomaly_label"]
            ==
            "Anomalía"
        ]

    )

    total_records = len(anomaly_df)

    anomaly_pct = round(

        (
            total_anomalies
            /
            total_records
        ) * 100,

        2

    )

    col1, col2, col3 = st.columns(3)

    with col1:

        render_kpi_card(

            "Registros",

            f"{total_records}"

        )

    with col2:

        render_kpi_card(

            "Anomalías",

            f"{total_anomalies}"

        )

    with col3:

        render_kpi_card(

            "% Riesgo",

            f"{anomaly_pct}%"

        )

    # ==================================================
    # ANOMALY CHART
    # ==================================================

    render_section_header(

        "📈 Detección Anomalías"

    )

    fig = px.scatter(

        anomaly_df,

        x="periodo",

        y="venta_total",

        color="anomaly_label",

        title="AI Anomaly Detection"

    )

    fig.update_layout(

        **CHART_THEME

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

    # ==================================================
    # ALERTS
    # ==================================================

    render_section_header(

        "🚨 AI Alerts"

    )

    if total_anomalies == 0:

        render_success_alert(

            "✅ No se detectaron anomalías."

        )

    else:

        render_warning_alert(

            f"""

🚨 Se detectaron:

{total_anomalies} anomalías.

📡 Revisar comportamiento comercial.

"""

        )

    # ==================================================
    # ANOMALY TABLE
    # ==================================================

    render_section_header(

        "📋 Detalle Anomalías"

    )

    anomalies_only = anomaly_df[

        anomaly_df["anomaly_label"]
        ==
        "Anomalía"

    ]

    st.dataframe(

        anomalies_only,

        use_container_width=True

    )

    # ==================================================
    # AI INSIGHTS
    # ==================================================

    render_section_header(

        "🧠 AI Insights"

    )

    render_executive_alert(

        "Machine Learning Detection",

        f"""

🤖 Modelo IA ejecutado correctamente.

📊 Registros analizados:
{total_records}

🚨 Anomalías detectadas:
{total_anomalies}

📈 Riesgo operacional:
{anomaly_pct}%

"""

    )