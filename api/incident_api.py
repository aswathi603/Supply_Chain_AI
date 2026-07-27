from api.base_api import BaseAPI


class IncidentAPI(BaseAPI):

    entity = "incidents"


def list_incidents():

    return IncidentAPI.list()


def incidents_df():

    return IncidentAPI.dataframe()