"""
Domain Calculations
"""

import math


EARTH_RADIUS_KM = 6371.0


def haversine_km(
    lat1: float,
    lon1: float,
    lat2: float,
    lon2: float,
) -> float:
    """
    Calculate distance between two coordinates.
    """

    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)

    delta_phi = math.radians(
        lat2 - lat1
    )

    delta_lambda = math.radians(
        lon2 - lon1
    )

    a = (

        math.sin(delta_phi / 2) ** 2

        + math.cos(phi1)

        * math.cos(phi2)

        * math.sin(delta_lambda / 2) ** 2

    )

    return round(

        2

        * EARTH_RADIUS_KM

        * math.asin(

            math.sqrt(a)

        ),

        2,

    )


def transit_cost(

    distance_km: float,

    cost_per_km: float,

    containers: int = 1,

) -> float:

    return round(

        distance_km

        * cost_per_km

        * containers,

        2,

    )


def transit_days(

    distance_km: float,

    days_per_1000km: float,

) -> float:

    return round(

        (distance_km / 1000)

        * days_per_1000km,

        2,

    )