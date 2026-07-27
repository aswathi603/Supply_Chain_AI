"""
Premium Customer Priority Simulation

Simulates order prioritization based on customer
priority and business value.
"""

from api.order_api import orders_df

from simulations.base_simulation import simulation_result


PRIORITY_WEIGHTS = {

    "Strategic": 3,

    "Premium": 2,

    "Standard": 1,

}


def run():
    """
    Simulate priority-based order fulfillment.
    """

    df = orders_df().copy()

    if df.empty:

        return simulation_result(

            scenario="Premium Customer Priority",

            summary="No orders available.",

            recommendation="No prioritization required.",

            confidence=1.0,

        )

    df["priority_score"] = (

        df["priority"]

        .map(PRIORITY_WEIGHTS)

        .fillna(0)

    )

    df = df.sort_values(

        [

            "priority_score",

            "value_usd",

        ],

        ascending=[

            False,

            False,

        ],

    )

    strategic_orders = int(

        (

            df["priority"]

            == "Strategic"

        ).sum()

    )

    premium_orders = int(

        (

            df["priority"]

            == "Premium"

        ).sum()

    )

    standard_orders = int(

        (

            df["priority"]

            == "Standard"

        ).sum()

    )

    recommendation = (

        "Fulfill Strategic orders first, "

        "followed by Premium customers, "

        "then Standard orders to maximize "

        "customer satisfaction and business value."

    )

    return simulation_result(

        scenario="Premium Customer Priority",

        summary="Generated optimized fulfillment queue.",

        before={

            "total_orders":

                len(df),

        },

        after={

            "strategic_orders":

                strategic_orders,

            "premium_orders":

                premium_orders,

            "standard_orders":

                standard_orders,

        },

        impact={

            "recommended_dispatch_order":

                df[

                    [

                        "id",

                        "customer_name",

                        "priority",

                        "value_usd",

                        "status",

                    ]

                ].to_dict(

                    orient="records"

                ),

            "highest_priority_customer":

                (

                    df.iloc[0]["customer_name"]

                    if not df.empty

                    else None

                ),

            "highest_priority_order":

                (

                    df.iloc[0]["id"]

                    if not df.empty

                    else None

                ),

            "estimated_service_level":

                "High",

        },

        recommendation=recommendation,

        confidence=0.88,

    )