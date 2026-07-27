from api.base_api import BaseAPI


class TransportationAPI(BaseAPI):

    entity = "transportation"


def list_modes():

    return TransportationAPI.list()


def modes_df():

    return TransportationAPI.dataframe()