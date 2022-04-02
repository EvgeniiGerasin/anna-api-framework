import setuptools


setuptools.setup(
    name="anna-api-framework",
    version="0.0.5",
    author="Evgenii Gerasin",
    author_email="e.d.gerasin@yandex.ru",
    description="Framework for rapid development of API tests and report generation",
    packages=["anna"],
    long_description=open("README.md").read(),
    license=open("LICENSE.txt").read(),
    install_requires=[
        "requests==2.27.*",
        "pytest==7.1.*",
        "allure-pytest==2.9.*",
    ]
)
