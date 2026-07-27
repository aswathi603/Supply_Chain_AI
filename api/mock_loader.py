"""
Mock API Loader
"""

from utils.json_loader import (
    load_json,
    load_df,
)


def api_get(
    entity: str,
):

    try:

        return load_json(entity)

    except Exception as ex:

        raise RuntimeError(
            f"Unable to load {entity}"
        ) from ex


def api_get_df(
    entity: str,
):

    try:

        return load_df(entity)

    except Exception as ex:

        raise RuntimeError(
            f"Unable to load dataframe for {entity}"
        ) from ex