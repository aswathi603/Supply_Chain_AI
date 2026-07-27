"""
Inventory Redistribution Simulation

Simulates inventory movement between warehouses
to reduce stockout risk.
"""

from api.inventory_api import inventory_df

from simulations.base_simulation import simulation_result


def run(
    sku: str = "SKU-EL-001",
):
    """
    Simulate redistribution of inventory
    between warehouses.
    """

    df = inventory_df().copy()

    inventory = df[
        df["sku"] == sku
    ].copy()

    if inventory.empty:

        return simulation_result(

            scenario="Inventory Redistribution",

            summary=f"SKU '{sku}' not found.",

            recommendation="Verify the SKU.",

            confidence=1.0,

        )

    donors = inventory[
        inventory["days_of_supply"] > 20
    ].copy()

    receivers = inventory[
        inventory["days_of_supply"] < 10
    ].copy()

    if donors.empty or receivers.empty:

        return simulation_result(

            scenario="Inventory Redistribution",

            summary="No redistribution required.",

            recommendation="Current inventory distribution is balanced.",

            confidence=0.95,

        )

    transfer_plan = []

    total_units = 0

    estimated_cost = 0

    for _, receiver in receivers.iterrows():

        if donors.empty:
            break

        donor = donors.iloc[0]

        transfer_units = int(

            min(

                2000,

                donor["units_on_hand"] * 0.30,

            )

        )

        transfer_plan.append(

            {

                "from_warehouse":

                    donor["warehouse_id"],

                "to_warehouse":

                    receiver["warehouse_id"],

                "sku":

                    sku,

                "units":

                    transfer_units,

            }

        )

        total_units += transfer_units

        estimated_cost += transfer_units * 0.25

    recommendation = (

        "Redistribute inventory immediately to "

        "reduce stockout risk and improve service "

        "levels across warehouses."

    )

    return simulation_result(

        scenario="Inventory Redistribution",

        summary=(

            f"Redistribution plan generated for "

            f"{sku}."

        ),

        before={

            "donor_warehouses":

                len(donors),

            "receiver_warehouses":

                len(receivers),

        },

        after={

            "planned_transfers":

                len(transfer_plan),

            "units_to_transfer":

                total_units,

        },

        impact={

            "transfer_plan":

                transfer_plan,

            "estimated_transfer_cost_usd":

                round(

                    estimated_cost,

                    2,

                ),

            "expected_service_level_improvement":

                "High",

            "expected_stockout_reduction":

                len(receivers),

        },

        recommendation=recommendation,

        confidence=0.80,

    )