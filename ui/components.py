"""
Reusable UI Components
"""

import streamlit as st


# ==========================================================
# Section Header
# ==========================================================

def section(title: str):

    st.markdown(
        f"""
        <div class="section-title">
            <span class="dot"></span>
            {title}
        </div>
        """,
        unsafe_allow_html=True,
    )


# ==========================================================
# KPI Card
# ==========================================================

def kpi_card(
    label: str,
    value,
    delta: str = "",
    delta_up: bool = True,
):

    delta_class = (
        "kpi-delta-up"
        if delta_up
        else "kpi-delta-down"
    )

    delta_html = (
        f"<div class='{delta_class}'>{delta}</div>"
        if delta
        else ""
    )

    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-label">{label}</div>
            <div class="kpi-value">{value}</div>
            {delta_html}
        </div>
        """,
        unsafe_allow_html=True,
    )


# ==========================================================
# Status Pill
# ==========================================================

def pill(
    text: str,
    kind: str = "info",
):
    """
    Render colored status pill.
    """

    colors = {

        "success": "#16A34A",

        "warning": "#D97706",

        "danger": "#DC2626",

        "info": "#2563EB",

    }

    color = colors.get(

        kind,

        colors["info"],

    )

    return (

        f"""

        <span
            style="
                background:{color};
                color:white;
                padding:4px 10px;
                border-radius:15px;
                font-size:12px;
                font-weight:600;
            ">

            {text}

        </span>

        """

    )


# ==========================================================
# Divider
# ==========================================================

def divider():

    st.markdown("---")


# ==========================================================
# Empty State
# ==========================================================

def empty_state(
    message: str,
):

    st.info(message)


# ==========================================================
# Success Banner
# ==========================================================

def success(
    message: str,
):

    st.success(message)


# ==========================================================
# Warning Banner
# ==========================================================

def warning(
    message: str,
):

    st.warning(message)


# ==========================================================
# Error Banner
# ==========================================================

def error(
    message: str,
):

    st.error(message)


# ==========================================================
# About
# ==========================================================

def render_about():

    section(

        "About CrisisOps AI"

    )

    st.markdown(

        """

### CrisisOps AI

CrisisOps AI is an enterprise-grade Supply Chain
Intelligence platform powered by AI Agents.

### Core Features

- Multi-Agent AI Architecture
- LangGraph Workflow
- Digital Twin Simulation
- Demand Forecasting
- Shipment Delay Prediction
- Supplier Risk Assessment
- Inventory Optimization
- Executive Dashboard
- Interactive Analytics

### Technology Stack

- Python
- Streamlit
- LangGraph
- Ollama
- Plotly
- PyDeck
- Pandas

### Version

2.0

""",

    )