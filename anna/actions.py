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
            self._report.request(kwargs)
            if method == 'GET':
                responce = self._s.get(self.url, **kwargs)
            elif method == 'POST':
                responce = self._s.post(self.url, **kwargs)
            self._report.responce(responce)
        return responce
