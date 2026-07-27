"""
Executive Dashboard
"""

import streamlit as st
import pydeck as pdk
import plotly.express as px

from api.incident_api import incidents_df
from api.shipment_api import shipments_df
from api.supplier_api import suppliers_df
from api.warehouse_api import warehouses_df

from services.reporting_service import executive_brief

from ui.components import (
    section,
    kpi_card,
)

from utils.helpers import money

from utils.visualization import (
    styled,
    bar,
)


def render_dashboard():
    """
    Render the executive dashboard.
    """

    try:

        brief = executive_brief()

        ships = shipments_df()

        warehouses = warehouses_df()

        suppliers = suppliers_df()

        incidents = incidents_df()

    except Exception as ex:

        st.error(

            f"Unable to load dashboard data.\n\n{ex}"

        )

        return

    # ==========================================================
    # Executive Health
    # ==========================================================

    health = brief["overall_health"]

    if health == "Healthy":

        st.success(
            "🟢 Overall Supply Chain Health : Healthy"
        )

    elif health == "Warning":

        st.warning(
            "🟠 Overall Supply Chain Health : Warning"
        )

    else:

        st.error(
            "🔴 Overall Supply Chain Health : Critical"
        )

    # ==========================================================
    # KPI Cards
    # ==========================================================

    section("Executive KPIs")

    kpis = [

        (

            "Total Shipments",

            brief["shipments"]["total_shipments"],

            "",

            True,

        ),

        (

            "Delayed",

            brief["shipments"]["delayed"],

            "+1 vs Yesterday",

            False,

        ),

        (

            "Value at Risk",

            money(

                brief["shipments"]["value_at_risk_usd"]

            ),

            "",

            False,

        ),

        (

            "Open Incidents",

            brief["incidents"]["open"],

            f"{brief['incidents']['critical']} Critical",

            False,

        ),

        (

            "Revenue at Risk",

            money(

                brief["orders"]["revenue_at_risk_usd"]

            ),

            "",

            False,

        ),

    ]

    cols = st.columns(

        len(kpis)

    )

    for col, item in zip(

        cols,

        kpis,

    ):

        with col:

            kpi_card(

                item[0],

                str(item[1]),

                item[2],

                item[3],

            )

    st.write("")

    # ==========================================================
    # Global Supply Chain Network
    # ==========================================================

    section("🌍 Global Supply Chain Network")

    stat1, stat2, stat3 = st.columns(3)

    stat1.metric(

        "Suppliers",

        len(suppliers),

    )

    stat2.metric(

        "Warehouses",

        len(warehouses),

    )

    stat3.metric(

        "Active Shipments",

        len(

            ships[
                ships["status"] != "Delivered"
            ]
        ),

    )

    supplier_points = [

        {

            "lat": row["lat"],

            "lon": row["lon"],

            "name": row["name"],

            "kind": "Supplier",

        }

        for _, row in suppliers.iterrows()

    ]

    warehouse_points = [

        {

            "lat": row["lat"],

            "lon": row["lon"],

            "name": row["name"],

            "kind": "Warehouse",

        }

        for _, row in warehouses.iterrows()

    ]

    arcs = (

        ships[

            ships["status"].isin(

                [

                    "In Transit",

                    "Delayed",

                    "At Customs",

                ]

            )

        ]

        .apply(

            lambda row: {

                "from_lat": row["origin_lat"],

                "from_lon": row["origin_lon"],

                "to_lat": row["dest_lat"],

                "to_lon": row["dest_lon"],

                "color":

                    [239, 68, 68]

                    if row["status"] != "In Transit"

                    else [56, 189, 248],

            },

            axis=1,

        )

        .tolist()

    )

    scatter_layer = pdk.Layer(

        "ScatterplotLayer",

        data=supplier_points + warehouse_points,

        get_position="[lon, lat]",

        get_radius=90000,

        get_fill_color="[167,139,250,180]",

        pickable=True,

    )

    arc_layer = pdk.Layer(

        "ArcLayer",

        data=arcs,

        get_source_position="[from_lon, from_lat]",

        get_target_position="[to_lon, to_lat]",

        get_source_color="color",

        get_target_color="color",

        get_width=2,

    )

    view_state = pdk.ViewState(

        latitude=25,

        longitude=40,

        zoom=1.2,

        pitch=30,

    )

    st.pydeck_chart(

        pdk.Deck(

            layers=[

                scatter_layer,

                arc_layer,

            ],

            initial_view_state=view_state,

            map_style="mapbox://styles/mapbox/dark-v10",

            tooltip={

                "text": "{name}\n{kind}"

            },

        )

    )

    # ==========================================================
    # Shipment Mode & Incident Charts
    # ==========================================================

    st.write("")

    left, right = st.columns(2)

    with left:

        section("Shipments by Transportation Mode")

        if not ships.empty:

            mode_counts = (

                ships

                .groupby("mode")

                .size()

                .reset_index(name="count")

            )

            fig = bar(

                mode_counts,

                "mode",

                "count",

                color="mode",

            )

            st.plotly_chart(

                styled(fig),

                use_container_width=True,

            )

        else:

            st.info("No shipment data available.")

    with right:

        section("Incidents by Severity")

        if not incidents.empty:

            severity = (

                incidents

                .groupby("severity")

                .size()

                .reset_index(name="count")

            )

            fig = px.pie(

                severity,

                values="count",

                names="severity",

                hole=0.55,

            )

            st.plotly_chart(

                styled(fig),

                use_container_width=True,

            )

        else:

            st.info("No incidents available.")

    # ==========================================================
    # Warehouse Utilization
    # ==========================================================

    st.write("")

    section("Warehouse Utilization")

    if not warehouses.empty:

        warehouse_fig = px.bar(

            warehouses.sort_values(

                "utilization",

                ascending=True,

            ),

            x="utilization",

            y="name",

            orientation="h",

            color="utilization",

        )

        st.plotly_chart(

            styled(warehouse_fig),

            use_container_width=True,

        )

    else:

        st.info("No warehouse information available.")

    # ==========================================================
    # Supplier Summary
    # ==========================================================

    st.write("")

    section("Supplier Risk Distribution")

    if not suppliers.empty:

        supplier_risk = (

            suppliers

            .groupby("risk_level")

            .size()

            .reset_index(name="count")

        )

        supplier_fig = px.bar(

            supplier_risk,

            x="risk_level",

            y="count",

            color="risk_level",

        )

        st.plotly_chart(

            styled(supplier_fig),

            use_container_width=True,

        )

    else:

        st.info("No supplier information available.")

    # ==========================================================
    # Active Shipments
    # ==========================================================

    st.write("")

    section("🚚 Active Shipments")

    active_shipments = ships[

        ships["status"] != "Delivered"

    ]

    if not active_shipments.empty:

        display_columns = [

            "id",

            "supplier_id",

            "origin",

            "destination",

            "mode",

            "status",

            "eta_days",

            "delay_days",

            "priority",

            "value_usd",

            "product",

        ]

        available_columns = [

            column

            for column in display_columns

            if column in active_shipments.columns

        ]

        st.dataframe(

            active_shipments[

                available_columns

            ],

            hide_index=True,

            use_container_width=True,

        )

    else:

        st.success(

            "🎉 No active shipment disruptions."

        )

    # ==========================================================
    # Executive Summary
    # ==========================================================

    st.write("")

    section("Executive Summary")

    st.markdown(

        f"""

**Overall Health:** **{brief['overall_health']}**

### Shipment Overview

- Total Shipments : **{brief['shipments']['total_shipments']}**
- Delayed Shipments : **{brief['shipments']['delayed']}**
- Value at Risk : **{money(brief['shipments']['value_at_risk_usd'])}**

### Inventory

- SKUs : **{brief['inventory']['skus']}**
- Low Stock Items : **{brief['inventory']['low_stock_lines']}**

### Orders

- Orders at Risk : **{brief['orders']['at_risk']}**
- Revenue at Risk : **{money(brief['orders']['revenue_at_risk_usd'])}**

### Incidents

- Open Incidents : **{brief['incidents']['open']}**
- Critical Incidents : **{brief['incidents']['critical']}**

### Warehouses

- Total Warehouses : **{brief['warehouses']['count']}**
- Warehouses Near Capacity : **{brief['warehouses']['at_capacity']}**

""",

        unsafe_allow_html=True,

    )