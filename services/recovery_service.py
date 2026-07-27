"""
Recovery Service

Generates recovery recommendations for delayed shipments.
"""

from typing import Dict, List

from services.shipment_service import delayed


def recovery_plan(shipment_id: str | None = None) -> List[Dict]:
    """
    Generate recovery plans for delayed shipments.

    Args:
        shipment_id: Optional shipment ID.
                     If supplied, generate recommendations only
                     for that shipment.

    Returns:
        List of recovery recommendations.
    """

    delayed_shipments = delayed()

    if shipment_id:

        delayed_shipments = [

            shipment

            for shipment in delayed_shipments

            if shipment["id"] == shipment_id

        ]

    plans = []

    for shipment in delayed_shipments:

        eta = shipment.get("eta_days", 0)

        priority = shipment.get("priority", "Standard")

        product = shipment.get("product", "Unknown")

        plans.append(

            {

                "shipment_id": shipment["id"],

                "priority": priority,

                "product": product,

                "recommendations": [

                    {

                        "strategy": "Air Freight",

                        "estimated_cost_usd": 12000,

                        "eta_reduction_days": max(1, eta // 2),

                        "confidence": 0.93,

                        "business_impact":

                            "Fastest delivery with higher transportation cost."

                    },

                    {

                        "strategy": "Inventory Redistribution",

                        "estimated_cost_usd": 4500,

                        "eta_reduction_days": max(1, eta // 3),

                        "confidence": 0.88,

                        "business_impact":

                            "Utilizes nearby warehouses to fulfill demand."

                    },

                    {

                        "strategy": "Alternate Supplier",

                        "estimated_cost_usd": 7000,

                        "eta_reduction_days": max(1, eta // 2),

                        "confidence": 0.90,

                        "business_impact":

                            "Maintains supply continuity through backup suppliers."

                    },

                ]

            }

        )

    return plans