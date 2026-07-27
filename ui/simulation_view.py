"""
Digital Twin Simulation View
"""
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import streamlit as st

from services.digital_twin_service import (
    SCENARIOS,
    run_scenario,
)

from ui.components import (
    kpi_card,
    section,
)

from utils.helpers import money


def render_simulations():

    section("🧪 Digital Twin Simulations")

    scenario = st.selectbox(

        "Choose Simulation",

        list(SCENARIOS.keys()),

    )

    params = {}

    if scenario == "Shipment Rerouting":

        params["shipment_id"] = st.text_input(

            "Shipment ID",

            "",

        )

        params["new_mode"] = st.selectbox(

            "Transport Mode",

            [

                "Air",

                "Road",

                "Rail",

                "Ocean",

            ],

        )

    elif scenario == "Supplier Replacement":

        params["supplier_id"] = st.text_input(

            "Supplier ID",

            "SUP-1001",

        )

        params["category"] = st.text_input(

            "Category (Optional)",

            "",

        )

    elif scenario == "Demand Spike":

        params["product"] = st.text_input(

            "Product",

            "Semiconductors",

        )

        params["spike_pct"] = st.slider(

            "Demand Increase (%)",

            10,

            100,

            40,

        )

    elif scenario == "Warehouse Capacity":

        params["target_util"] = st.slider(

            "Target Utilization",

            0.50,

            0.95,

            0.75,

        )

    elif scenario == "Inventory Redistribution":

        params["sku"] = st.text_input(

            "SKU",

            "SKU-EL-001",

        )

    elif scenario == "Customs Delay":

        params["location"] = st.text_input(

            "Location",

            "Singapore Customs",

        )

        params["extra_days"] = st.slider(

            "Extra Delay",

            1,

            14,

            3,

        )

    elif scenario == "Transportation Comparison":

        params["distance_km"] = st.slider(

            "Distance (km)",

            500,

            20000,

            10000,

            step=500,

        )

    if st.button(

        "▶ Run Simulation",

        type="primary",

        use_container_width=True,

    ):

        params = {

            k: v

            for k, v in params.items()

            if v not in ("", None)

        }

        st.session_state["simulation"] = run_scenario(

            scenario,

            **params,

        )

    if "simulation" in st.session_state:

        render_result(

            st.session_state["simulation"]

        )


def render_result(result: dict):

    st.divider()

    section("📊 Simulation Result")

    st.success(
        result.get(
            "summary",
            "Simulation Completed",
        )
    )

    confidence = result.get("confidence", 0)

    st.progress(confidence)

    st.caption(f"Confidence : {confidence:.0%}")

    st.write("")

    # =====================================================
    # BEFORE / AFTER (Shipment Rerouting Only)
    # =====================================================

    if result.get("before") and result.get("after"):

        before = result["before"]
        after = result["after"]
        delta = result.get("delta", {})

        st.subheader("Before vs After")

        c1, c2, c3 = st.columns(3)

        with c1:
            st.metric(
                "ETA",
                f'{after.get("eta_days", 0)} Days',
                delta=f'-{delta.get("time_saved_days", 0)} Days',
            )

        with c2:
            st.metric(
                "Logistics Cost",
                money(after.get("logistics_cost_usd", 0)),
                delta=money(delta.get("extra_cost_usd", 0)),
            )

        with c3:
            st.metric(
                "Service Level",
                f'+{delta.get("service_level_uplift_pct", 0)}%',
            )

        comparison = pd.DataFrame({

            "Metric": [
                "Transport Mode",
                "ETA (Days)",
                "Logistics Cost",
            ],

            "Before": [
                before.get("mode", "-"),
                before.get("eta_days", "-"),
                money(before.get("logistics_cost_usd", 0)),
            ],

            "After": [
                after.get("mode", "-"),
                after.get("eta_days", "-"),
                money(after.get("logistics_cost_usd", 0)),
            ],

        })

        st.dataframe(
            comparison,
            use_container_width=True,
            hide_index=True,
        )

        # ==========================================
        # ETA Comparison
        # ==========================================

        st.subheader("📅 ETA Comparison")

        eta_df = pd.DataFrame({

            "Scenario": [
                "Before",
                "After",
            ],

            "ETA Days": [
                before.get("eta_days", 0),
                after.get("eta_days", 0),
            ],

        })

        eta_fig = px.bar(

            eta_df,

            x="Scenario",

            y="ETA Days",

            color="Scenario",

            text="ETA Days",

            color_discrete_sequence=[
                "#3B82F6",
                "#10B981",
            ],

        )

        eta_fig.update_layout(

            template="plotly_dark",

            height=380,

            title="Estimated Transit Time",

            showlegend=False,

        )

        eta_fig.update_traces(
            textposition="outside"
        )

        st.plotly_chart(
            eta_fig,
            use_container_width=True,
        )

        # ==========================================
        # Logistics Cost Comparison
        # ==========================================

        st.subheader("💰 Logistics Cost Comparison")

        cost_df = pd.DataFrame({

            "Scenario": [
                "Before",
                "After",
            ],

            "Cost": [
                before.get("logistics_cost_usd", 0),
                after.get("logistics_cost_usd", 0),
            ],

        })

        cost_fig = px.bar(

            cost_df,

            x="Scenario",

            y="Cost",

            color="Scenario",

            text="Cost",

            color_discrete_sequence=[
                "#3B82F6",
                "#EF4444",
            ],

        )

        cost_fig.update_traces(

            texttemplate="$%{text:,.0f}",

            textposition="outside",

        )

        cost_fig.update_layout(

            template="plotly_dark",

            height=380,

            title="Logistics Cost",

            showlegend=False,

        )

        st.plotly_chart(
            cost_fig,
            use_container_width=True,
        )

    # =====================================================
    # IMPACT
    # =====================================================

    if result.get("impact"):

        section("Business Impact")

        impact = result["impact"]

        if isinstance(impact, dict):

            for key, value in impact.items():

                if isinstance(value, list):

                    st.subheader(
                        key.replace(
                            "_",
                            " ",
                        ).title()
                    )

                    if value:

                        st.dataframe(
                            pd.DataFrame(value),
                            use_container_width=True,
                            hide_index=True,
                        )

                else:

                    if isinstance(value, (int, float)):

                        if "usd" in key.lower():

                            st.metric(
                                key.replace(
                                    "_",
                                    " ",
                                ).title(),
                                money(value),
                            )

                        else:

                            st.metric(
                                key.replace(
                                    "_",
                                    " ",
                                ).title(),
                                value,
                            )

                    else:

                        st.write(
                            f"**{key.replace('_',' ').title()}** : {value}"
                        )

    # =====================================================
    # TABLES
    # =====================================================

    for table in [

        "affected",

        "candidates",

        "plan",

        "queue",

        "table",

        "over_capacity",

        "under_capacity",

    ]:

        if result.get(table):

            section(
                table.replace(
                    "_",
                    " ",
                ).title()
            )

            st.dataframe(

                pd.DataFrame(result[table]),

                hide_index=True,

                use_container_width=True,

            )

    # =====================================================
    # RECOMMENDATION
    # =====================================================

    if result.get("recommendation"):

        section("Recommendation")

        st.success(result["recommendation"])