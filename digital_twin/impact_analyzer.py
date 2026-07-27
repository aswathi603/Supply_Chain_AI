"""
Impact Analyzer
"""


def analyze(result: dict):

    delta = result.get("delta", {})

    return {

        "time_saved_days":

            delta.get(
                "time_saved_days",
                0,
            ),

        "extra_cost_usd":

            delta.get(
                "extra_cost_usd",
                0,
            ),

        "service_level_uplift_pct":

            delta.get(
                "service_level_uplift_pct",
                0,
            ),

        "risk_score":

            delta.get(
                "risk_score",
                0,
            ),

    }