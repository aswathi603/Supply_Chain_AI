"""
Reporting Service

Generates an executive summary of the entire
supply chain.
"""

from datetime import datetime

from services.shipment_service import summary as shipment_summary
from services.inventory_service import summary as inventory_summary
from services.order_service import summary as order_summary
from services.incident_service import summary as incident_summary
from services.warehouse_service import summary as warehouse_summary


def _overall_health(
    shipments: dict,
    incidents: dict,
    warehouses: dict,
) -> str:
    """
    Determine overall supply chain health.
    """

    if incidents["critical"] > 0:
        return "Critical"

    if shipments["delayed"] > 10:
        return "Warning"

    if warehouses["at_capacity"] > 2:
        return "Warning"

    return "Healthy"


def executive_brief() -> dict:
    """
    Build executive KPI report.
    """

    shipments = shipment_summary()

    inventory = inventory_summary()

    orders = order_summary()

    incidents = incident_summary()

    warehouses = warehouse_summary()

    return {

        "generated_at":

            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),

        "overall_health":

            _overall_health(
                shipments,
                incidents,
                warehouses,
            ),

        "shipments":

            shipments,

        "inventory":

            inventory,

        "orders":

            orders,

        "incidents":

            incidents,

        "warehouses":

            warehouses,

    }