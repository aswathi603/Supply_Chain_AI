"""
Risk Assessment Simulation

Evaluates overall supply chain risk by combining
shipment, supplier, warehouse, and incident data.
"""

from api.shipment_api import shipments_df
from api.incident_api import incidents_df
from api.supplier_api import suppliers_df
from api.warehouse_api import warehouses_df

from simulations.base_simulation import simulation_result


def run():
    """
    Assess overall supply chain risk.
    """

    shipments = shipments_df()

    incidents = incidents_df()

    suppliers = suppliers_df()

    warehouses = warehouses_df()

    delayed_shipments = int(

        (shipments["status"] == "Delayed").sum()

    )

    customs_shipments = int(

        (shipments["status"] == "At Customs").sum()

    )

    critical_incidents = int(

        (incidents["severity"] == "Critical").sum()

    )

    risky_suppliers = int(

        suppliers["risk_level"].isin(

            [

                "High",

                "Critical",

            ]

        ).sum()

    )

    overloaded_warehouses = int(

        (

            warehouses["utilization"] >= 0.85

        ).sum()

    )

    score = 0

    score += delayed_shipments * 3

    score += customs_shipments * 2

    score += critical_incidents * 10

    score += risky_suppliers * 4

    score += overloaded_warehouses * 5

    score = min(score, 100)

    if score >= 70:

        level = "Critical"

    elif score >= 50:

        level = "High"

    elif score >= 25:

        level = "Medium"

    else:

        level = "Low"

    if level == "Critical":

        recommendation = (

            "Immediate executive attention required. "

            "Prioritize recovery plans, reroute critical "

            "shipments, and activate alternate suppliers."

        )

    elif level == "High":

        recommendation = (

            "Closely monitor affected operations and "

            "begin mitigation for high-risk suppliers "

            "and delayed shipments."

        )

    elif level == "Medium":

        recommendation = (

            "Monitor KPIs and prepare contingency "

            "plans if conditions worsen."

        )

    else:

        recommendation = (

            "Current operations are stable. "

            "Continue routine monitoring."

        )

    return simulation_result(

        scenario="Supply Chain Risk Assessment",

        summary=(

            f"Overall supply chain risk is "

            f"{level}."

        ),

        before={

            "overall_risk_score":

                score,

        },

        after={

            "risk_level":

                level,

        },

        impact={

            "delayed_shipments":

                delayed_shipments,

            "customs_shipments":

                customs_shipments,

            "critical_incidents":

                critical_incidents,

            "high_risk_suppliers":

                risky_suppliers,

            "overloaded_warehouses":

                overloaded_warehouses,

        },

        recommendation=recommendation,

        confidence=0.91,

    )