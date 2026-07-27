"""
Output parser.
"""


def to_text(response):

    if response is None:
        return ""

    if hasattr(response, "content"):
        return response.content

    return str(response)