"""
Base API Layer

Provides reusable helper functions
for all mock APIs.
"""

from api.mock_loader import (
    api_get,
    api_get_df,
)


class BaseAPI:

    entity = ""

    @classmethod
    def list(cls):

        return api_get(cls.entity)

    @classmethod
    def dataframe(cls):

        return api_get_df(cls.entity)

    @classmethod
    def get_by_id(
        cls,
        object_id,
    ):

        for item in cls.list():

            if item.get("id") == object_id:

                return item

        return None