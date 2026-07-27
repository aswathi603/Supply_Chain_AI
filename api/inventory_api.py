from api.base_api import BaseAPI


class InventoryAPI(BaseAPI):

    entity = "inventory"


def list_inventory():

    return InventoryAPI.list()


def inventory_df():

    return InventoryAPI.dataframe()