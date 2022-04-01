import json
from this import s
import allure

from requests import Response


class Report:
    
    # severity
    @staticmethod
    def severity(level: str):
        """Putting the severity in report

        Args:
            level (str): May be one of
            BLOCKER, CRITICAL, NORMAL, MINOR, TRIVIAL
        """
        if level == 'BLOCKER':
            allure.severity(allure.severity_level.BLOCKER)
        elif level == 'CRITICAL':
            allure.severity(allure.severity_level.CRITICAL)
        elif level == 'NORMAL':
            return allure.severity(allure.severity_level.NORMAL)
        elif level == 'MINOR':
            allure.severity(allure.severity_level.MINOR)
        elif level == 'TRIVIAL':
            allure.severity(allure.severity_level.TRIVIAL)

    # links
    @staticmethod
    def link(url, name):
        """Putting the link test in report"""
        return allure.link(url, name)

    @staticmethod
    def test_case(url, name):
        """Putting the link of test case in report"""
        return Report.test_case(url, name)

    @staticmethod
    def issue(url, name):
        """Putting the link of issue in report"""
        return Report.issue(url, name)

    # allure tags
    @staticmethod
    def feature(text: str):
        """Putting the feature test in report"""
        return allure.feature(text)

    @staticmethod
    def title(text: str):
        """Putting the title test in report"""
        return allure.title(text)

    @staticmethod
    def epic(text: str):
        """Putting the epic test in report"""
        return allure.title(text)

    @staticmethod
    def story(text: str):
        """Putting the story test in report"""
        return allure.title(text)

    # allure step
    @staticmethod
    def step(name: str):
        """Putting the step test in report"""
        return allure.step(name)

    # other custom attachements
    @staticmethod
    def put_description(**kwargs):
        """Putting a description in report

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
        """Putting a info on request in report

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
