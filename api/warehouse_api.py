from api.base_api import BaseAPI


class WarehouseAPI(BaseAPI):

    entity = "warehouses"


def list_warehouses():

    return WarehouseAPI.list()


def warehouses_df():

    return WarehouseAPI.dataframe()