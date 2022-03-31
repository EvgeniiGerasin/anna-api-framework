import requests
import allure

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


    def get(self, **kwargs):

        with allure.step(f'GET request: {self.url}'):
            
            # allure.attach(
            #     f'{kwargs}', 'Information on request', allure.attachment_type.JSON
            # )
            self._report.put_request(kwargs)
            responce = self._s.get(self.url, **kwargs)
            # allure.attach(
            #     f'{responce.url} \n {responce.headers} \n {responce.status_code}', 'Full request', allure.attachment_type.URI_LIST
            # )
            self._report.put_responce(responce)
            # r = responce.text.replace('\'', '"')
            # allure.attach(
            #     f'{r}', 'Body', allure.attachment_type.JSON
            # )
            responce
        return responce

