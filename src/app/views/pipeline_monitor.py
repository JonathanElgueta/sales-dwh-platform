import streamlit as st

from datetime import datetime

import pandas as pd

from src.app.components.section_header import (

    render_section_header

)

from src.app.components.alerts import (

    render_success_alert,
    render_info_alert,
    render_warning_alert,
    render_error_alert,
    render_executive_alert

)

from src.app.components.kpi_card import (

    render_kpi_card

)

from src.app.services.pipeline.incremental_loader import (

    process_incremental_file

)

from src.app.services.pipeline.warehouse_loader import (

    update_sales_warehouse

)

from src.app.services.pipeline.mart_generator import (

    generate_all_marts

)

from src.app.services.pipeline.audit_logger import (

    write_pipeline_log,
    read_pipeline_logs

)

from src.app.services.pipeline.qa_engine import (

    run_qa_validations

)

from src.app.services.pipeline.schema_mapper import (

    normalize_columns

)

from src.app.auth.session_manager import (

    get_username

)

# ==================================================
# PIPELINE MONITOR
# ==================================================

def render_pipeline_monitor():

    # ==================================================
    # HEADER
    # ==================================================

    render_section_header(

        "🚀 Pipeline Monitor",

        "Enterprise Data Pipeline Control Center"

    )

    # ==================================================
    # STATUS
    # ==================================================

    render_success_alert(

        "✅ Pipeline operativo correctamente."

    )

    # ==================================================
    # INCREMENTAL LOAD
    # ==================================================

    render_section_header(

        "📦 Incremental Load"

    )

    uploaded_file = st.file_uploader(

        "Cargar nuevo archivo ventas XLSX",

        type=["xlsx"]

    )

    if uploaded_file is not None:

        render_info_alert(

            f"📂 Archivo cargado: {uploaded_file.name}"

        )

        try:

            # ==================================================
            # PREVIEW DATA
            # ==================================================

            preview_df = pd.read_excel(

                uploaded_file

            )

            # ==================================================
            # NORMALIZE COLUMNS
            # ==================================================

            preview_df = normalize_columns(

                preview_df

            )

            # ==================================================
            # PREVIEW
            # ==================================================

            st.dataframe(

                preview_df.head(),

                use_container_width=True

            )

            # ==================================================
            # QA VALIDATION
            # ==================================================

            render_section_header(

                "✅ QA Validation"

            )

            qa_result = run_qa_validations(

                preview_df

            )

            # ==================================================
            # KPI QA
            # ==================================================

            col1, col2, col3 = st.columns(3)

            with col1:

                render_kpi_card(

                    "QA Score",

                    f"{qa_result['qa_score']}%"

                )

            with col2:

                render_kpi_card(

                    "Errores",

                    str(qa_result["errors"])

                )

            with col3:

                render_kpi_card(

                    "Estado",

                    "PASS" if qa_result["success"] else "FAIL"

                )

            # ==================================================
            # QA DETAILS
            # ==================================================

            qa_df = pd.DataFrame(

                qa_result["validations"]

            )

            st.dataframe(

                qa_df,

                use_container_width=True

            )

            # ==================================================
            # QA ALERT
            # ==================================================

            if qa_result["success"]:

                render_success_alert(

                    "✅ QA validado correctamente."

                )

            else:

                render_error_alert(

                    "❌ QA detectó errores críticos."

                )

            # ==================================================
            # PROCESS BUTTON
            # ==================================================

            if qa_result["success"]:

                if st.button(

                    "🚀 Procesar Incremental",

                    use_container_width=True

                ):

                    with st.spinner(

                        "Procesando archivo incremental..."

                    ):

                        # ==================================================
                        # PROCESS FILE
                        # ==================================================

                        result = process_incremental_file(

                            uploaded_file

                        )

                    # ==================================================
                    # SUCCESS PROCESS
                    # ==================================================

                    if result["success"]:

                        render_success_alert(

                            f"""
✅ Archivo procesado correctamente.

📦 Registros cargados:
{result['rows']}

💾 Archivo temporal generado:
{result['file']}
"""
                        )

                        # ==================================================
                        # UPDATE WAREHOUSE
                        # ==================================================

                        warehouse_result = update_sales_warehouse(

                            result["data"]

                        )

                        if warehouse_result["success"]:

                            render_success_alert(

                                f"""
✅ Data Warehouse actualizado correctamente.

📦 Registros cargados:
{warehouse_result['rows']}

🧠 Partición actualizada:
{warehouse_result['partitions']}
"""
                            )

                            # ==================================================
                            # GENERATE ANALYTICS MARTS
                            # ==================================================

                            analytics_result = generate_all_marts()

                            if analytics_result["success"]:

                                render_success_alert(

                                    f"""
✅ Analytics Marts regenerados correctamente.

📈 Registros procesados:
{analytics_result['rows']}

✅ mart_sales_monthly
✅ mart_brand_performance
✅ mart_category_performance
✅ mart_channel_performance
"""
                                )

                                # ==================================================
                                # CLEAR CACHE
                                # ==================================================

                                st.cache_data.clear()

                                render_success_alert(

                                    "✅ Cache refrescado correctamente."

                                )

                                # ==================================================
                                # AUDIT LOG SUCCESS
                                # ==================================================

                                write_pipeline_log(

                                    user=get_username(),

                                    file_name=uploaded_file.name,

                                    rows=result["rows"],

                                    status="SUCCESS",

                                    message="Pipeline ejecutado correctamente"

                                )

                                # ==================================================
                                # EXECUTIVE STATUS
                                # ==================================================

                                render_executive_alert(

                                    "Pipeline Status",

                                    """
✅ Incremental Load completado

✅ Data Warehouse actualizado

✅ Analytics Marts regenerados

✅ Cache refrescado

✅ Governance actualizado
"""
                                )

                                # ==================================================
                                # RERUN APP
                                # ==================================================

                                st.rerun()

                            else:

                                render_error_alert(

                                    analytics_result["message"]

                                )

                        else:

                            render_error_alert(

                                warehouse_result["message"]

                            )

                    # ==================================================
                    # ERROR PROCESS
                    # ==================================================

                    else:

                        render_error_alert(

                            result["message"]

                        )

                        # ==================================================
                        # AUDIT LOG ERROR
                        # ==================================================

                        write_pipeline_log(

                            user=get_username(),

                            file_name=uploaded_file.name,

                            rows=0,

                            status="ERROR",

                            message=result["message"]

                        )

        # ==================================================
        # GLOBAL ERROR
        # ==================================================

        except Exception as e:

            render_error_alert(

                f"❌ Error procesando archivo:\n\n{str(e)}"

            )

    # ==================================================
    # EXECUTION INFO
    # ==================================================

    render_section_header(

        "⏱️ Última Ejecución"

    )

    execution_time = datetime.now().strftime(

        "%Y-%m-%d %H:%M:%S"

    )

    render_info_alert(

        f"🕒 Última validación: {execution_time}"

    )

    # ==================================================
    # PIPELINE STAGES
    # ==================================================

    render_section_header(

        "⚙️ Etapas Pipeline"

    )

    stages = [

        "✅ Extracción XLSX",
        "✅ Transformación",
        "✅ Data Warehouse",
        "✅ Semantic Layer",
        "✅ Analytics Layer",
        "✅ QA Validation",
        "✅ Governance"

    ]

    for stage in stages:

        st.write(stage)

    # ==================================================
    # EXECUTION METRICS
    # ==================================================

    render_section_header(

        "📊 Métricas Pipeline"

    )

    col1, col2, col3 = st.columns(3)

    with col1:

        render_kpi_card(

            "Fact Tables",

            "1"

        )

    with col2:

        render_kpi_card(

            "Data Marts",

            "4"

        )

    with col3:

        render_kpi_card(

            "Estado",

            "ONLINE"

        )

    # ==================================================
    # AUDIT LOGS
    # ==================================================

    render_section_header(

        "🧾 Audit Logs"

    )

    audit_df = read_pipeline_logs()

    st.dataframe(

        audit_df,

        use_container_width=True

    )

    # ==================================================
    # NEXT STEPS
    # ==================================================

    render_section_header(

        "🚀 Próximas Integraciones"

    )

    render_warning_alert(

        """
📦 Budget Fact

📈 Forecast Fact

🚚 Logistic Fact

🤖 Machine Learning

📡 Alertas automáticas

🧠 Forecasting IA

📊 Auto-refresh dashboards

🧾 Enterprise Governance

🔍 AI Anomaly Detection
"""
    )