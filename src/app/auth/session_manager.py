import streamlit as st


# ==================================================
# INIT SESSION
# ==================================================

def init_session():

    if "authenticated" not in st.session_state:

        st.session_state.authenticated = False

    if "username" not in st.session_state:

        st.session_state.username = None

    if "role" not in st.session_state:

        st.session_state.role = None


# ==================================================
# LOGIN USER
# ==================================================

def login_user(username, role):

    st.session_state.authenticated = True

    st.session_state.username = username

    st.session_state.role = role


# ==================================================
# LOGOUT USER
# ==================================================

def logout_user():

    st.session_state.authenticated = False

    st.session_state.username = None

    st.session_state.role = None


# ==================================================
# VALIDATE SESSION
# ==================================================

def is_authenticated():

    return st.session_state.authenticated


# ==================================================
# GET USERNAME
# ==================================================

def get_username():

    return st.session_state.username


# ==================================================
# GET ROLE
# ==================================================

def get_role():

    return st.session_state.role