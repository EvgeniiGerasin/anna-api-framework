import json
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
        return allure.epic(text)

    @staticmethod
    def story(text: str):
        """Inserts a story into the report"""
        return allure.story(text)

    # allure step
    @staticmethod
    def step(name: str):
        """Inserts a step into the report"""
        return allure.step(name)

    # other custom attachments
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
        """Inserts additional info into the report

        Args:
            data: Any
        """
        allure.attach(
            json.dumps(data), 'Request information', allure.attachment_type.JSON
        )

    @staticmethod
    def response(response: Response):
        """Inserts additional info on response in report. For example:
        body, headers, cookies, status code

        Args:
            response: Response
        """
        allure.attach(
            f'{response.request.method}',
            'Request method',
            allure.attachment_type.TEXT
        )
        allure.attach(
            f'{response.request.body}',
            'Request body',
            allure.attachment_type.TEXT
        )
        allure.attach(
            f'{response.request.headers}',
            'Request header',
            allure.attachment_type.TEXT
        )
        allure.attach(
            f'{response.request.url}',
            'Request url',
            allure.attachment_type.TEXT
        )
        allure.attach(
            f'{response.status_code}',
            'Response status code',
            allure.attachment_type.TEXT
        )
        allure.attach(
            '{}'.format(response.text.replace('\'', '""')),
            'Response body',
            allure.attachment_type.JSON
        )
        allure.attach(
            f'{response.headers}',
            'Response headers',
            allure.attachment_type.TEXT
        )
        allure.attach(
            f'{response.cookies}',
            'Response cookies',
            allure.attachment_type.TEXT
        )
