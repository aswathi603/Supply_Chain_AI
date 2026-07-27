"""
Chat History Storage
"""

import streamlit as st


def _init():

    if "chat_history" not in st.session_state:

        st.session_state.chat_history = []


def add(
    role: str,
    content: str,
    agent=None,
    time=None,
):

    _init()

    st.session_state.chat_history.append(
        {
            "role": role,
            "content": content,
            "agent": agent,
            "time": time,
        }
    )


def history():

    _init()

    return st.session_state.chat_history


def last(limit: int = 10):

    _init()

    return st.session_state.chat_history[-limit:]


def clear():

    _init()

    st.session_state.chat_history = []