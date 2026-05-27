import streamlit as st

from auth.auth_service import (

    validate_login

)

from auth.session_manager import (

    login_user

)


# ==================================================
# LOGIN PAGE
# ==================================================

def render_login():

    st.markdown(

        """
        # 🔐 SALES DWH PLATFORM

        ### Enterprise Analytics Platform
        """
    )

    st.markdown("---")

    username = st.text_input(

        "Usuario"

    )

    password = st.text_input(

        "Password",

        type="password"

    )

    login_button = st.button(

        "Iniciar Sesión",

        use_container_width=True

    )

    if login_button:

        result = validate_login(

            username,
            password

        )

        if result["authenticated"]:

            login_user(

                username,
                result["role"]

            )

            st.success(

                "Login exitoso"
            )

            st.rerun()

        else:

            st.error(

                "Usuario o password incorrectos"
            )