import streamlit as st
from datetime import datetime

# ==================================================
# PIPELINE MONITOR
# ==================================================

def render_pipeline_monitor():

    # ==================================================
    # TITLE
    # ==================================================

    st.title(
        "🚀 Pipeline Monitor"
    )

    st.markdown("---")

    # ==================================================
    # STATUS
    # ==================================================

    st.subheader(
        "📡 Estado Pipeline"
    )

    st.success(
        "✅ Pipeline operativo correctamente."
    )

    # ==================================================
    # EXECUTION INFO
    # ==================================================

    st.markdown("---")

    st.subheader(
        "⏱️ Última Ejecución"
    )

    execution_time = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    st.info(

        f"""
🕒 Última validación:

{execution_time}
"""

    )

    # ==================================================
    # PIPELINE STAGES
    # ==================================================

    st.markdown("---")

    st.subheader(
        "⚙️ Etapas Pipeline"
    )

    stages = [

        "✅ Extracción XLSX",
        "✅ Transformación",
        "✅ Data Warehouse",
        "✅ Semantic Layer",
        "✅ Data Marts",
        "✅ Analytics Layer"

    ]

    for stage in stages:

        st.write(stage)

    # ==================================================
    # EXECUTION METRICS
    # ==================================================

    st.markdown("---")

    st.subheader(
        "📊 Métricas Pipeline"
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Tablas Fact",
            "1"
        )

    with col2:

        st.metric(
            "Data Marts",
            "5"
        )

    with col3:

        st.metric(
            "Estado",
            "ONLINE"
        )

    # ==================================================
    # NEXT STEPS
    # ==================================================

    st.markdown("---")

    st.subheader(
        "🚀 Próximas Integraciones"
    )

    st.warning(

        """
📦 Budget Fact

📈 Forecast Fact

🚚 Logistic Fact

🤖 Machine Learning

📡 Alertas automáticas
"""

    )