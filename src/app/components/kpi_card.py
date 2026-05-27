import streamlit as st

# ==================================================
# KPI CARD COMPONENT
# ==================================================

def render_kpi_card(

    title,
    value,
    delta=None

):

    delta_html = ""

    if delta:

        delta_html = (
            f"<div style='"
            f"color:#94A3B8;"
            f"margin-top:12px;"
            f"font-size:16px;"
            f"font-weight:600;"
            f"'>"
            f"{delta}"
            f"</div>"
        )

    html = (
        f"<div style='"
        f"background:#111827;"
        f"padding:28px;"
        f"border-radius:18px;"
        f"border:1px solid #334155;"
        f"box-shadow:0px 10px 30px rgba(0,0,0,0.35);"
        f"min-height:180px;"
        f"'>"

        f"<div style='"
        f"color:#94A3B8;"
        f"font-size:15px;"
        f"font-weight:600;"
        f"margin-bottom:14px;"
        f"text-transform:uppercase;"
        f"letter-spacing:1px;"
        f"'>"
        f"{title}"
        f"</div>"

        f"<div style='"
        f"color:white;"
        f"font-size:40px;"
        f"font-weight:800;"
        f"line-height:1.1;"
        f"'>"
        f"{value}"
        f"</div>"

        f"{delta_html}"

        f"</div>"
    )

    st.markdown(

        html,

        unsafe_allow_html=True

    )