import json
from this import s
import allure

from requests import Response


class Report:

    # severity
    @staticmethod
    def severity(level: str):
        """Inserts a test severity into the report

        Args:
            level (str): May be one of
            BLOCKER, CRITICAL, NORMAL, MINOR, TRIVIAL
        """
        if level == 'BLOCKER':
            return allure.severity(allure.severity_level.BLOCKER)
        elif level == 'CRITICAL':
            return allure.severity(allure.severity_level.CRITICAL)
        elif level == 'NORMAL':
            return allure.severity(allure.severity_level.NORMAL)
        elif level == 'MINOR':
            return allure.severity(allure.severity_level.MINOR)
        elif level == 'TRIVIAL':
            return allure.severity(allure.severity_level.TRIVIAL)

    # links
    @staticmethod
    def link(url, name):
        """Inserts a link into the report"""
        return allure.link(url=url, name=name)

    @staticmethod
    def testcase(url, name):
        """Inserts a link to a test case into the report"""
        return allure.testcase(url=url, name=name)

    @staticmethod
    def issue(url, name):
        """Inserts a issue to a test case into the report"""
        return allure.issue(url=url, name=name)

    # allure tags
    @staticmethod
    def feature(text: str):
        """Inserts a feature into the report"""
        return allure.feature(text)

    @staticmethod
    def title(text: str):
        """Inserts a title into the report"""
        return allure.title(text)

    @staticmethod
    def epic(text: str):
        """Inserts a epic into the report"""
        return allure.title(text)

    @staticmethod
    def story(text: str):
        """Inserts a story into the report"""
        return allure.title(text)

    # allure step
    @staticmethod
    def step(name: str):
        """Inserts a step into the report"""
        return allure.step(name)

    # other custom attachements
    @staticmethod
    def description(**kwargs):
        """Inserts a description into the report

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
    def request(data):
        """Inserts a info into the report

        Args:
            request (any): data
        """
        allure.attach(
            json.dumps(data), 'Request information', allure.attachment_type.JSON
        )

    @staticmethod
    def responce(responce: Response):
        """Inserts a info on responce in report. For example:
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
