"""
Order Service
"""

from typing import Dict, List

from api.order_api import orders_df


def at_risk() -> List[Dict]:
    """
    Return orders marked as At Risk.
    """

    df = orders_df()

    return df[
        df["status"] == "At Risk"
    ].to_dict(
        orient="records"
    )


def summary() -> Dict:
    """
    Generate order KPIs.
    """

    df = orders_df()

    return {

        "orders":
            int(len(df)),

        "at_risk":
            int(
                (df["status"] == "At Risk").sum()
            ),

        "revenue_at_risk_usd":
            round(
                float(
                    df.loc[
                        df["status"] == "At Risk",
                        "value_usd",
                    ].sum()
                ),
                2,
            ),

    }