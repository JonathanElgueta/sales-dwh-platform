import streamlit as st

# ==================================================
# EXECUTIVE ALERT
# ==================================================

def render_executive_alert(

    title,
    message

):

    html = (
        f"<div style='"
        f"background:#0F1E3A;"
        f"border:1px solid #334155;"
        f"border-radius:16px;"
        f"padding:24px;"
        f"margin-top:20px;"
        f"margin-bottom:20px;"
        f"'>"

        f"<h2 style='"
        f"color:white;"
        f"margin-bottom:20px;"
        f"'>"
        f"{title}"
        f"</h2>"

        f"<div style='"
        f"color:#E2E8F0;"
        f"font-size:20px;"
        f"line-height:2;"
        f"'>"
        f"{message}"
        f"</div>"

        f"</div>"
    )

    st.markdown(

        html,

        unsafe_allow_html=True

    )

# ==================================================
# INFO ALERT
# ==================================================

def render_info_alert(message):

    st.info(message)

# ==================================================
# SUCCESS ALERT
# ==================================================

def render_success_alert(message):

    st.success(message)

# ==================================================
# WARNING ALERT
# ==================================================

def render_warning_alert(message):

    st.warning(message)

# ==================================================
# ERROR ALERT
# ==================================================

def render_error_alert(message):

    st.error(message)