from api.base_api import BaseAPI


class SupplierAPI(BaseAPI):

    entity = "suppliers"


def list_suppliers():

    return SupplierAPI.list()


def suppliers_df():

    return SupplierAPI.dataframe()


def get_supplier(
    supplier_id,
):

    return SupplierAPI.get_by_id(
        supplier_id
    )