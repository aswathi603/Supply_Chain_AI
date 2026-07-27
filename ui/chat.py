"""
Chat Interface
"""

from datetime import datetime

import streamlit as st

from graph.workflow import run_workflow
from memory.memory_manager import memory
from ui.components import section


# ==========================================================
# Prompt Categories
# ==========================================================

PROMPT_GROUPS = {

    "📊 Reporting": [

        "Give me an executive summary.",
        "Summarize today's supply chain performance.",
        "Show all critical KPIs.",
        "Generate a business health report.",
        "What are the biggest operational risks today?",

    ],

    "🚚 Shipment": [

        "Which shipments are delayed?",
        "Show all shipments at customs.",
        "Which shipments are at high risk?",
        "List premium shipments currently in transit.",
        "Show the ETA for all delayed shipments.",
        "Find shipments delayed by more than 3 days.",
        "Which shipment has the highest value at risk?",
        "Show cancelled shipments.",

    ],

    "📦 Inventory": [

        "Show inventory at risk.",
        "Which products are below reorder level?",
        "Which SKU has the highest stockout risk?",
        "Recommend inventory redistribution.",
        "Which warehouse has the lowest inventory?",
        "Show products with less than 7 days of supply.",

    ],

    "🏭 Supplier": [

        "Recommend alternate suppliers.",
        "Show high-risk suppliers.",
        "Rank suppliers by reliability.",
        "Find alternate suppliers for Electronics.",
        "Which supplier has the shortest lead time?",
        "Show supplier performance.",

    ],

    "⚠️ Incidents": [

        "Show all open incidents.",
        "List critical incidents.",
        "What incidents are affecting shipments?",
        "Summarize current disruptions.",
        "Which incident has the highest financial impact?",

    ],

    "🔄 Recovery": [

        "Suggest a recovery plan for delayed shipments.",
        "Recommend mitigation for customs delays.",
        "Suggest actions to reduce business risk.",
        "How can we reduce shipment delays?",

    ],

    "📈 Forecasting": [

        "Forecast shipment delays.",
        "Predict next month's demand.",
        "Forecast warehouse utilization.",
        "Predict inventory shortages.",
        "Estimate transportation cost next month.",
        "Show business impact forecast.",

    ],

    "🛰️ Digital Twin": [

        "Simulate shipment rerouting.",
        "Simulate replacing a supplier.",
        "Run a demand spike simulation.",
        "Compare Air vs Ocean transportation.",
        "Simulate warehouse capacity balancing.",
        "Run an inventory redistribution simulation.",

    ],
}


# ==========================================================
# Chat Page
# ==========================================================

def render_chat():

    section("💬 CrisisOps AI Assistant")

    st.caption(
        "Ask questions about shipments, suppliers, inventory, forecasting, or digital twin simulations."
    )

    st.write("")

    st.subheader("Quick Actions")

    for category, prompts in PROMPT_GROUPS.items():

        with st.container(border=True):

            st.markdown(f"### {category}")

            cols = st.columns(2)

            for i, prompt in enumerate(prompts):

                with cols[i % 2]:

                    if st.button(
                        prompt,
                        key=f"{category}_{i}",
                        use_container_width=True,
                    ):
                        process_query(prompt)

            st.write("")

    st.divider()

    render_history()

    query = st.chat_input(
        "Ask anything about your supply chain..."
    )

    if query:
        process_query(query)

    st.write("")

    c1, c2 = st.columns([1, 5])

    with c1:

        if st.button(
            "🗑 Clear",
            use_container_width=True,
        ):

            memory.clear()

            st.rerun()


# ==========================================================
# Conversation History
# ==========================================================

def render_history():

    history = memory.history()

    if not history:
        return

    st.subheader("Conversation")

    for message in history:

        if message["role"] == "user":

            with st.chat_message("user"):

                st.write(message["content"])

        elif message["role"] == "assistant":

            with st.chat_message("assistant"):

                st.caption(
                    f"🤖 {message.get('agent', 'Supervisor')}"
                )

                st.write(message["content"])

                if message.get("time"):

                    st.caption(
                        f"🕒 {message['time']}"
                    )


# ==========================================================
# Query Processing
# ==========================================================

def process_query(query: str):

    with st.spinner("Analyzing supply chain..."):

        try:

            # Base Agent stores the conversation.
            run_workflow(query)

        except Exception as ex:

            memory.add(

                role="assistant",

                content=(
                    "An unexpected error occurred.\n\n"
                    f"{type(ex).__name__}: {ex}"
                ),

                agent="System",

                time=datetime.now().strftime("%H:%M:%S"),

            )

    st.rerun()