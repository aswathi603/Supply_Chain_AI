"""
CrisisOps AI

Supply Chain Multi-Agent Intelligence Platform

Application Entry Point
"""

from pathlib import Path

import streamlit as st

from config.settings import (
    APP_NAME,
    APP_TAGLINE,
    APP_ICON,
)

from memory.memory_manager import memory

from ui.sidebar import render_sidebar

from ui.dashboard import render_dashboard

from ui.chat import render_chat

from ui.simulation_view import render_simulations

from ui.metrics import render_forecasting

from ui.components import render_about

from utils.logger import get_logger


logger = get_logger(__name__)


# ==========================================================
# Streamlit Configuration
# ==========================================================

st.set_page_config(

    page_title=APP_NAME,

    page_icon=APP_ICON,

    layout="wide",

    initial_sidebar_state="expanded",

)


# ==========================================================
# Load CSS
# ==========================================================

def load_css():

    css = (

        Path(__file__).parent

        / "assets"

        / "styles.css"

    )

    if css.exists():

        st.markdown(

            f"<style>{css.read_text()}</style>",

            unsafe_allow_html=True,

        )


# ==========================================================
# Initialize Session
# ==========================================================

def initialize():

    """
    Initialize application state.
    """

    memory.history()

    logger.info(

        "CrisisOps AI started."

    )


# ==========================================================
# Header
# ==========================================================

def render_header():

    st.markdown(

        f"""

<div class="app-header">

<div class="app-header-title">

{APP_ICON} {APP_NAME}

</div>

<div class="app-header-sub">

{APP_TAGLINE}

</div>

</div>

""",

        unsafe_allow_html=True,

    )


# ==========================================================
# Main
# ==========================================================

def main():

    load_css()

    initialize()

    render_header()

    page = render_sidebar()

    routes = {

        "Dashboard":

            render_dashboard,

        "Chat with Agents":

            render_chat,

        "Digital Twin Simulations":

            render_simulations,

        "Forecasting":

            render_forecasting,

    }

    try:

        routes.get(

            page,

            render_dashboard,

        )()

    except Exception as ex:

        logger.exception(ex)

        st.error(

            "An unexpected error occurred."

        )

        with st.expander(

            "Show Details"

        ):

            st.exception(ex)


# ==========================================================
# Run
# ==========================================================

if __name__ == "__main__":

    main()