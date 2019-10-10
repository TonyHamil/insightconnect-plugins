import komand
from komand.exceptions import PluginException
from .schema import ConnectionSchema, Input
import requests
from requests import Session, Request
import json
from icon_kace.util.api import KACE


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self._base_url = None
        self.api = None

    def connect(self, params):
        base_uri = params.get('url')
        scheme = "https://" if params.get('ssl_verify') else "http://"
        self._base_url = scheme + base_uri
        self.logger.info("Connect: Connecting..")
        username_password = params.get('username_and_password')
        self.username = username_password['username']
        self.password = username_password['password']
        self.org = params.get('organization')
        self.headers = {'Accept': 'application/json', 'Content-Type': 'application/json', 'x-dell-api-version': '9'}
        self.data = {'password': self.password, 'userName': self.username, 'organizationName': self.org}
        verify = False

        self.api = KACE(self._base_url, self.org, self.headers, self.data, verify)

    def test(self, params):
        base_url = self._base_url
        headers = self.headers
        data = self.data

        url = base_url + '/ams/shared/api/security/login'
        session = Session()

        session.headers = headers
        resp = session.post(url, json=data, verify=False,)

        if resp.status_code == 200:
            return {'success': True}
        else:
            raise PluginException(
                cause="Received HTTP %d status code from grabbing the Token for KACE. Please verify your KACE server and credentials and try again.",
                assistance="If the issue persists please contact support.",
                data=f"{resp.status_code} {resp.text}"
            )
