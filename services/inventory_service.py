"""
Inventory Service

Business logic for inventory analytics.
"""

from typing import Dict, List

from api.inventory_api import inventory_df


def low_stock(threshold_days: int = 10) -> List[Dict]:
    """
    Return inventory items below the specified
    days of supply threshold.
    """

    df = inventory_df()

    return df[
        df["days_of_supply"] <= threshold_days
    ].to_dict(
        orient="records"
    )


def summary() -> Dict:
    """
    Generate inventory KPIs.
    """

    df = inventory_df()

    return {

        "skus":
            int(df["sku"].nunique()),

        "warehouses":
            int(df["warehouse_id"].nunique()),

        "low_stock_lines":
            int(
                (df["days_of_supply"] <= 10).sum()
            ),

        "inventory_value_usd":
            round(
                float(
                    (
                        df["units_on_hand"]
                        * df["unit_cost_usd"]
                    ).sum()
                ),
                2,
            ),

    }