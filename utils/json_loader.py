"""
JSON Loader
"""

import json

from functools import lru_cache

from pathlib import Path

import pandas as pd

from config.settings import DATA_DIR


@lru_cache(maxsize=64)
def load_json(

    name: str,

):

    path = DATA_DIR / f"{name}.json"

    if not path.exists():

        raise FileNotFoundError(

            f"{path} not found."

        )

    with open(

        path,

        "r",

        encoding="utf-8",

    ) as file:

        return json.load(file)


def load_df(

    name: str,

):

    return pd.DataFrame(

        load_json(name)

    )


def clear_cache():

    load_json.cache_clear()