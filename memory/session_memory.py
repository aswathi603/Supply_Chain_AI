"""
Session Manager
"""

import streamlit as st


def get(
    key,
    default=None,
):

    return st.session_state.get(

        key,

        default,

    )


def set_(
    key,
    value,
):

    st.session_state[key] = value


def exists(
    key,
):

    return key in st.session_state


def delete(
    key,
):

    if key in st.session_state:

        del st.session_state[key]