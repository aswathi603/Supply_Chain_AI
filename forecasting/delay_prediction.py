"""
Delay Prediction
"""

from forecasting.base_forecaster import forecast_metadata

from api.shipment_api import shipments_df


def predict_delays():

    df = shipments_df().copy()

    def calculate_risk(row):

        risk = 0.10

        if row["mode"] == "Ocean":
            risk += 0.35

        elif row["mode"] == "Road":
            risk += 0.15

        if row["status"] == "Delayed":
            risk += 0.25

        elif row["status"] == "At Customs":
            risk += 0.20

        return min(round(risk, 2), 0.99)

    df["delay_risk"] = df.apply(
        calculate_risk,
        axis=1,
    )

    return {

        "metadata":

            forecast_metadata(
                "Delay Prediction"
            ),

        "predictions":

            df[
                [
                    "id",
                    "product",
                    "mode",
                    "status",
                    "delay_risk",
                ]
            ].to_dict(
                orient="records"
            ),

    }