"""
Formatting Utilities
"""


def fmt_number(value):

    try:

        return f"{float(value):,.0f}"

    except Exception:

        return str(value)


def truncate(

    text: str,

    length: int = 80,

):

    if not text:

        return ""

    if len(text) <= length:

        return text

    return text[: length - 3] + "..."