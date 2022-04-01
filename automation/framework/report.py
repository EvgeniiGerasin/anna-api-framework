import json
import allure

from requests import Response


class Report:

    @staticmethod
    def put_description(**kwargs):
        """Putting description in report

        Args:
            **kwargs: description
        """
        description = ''
        for arg, value in kwargs.items():
            description += (
                '<p>{}: <strong>{}</strong></p>'.format(arg, value)
            )
        allure.dynamic.description_html(description)

    @staticmethod
    def put_request(data):
        """Putting info on request in report

        Args:
            request (any): data
        """
        allure.attach(
            json.dumps(data), 'Request information', allure.attachment_type.JSON
        )

    @staticmethod
    def put_responce(responce: Response):
        """Putting info on responce in report. For example:
        body, headers, coockes, status code

        Args:
            responce (Response)
        """
        allure.attach(
            f'{responce.request.method}',
            'Request method',
            allure.attachment_type.TEXT
        )
        allure.attach(
            f'{responce.request.body}',
            'Request body',
            allure.attachment_type.TEXT
        )
        allure.attach(
            f'{responce.request.headers}',
            'Request header',
            allure.attachment_type.TEXT
        )
        allure.attach(
            f'{responce.request.url}',
            'Request url',
            allure.attachment_type.TEXT
        )
        allure.attach(
            f'{responce.status_code}',
            'Responce status code',
            allure.attachment_type.TEXT
        )
        allure.attach(
            '{}'.format(responce.text.replace('\'', '""')),
            'Responce body',
            allure.attachment_type.JSON
        )
        allure.attach(
            f'{responce.headers}',
            'Responce headers',
            allure.attachment_type.TEXT
        )
        allure.attach(
            f'{responce.cookies}',
            'Responce coocke',
            allure.attachment_type.TEXT
        )
