"""
Incident Service
"""

from typing import Dict, List

from api.incident_api import incidents_df

OPEN = "Open"
CRITICAL = "Critical"


def open_incidents() -> List[Dict]:
    """
    Return all open incidents.
    """

    df = incidents_df()

    return df[
        df["status"] == OPEN
    ].to_dict(
        orient="records"
    )


def summary() -> Dict:
    """
    Generate incident KPIs.
    """

    df = incidents_df()

    return {

        "open":
            int(
                (df["status"] == OPEN).sum()
            ),

        "critical":
            int(
                (df["severity"] == CRITICAL).sum()
            ),

        "total_impact_usd":
            round(
                float(
                    df.loc[
                        df["status"] == OPEN,
                        "impact_usd",
                    ].sum()
                ),
                2,
            ),

    }