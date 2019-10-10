import komand
from komand.exceptions import PluginException
import json
from requests import Session, Request, request
from json import JSONDecodeError


class KACE:

    def __init__(self, base_url, org, headers, data, verify):
        self._base_url = base_url
        self.org = org
        self.headers = headers
        self.data = data
        self.verify = verify
        self.session = Session()

    def _call_api(self, method, endpoint, params=None, data=None):
        url = self._base_url + '/ams/shared/api/security/login'
        self.session.headers = self.headers

        resp = self.session.post(url, json=self.data, verify=self.verify,)

        if resp.status_code not in range(200, 299):
            raise PluginException(
                cause="Received HTTP %d status code from grabbing the Token for KACE. Please verify your KACE server and credentials and try again.",
                assistance="If the issue persists please contact support.",
                data=f"{resp.status_code} {resp.text}"
            )

        try:
            resp_data = resp.json()
        except json.decoder.JSONDecodeError:
            raise PluginException(
                cause="Received an unexpected response from KACE ",
                assistance="(non-JSON or no response was received).",
                data=resp.text
            )

        self.session.headers.update({'x-dell-csrf-token': resp.headers['x-dell-csrf-token']})

        url2 = self._base_url + endpoint

        if method == "POST":
            resp2 = self.session.post(url2, verify=False,)
        elif method == "GET":
            resp2 = self.session.get(url2, verify=False,)

        if resp2.status_code not in range(200, 299):
            raise PluginException(
                cause="Received HTTP %d status code from the KACE Inventory Lookup. Please verify your KACE server status and try again.",
                assistance="If the issue persists please contact support.",
                data=f"{resp2.status_code} {resp2.text}"
            )

        try:
            content = resp2.json()
        except json.decoder.JSONDecodeError:
            raise PluginException(
                cause="Received an unexpected response from KACE ",
                assistance="(non-JSON or no response was received).",
                data=resp2.text
            )

        if "Machines" in content:
            system = content["Machines"]
            return {
                "success": True,
                "result": system
            }

        elif "Result" in content:
            system = content["Result"]
            return {
                "success": True,
                "result": system
            }

        else:
            return {
                "success": True,
                "result": content
            }

    def machine_inventory(self, device):
        endpoint = '/api/inventory/machines?filtering=machine.Name co ' + device

        return self._call_api("GET", endpoint)

    def system_refresh(self, device):
        inventory = self.machine_inventory(device)

        id = inventory["result"][0]["Id"]
        endpoint = '/api/inventory/machines/' + id + '/force/'

        return self._call_api("POST", endpoint)
