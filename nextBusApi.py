import requests

# Next Bus Arrival Time API Wrapper of Citybus Limtied and New World First Bus Services Limited 
class NextBusArrivalTimeAPI():
    def __init__(self):
        # Based on API SPECS: https://www.nwstbus.com.hk/datagovhk/bus_eta_api_specifications.pdf
        self.name = "NextBusArrivalTimeAPI"
        self.version = "v1"
        self._base_url = "https://rt.data.gov.hk"

    def request_get(self, url: str):
        try:
            response = requests.get(url)
            response = response.json()
            return response
        except Exception as e:
            print(f"Error: {e}")
            return {"Error": str(e)}

    def validate_company_id(self, company_id: str):
        if company_id in ["NWFB", "CTB"]:
            return True
        else:
            errormsg = "company_id not supported, please either pass `NWFB` or `CTB` as company_id"
            print(errormsg)
            return False

    def validate_direction(self, direction):
        if direction in ["inbound", "outbound"]:
            return True
        else:
            errormsg = "Invalid direction, please either pass `inbound` or `outbound` as direction"
            print(errormsg)
            return False

    def validate_company_id_and_direction(self, company_id: str, direction: str):
        validate_company = self.validate_company_id(company_id)
        validate_direction = self.validate_direction(direction)
        if validate_company & validate_direction:
            return True
        else:
            return False

    def get_company_info(self, company_id: str):
        valid = self.validate_company_id(company_id)
        if valid == True:
            endpoint = f"{self._base_url}/v1/transport/citybus-nwfb/company/{company_id}"
            resp = self.request_get(endpoint)
            return resp
        else:
            return {"Error": "Invalid Company ID"}

    def get_route(self, company_id: str, route: str):
        valid = self.validate_company_id(company_id)
        if valid:
            endpoint = f"{self._base_url}/v1/transport/citybus-nwfb/route/{company_id}/{route}"
            resp = self.request_get(endpoint)
            return resp
        else:
            return {"Error": "Invalid Company ID"}

    def get_stop(self, stop_id: str):
        endpoint = f"{self._base_url}/v1/transport/citybus-nwfb/stop/{stop_id}"
        resp = self.request_get(endpoint)
        return resp

    def get_route_stop(self, company_id: str, route: str, direction: str):
        valid = self.validate_company_id_and_direction(company_id, direction)
        if valid:
            endpoint = f"{self._base_url}/v1/transport/citybus-nwfb/route-stop/{company_id}/{route}/{direction}"
            resp = self.request_get(endpoint)
            return resp
        else:
            return {"Error": "Invalid Company ID or direction"}

    def get_eta(self, company_id: str, route: str, stop_id: str):
        valid = self.validate_company_id(company_id)
        if valid:
            endpoint = f"{self._base_url}/v1/transport/citybus-nwfb/eta/{company_id}/{stop_id}/{route}"
            print(endpoint)
            resp = self.request_get(endpoint)
            return resp
        else:
            return {"Error": "Invalid Company ID"}
