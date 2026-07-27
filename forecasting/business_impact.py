"""
Business Impact Forecast
"""

from forecasting.base_forecaster import forecast_metadata

from services.reporting_service import executive_brief


def business_impact():

    report = executive_brief()

    result = {

        "revenue_at_risk_usd":

            report["orders"]["revenue_at_risk_usd"],

        "incident_impact_usd":

            report["incidents"]["total_impact_usd"],

        "shipment_value_at_risk_usd":

            report["shipments"]["value_at_risk_usd"],

    }

    result.update(

        forecast_metadata(

            "Business Impact"

        )

    )

    return result