import json
import allure
import json

from requests import Response


class Report:

    def put_request(self, data):
        """Putting info on request in report

        Args:
            request (any): data
        """
        allure.attach(
            json.dumps(data), 'Request information', allure.attachment_type.JSON
        )

    def put_responce(self, responce: Response):
        """Putting info on responce in report. For example:
        body, headers, coockes, status code

        Args:
            responce (Response)
        """
        # need for correct view in report
        allure.attach(
            f'{responce.request.body}', 'Request body', allure.attachment_type.TEXT
        )
        allure.attach(
            f'{responce.request.headers}', 'Request header', allure.attachment_type.TEXT
        )
        allure.attach(
            f'{responce.request.url}', 'Request url', allure.attachment_type.TEXT
        )
        allure.attach(
            f'{responce.status_code}', 'Responce status code', allure.attachment_type.TEXT
        )
        allure.attach(
            '{}'.format(responce.text.replace('\'', '""')), 'Responce body', allure.attachment_type.JSON
        )
        allure.attach(
            f'{responce.headers}', 'Responce headers', allure.attachment_type.TEXT
        )
        allure.attach(
            f'{responce.cookies}', 'Responce coocke', allure.attachment_type.TEXT
        )
