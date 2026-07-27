from api.base_api import BaseAPI


class OrderAPI(BaseAPI):

    entity = "orders"


def list_orders():

    return OrderAPI.list()


def orders_df():

    return OrderAPI.dataframe()