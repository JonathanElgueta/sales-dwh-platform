import streamlit as st

# ==================================================
# SECTION HEADER
# ==================================================

def render_section_header(

    title,
    subtitle=None

):

    html = (
        f"<div style='margin-bottom:30px;'>"

        f"<h1 style='"
        f"color:white;"
        f"font-size:42px;"
        f"font-weight:800;"
        f"margin-bottom:5px;"
        f"'>"
        f"{title}"
        f"</h1>"
    )

    if subtitle:

        html += (
            f"<div style='"
            f"color:#94A3B8;"
            f"font-size:18px;"
            f"'>"
            f"{subtitle}"
            f"</div>"
        )

    html += "</div>"

    st.markdown(

        html,

        unsafe_allow_html=True

    )