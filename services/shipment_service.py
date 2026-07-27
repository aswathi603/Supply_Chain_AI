"""
Shipment Service

Business logic for shipment analytics.
"""

from typing import Dict, List

from api.shipment_api import shipments_df


def summary() -> Dict:
    """
    Generate shipment KPIs.
    """

    df = shipments_df()

    delayed = df["status"] == "Delayed"
    customs = df["status"] == "At Customs"

    return {

        "total_shipments": int(len(df)),

        "in_transit": int(
            (df["status"] == "In Transit").sum()
        ),

        "delivered": int(
            (df["status"] == "Delivered").sum()
        ),

        "delayed": int(
            delayed.sum()
        ),

        "at_customs": int(
            customs.sum()
        ),

        "cancelled": int(
            (df["status"] == "Cancelled").sum()
        ),

        "value_at_risk_usd": round(

            float(

                df.loc[
                    delayed | customs,
                    "value_usd",
                ].sum()

            ),

            2,

        ),

        "average_delay_days": round(

            float(

                df["delay_days"].mean()

            ),

            2,

        ),

    }


def delayed() -> List[Dict]:
    """
    Return all delayed shipments.
    """

    df = shipments_df()

    delayed_df = df[df["status"] == "Delayed"]

    return delayed_df.to_dict(
        orient="records"
    )


def shipment_by_id(
    shipment_id: str,
) -> Dict | None:
    """
    Return one shipment.
    """

    df = shipments_df()

    matches = df[
        df["id"] == shipment_id
    ]

    if matches.empty:
        return None

    return matches.iloc[0].to_dict()


def high_priority_shipments() -> List[Dict]:
    """
    Return Premium and Strategic shipments.
    """

    df = shipments_df()

    priority_df = df[
        df["priority"].isin(
            [
                "Premium",
                "Strategic",
            ]
        )
    ]

    return priority_df.to_dict(
        orient="records"
    )


def shipments_at_customs() -> List[Dict]:
    """
    Shipments currently at customs.
    """

    df = shipments_df()

    customs_df = df[
        df["status"] == "At Customs"
    ]

    return customs_df.to_dict(
        orient="records"
    )