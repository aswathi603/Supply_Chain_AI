"""
Demand Spike Simulation

Simulates a sudden increase in product demand and
evaluates its impact on inventory availability.
"""

from api.inventory_api import inventory_df

from simulations.base_simulation import simulation_result


def run(
    product: str = "Semiconductors",
    spike_pct: int = 40,
):
    """
    Simulate a sudden demand spike.
    """

    df = inventory_df().copy()

    inventory = df[
        df["product"] == product
    ].copy()

    if inventory.empty:

        return simulation_result(

            scenario="Demand Spike",

            summary=f"No inventory found for '{product}'.",

            recommendation="Verify the product name.",

            confidence=1.0,

        )

    inventory["new_days_of_supply"] = (

        inventory["days_of_supply"]

        / (1 + spike_pct / 100)

    ).round(1)

    inventory["stockout_risk"] = inventory[
        "new_days_of_supply"
    ].apply(

        lambda days:

        "High"

        if days < 7

        else (

            "Medium"

            if days < 14

            else "Low"

        )

    )

    stockout_lines = int(

        (

            inventory["stockout_risk"]

            == "High"

        ).sum()

    )

    average_before = round(

        inventory["days_of_supply"].mean(),

        1,

    )

    average_after = round(

        inventory["new_days_of_supply"].mean(),

        1,

    )

    recommendation = (

        "Increase procurement for affected SKUs, "

        "prioritize Premium and Strategic customer orders, "

        "and redistribute inventory across warehouses "

        "to reduce stockout risk."

    )

    return simulation_result(

        scenario="Demand Spike",

        summary=(

            f"Demand for '{product}' increased by "

            f"{spike_pct}%."

        ),

        before={

            "average_days_of_supply":

                average_before,

            "warehouse_count":

                int(

                    inventory["warehouse_id"]

                    .nunique()

                ),

        },

        after={

            "average_days_of_supply":

                average_after,

            "expected_stockout_lines":

                stockout_lines,

        },

        impact={

            "affected_inventory":

                inventory[
                    [

                        "sku",

                        "warehouse_id",

                        "days_of_supply",

                        "new_days_of_supply",

                        "stockout_risk",

                    ]

                ].to_dict(

                    orient="records"

                ),

            "stockout_risk_lines":

                stockout_lines,

            "business_impact":

                (

                    "Higher probability of delayed customer "

                    "orders if replenishment is not initiated."

                ),

        },

        recommendation=recommendation,

        confidence=0.79,

    )