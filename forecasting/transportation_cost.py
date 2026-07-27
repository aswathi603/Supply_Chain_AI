"""
Transportation Cost Forecast
"""

from api.transportation_api import (
    modes_df,
)

from forecasting.base_forecaster import (
    forecast_metadata,
)


def cost_outlook(
    distance_km: float = 10000,
):
    """
    Forecast transportation cost.
    """

    df = modes_df().copy()

    df["projected_cost_usd"] = (

        df["avg_cost_per_km_usd"]

        * distance_km

    ).round(
        0
    )

    return {

        "metadata":

            forecast_metadata(
                "Transportation Cost Forecast"
            ),

        "forecast":

            df.to_dict(
                orient="records"
            ),

    }