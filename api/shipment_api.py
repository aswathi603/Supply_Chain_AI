from api.base_api import BaseAPI


class ShipmentAPI(BaseAPI):

    entity = "shipments"


def list_shipments():

    return ShipmentAPI.list()


def shipments_df():

    return ShipmentAPI.dataframe()


def get_shipment(
    shipment_id: str,
):

    return ShipmentAPI.get_by_id(
        shipment_id
    )