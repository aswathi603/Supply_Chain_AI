"""
General Helper Functions
"""

import pandas as pd


def money(value):

    try:

        value = float(value)

    except Exception:

        return "-"

    if abs(value) >= 1_000_000:

        return f"${value/1_000_000:.2f}M"

    if abs(value) >= 1_000:

        return f"${value/1_000:.1f}K"

    return f"${value:,.2f}"


def pct(value):

    try:

        return f"{float(value)*100:.1f}%"

    except Exception:

        return "-"


def safe_df(data):

    if isinstance(data, pd.DataFrame):

        return data

    return pd.DataFrame(data)


def safe_get(

    dictionary,

    key,

    default=None,

):

    if dictionary is None:

        return default

    return dictionary.get(

        key,

        default,

    )