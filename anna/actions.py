import requests
import allure
from requests import Response

from anna.report import Report

class Action:

    def __init__(self, url):

        self._s = requests.session()
        self.url = url
        self._report = Report()

    def request(self, method: str, **kwargs) -> Response:
        """method of request

        Args:
            method (str): method of request GET, POST and etc.
        Returns:
            Response: responce of request
        """
        with allure.step(f'GET request'):
            responce = self._s.request(method, self.url, **kwargs)
            self._report.responce(responce)
        return responce
