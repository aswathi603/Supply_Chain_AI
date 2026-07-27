"""
Application Sidebar
"""

import streamlit as st

from config.settings import (
    APP_NAME,
    APP_TAGLINE,
    LLM_PROVIDER,
    OLLAMA_MODEL,
    HAS_LLM,
)


def render_sidebar() -> str:
    """
    Render the application sidebar.
    """

    with st.sidebar:

        st.title("🛰️ " + APP_NAME)

        st.caption(APP_TAGLINE)

        st.markdown("---")

        page = st.radio(

            "Navigation",

            [

                "Dashboard",

                "Chat with Agents",

                "Digital Twin Simulations",

                "Forecasting",

                "About",

            ],

        )

        st.markdown("---")

        st.subheader("🤖 AI Status")

        if HAS_LLM:

            st.success("LLM Connected")

        else:

            st.error("LLM Offline")

        st.write(f"**Provider:** {LLM_PROVIDER}")

        if LLM_PROVIDER == "ollama":

            st.write(f"**Model:** {OLLAMA_MODEL}")

            st.info("Running locally using Ollama.")

        else:

            st.info("Using cloud LLM provider.")

        st.markdown("---")

        st.subheader("📊 Project")

        st.write("Multi-Agent System")

        st.write("Digital Twin")

        st.write("Forecasting")

        st.write("Risk Assessment")

        st.write("Recovery Planning")

        st.markdown("---")

        st.caption("Version 2.0")

    return page