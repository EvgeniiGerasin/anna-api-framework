import requests
import allure
from requests import Response

from anna.report import Report

class Action:
    # python setup.py sdist
    # twine check dist/*  

    def __init__(self, url=None):

        self._s = requests.session()
        self.url = url
        self._report = Report()

    def request(self, method: str, url: str, **kwargs) -> Response:
        """method of request

        Args:
            method (str): method of request GET, POST and etc.
            url (str): url of request
        Returns:
            Response: responce of request
        """
        with allure.step('{} {}'.format(method, url)):
            responce = self._s.request(method, url, **kwargs)
            self._report.responce(responce)
        return responce
