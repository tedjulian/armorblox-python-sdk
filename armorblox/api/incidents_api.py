import requests
from urllib.parse import urlparse

ARMORBLOX_INCIDENT_API_PATH = "api/v1beta1/organizations/{}/incidents"
ARMORBLOX_INCIDENT_API_PAGE_SIZE = 100
ARMORBLOX_INCIDENT_API_TIME_FORMAT = "%Y-%m-%dT%H:%M:%SZ"
ARMORBLOX_INSTANCE_NAME = ""
ARMORBLOX_INSTANCE_URL = ""

class IncidentsApi:

    def __init__(self):
        pass

    def list_incidents(self):
        params = {
            "from_date": "",
            "to_date": "",
            "page_size": ARMORBLOX_INCIDENT_API_PAGE_SIZE,
            "page_token": ""
        }

        headers = {
            "x-ab-authorization": "",
            "Content-Type": "application/json",
        }

        url = ""
        if ARMORBLOX_INSTANCE_URL:
            tenant_name = urlparse(ARMORBLOX_INSTANCE_URL).netloc.split(".")[0]
            path = ARMORBLOX_INCIDENT_API_PATH.format(tenant_name)
            if not ARMORBLOX_INSTANCE_URL.endswith("/"):
                path = "/" + path

            url = ARMORBLOX_INSTANCE_URL + path
        else:
            url = "https://{}.armorblox.io/{}".format(ARMORBLOX_INSTANCE_NAME, ARMORBLOX_INCIDENT_API_PATH.format(ARMORBLOX_INSTANCE_NAME))

        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            response_json = response.json()
            next_page_token = response_json.get("next_page_token", None)
            return response_json.get("incidents", [])
        else:
            return []
