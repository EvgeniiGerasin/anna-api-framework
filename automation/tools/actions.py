import requests
import allure
from requests import Response

from tools.report import Report


class Action:

    def __init__(self, url):

        self._s = requests.session()
        self.url = url
        self._report = Report()

    def request(self, type: str, **kwargs) -> Response:
        """method of request

        Args:
            type (str): type of request GET, POST and etc.
        Returns:
            Response: responce of request
        """

        with allure.step(f'GET request'):
            self._report.put_request(kwargs)
            if type == 'GET':
                responce = self._s.get(self.url, **kwargs)
            elif type == 'POST':
                responce = self._s.post(self.url, **kwargs)
            self._report.put_responce(responce)
        return responce
