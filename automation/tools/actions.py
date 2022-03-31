import requests
import allure
from requests import Response

from tools.report import Report


class Action:

    def __init__(self, url):

        self._s = requests.session()
        self.url = url
        self._report = Report()

# info request
# url
# header request
# coocke
# body

    def get(self, **kwargs) -> Response:
        """GET method of request

        Returns:
            Response: responce of request
        """

        with allure.step(f'GET request: {self.url}'):
            self._report.put_request(kwargs)
            responce = self._s.get(self.url, **kwargs)
            self._report.put_responce(responce)
            responce
        return responce
