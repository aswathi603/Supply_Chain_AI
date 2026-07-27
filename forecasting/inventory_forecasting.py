"""
Inventory Forecasting
"""

from api.inventory_api import inventory_df

from forecasting.base_forecaster import (
    forecast_metadata,
)


def days_of_supply_outlook():
    """
    Forecast inventory outlook.
    """

    df = inventory_df().copy()

    df["outlook_7d"] = (

        df["days_of_supply"]

        - 7

    ).clip(
        lower=0
    )

    df["risk"] = df["days_of_supply"].apply(

        lambda days:

        "High"

        if days < 7

        else

        (

            "Medium"

            if days < 14

            else "Low"

        )

    )

    return {

        "metadata":

            forecast_metadata(
                "Inventory Forecast"
            ),

        "forecast":

            df.to_dict(
                orient="records"
            ),

    }