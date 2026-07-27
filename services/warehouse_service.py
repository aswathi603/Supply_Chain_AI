"""
Warehouse Service
"""

from typing import Dict

from api.warehouse_api import warehouses_df


def summary() -> Dict:
    """
    Generate warehouse KPIs.
    """

    df = warehouses_df()

    return {

        "count":
            int(len(df)),

        "average_utilization":
            round(
                float(
                    df["utilization"].mean()
                ),
                2,
            ),

        "at_capacity":
            int(
                (
                    df["utilization"] >= 0.85
                ).sum()
            ),

    }