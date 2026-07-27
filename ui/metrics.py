"""
Forecasting Dashboard
"""

import pandas as pd
import plotly.express as px
import streamlit as st

from api.mock_loader import api_get_df

from forecasting.business_impact import business_impact
from forecasting.delay_prediction import predict_delays
from forecasting.demand_forecasting import forecast_next_weeks
from forecasting.warehouse_utilization import utilization_projection

from ui.components import section, kpi_card

from utils.helpers import money
from utils.visualization import styled


def render_forecasting():

    section("📈 Forecasting & Predictive Analytics")

    impact = business_impact()

    c1, c2, c3 = st.columns(3)

    with c1:
        kpi_card(
            "Revenue at Risk",
            money(impact["revenue_at_risk_usd"]),
        )

    with c2:
        kpi_card(
            "Shipment Value at Risk",
            money(impact["shipment_value_at_risk_usd"]),
        )

    with c3:
        kpi_card(
            "Incident Impact",
            money(impact["incident_impact_usd"]),
        )

    st.write("")

    # ======================================================
    # Demand Forecast
    # ======================================================

    section("Demand Forecast")

    demand = api_get_df("demand")

    if not demand.empty:

        fig = px.line(

            demand,

            x="week",

            y=[
                "actual_units",
                "forecast_units",
            ],

            markers=True,

            color_discrete_sequence=[
                "#38BDF8",
                "#EF4444",
            ],

        )

        st.plotly_chart(
            styled(fig),
            use_container_width=True,
        )

    # ======================================================
    # Shipment Delay Prediction
    # ======================================================

    section("Shipment Delay Prediction")

    prediction = predict_delays()

    delays = pd.DataFrame(
        prediction["predictions"]
    )

    # Clean status values
    delays["status"] = (
        delays["status"]
        .astype(str)
        .str.strip()
        .str.title()
    )

    if not delays.empty:

        fig = px.bar(

            delays,

            x="id",

            y="delay_risk",

            color="status",

            hover_data=[
                "product",
                "mode",
            ],

            text="delay_risk",

            title="Shipment Delay Risk",

            color_discrete_map={

                "In Transit": "#7DBCF3",   # Light Blue

                "Delayed": "#1565C0",      # Blue

                "At Customs": "#F8A5A8",   # Pink

                "Delivered": "#22C55E",    # Green ✅

                "Cancelled": "#EF4444",    # Red ✅

            },

            category_orders={
                "status": [
                    "In Transit",
                    "Delayed",
                    "At Customs",
                    "Delivered",
                    "Cancelled",
                ]
            },

        )

        fig.update_traces(
            textposition="outside",
        )

        st.plotly_chart(
            styled(fig),
            use_container_width=True,
        )

    else:

        st.info(
            "No shipment predictions available."
        )

    # ======================================================
    # Warehouse Utilization Projection
    # ======================================================

    section("Warehouse Utilization Projection")

    projection = utilization_projection(
        growth_pct=8.0
    )

    warehouse = pd.DataFrame(
        projection["forecast"]
    )

    if not warehouse.empty:

        fig = px.bar(

            warehouse,

            x="name",

            y="projected_utilization",

            color="projected_utilization",

            text="projected_utilization",

            color_continuous_scale=[
                "#22C55E",
                "#F59E0B",
                "#EF4444",
            ],

            title="Projected Warehouse Utilization",

        )

        st.plotly_chart(
            styled(fig),
            use_container_width=True,
        )

    else:

        st.info(
            "No warehouse forecast available."
        )

    # ======================================================
    # Six Week Demand Projection
    # ======================================================

    section("Six Week Demand Projection")

    forecast_result = forecast_next_weeks(6)

    forecast = pd.DataFrame(
        forecast_result["forecast"]
    )

    if not forecast.empty:

        fig = px.line(

            forecast,

            x="week_offset",

            y="forecast_units",

            color="product",

            markers=True,

            title="6 Week Forecast",

        )

        st.plotly_chart(
            styled(fig),
            use_container_width=True,
        )

    else:

        st.info(
            "No forecast available."
        )

    # ======================================================
    # Summary
    # ======================================================

    st.write("")

    section("Forecast Summary")

    st.markdown(
        """
### Key Insights

- Demand is projected using historical trends.
- Delay prediction identifies shipments requiring proactive attention.
- Warehouse utilization forecasts capacity pressure.
- Revenue at risk combines order value and disruption impact.

### Recommended Actions

- Monitor high-risk shipments daily.
- Increase inventory for products with growing demand.
- Balance warehouse utilization before reaching capacity.
- Prepare alternate transportation routes for critical shipments.
"""
    )