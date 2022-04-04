from setuptools import setup
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = pathlib.Path(here / 'README.md').read_text(encoding='utf-8')

setup(
    name="anna-api-test-framework",
    version="0.0.1",
    author="Evgenii Gerasin",
    author_email="e.d.gerasin@yandex.ru",
    description="Framework for rapid development of API tests and report generation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/EvgeniiGerasin/anna-api-framework",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Testing",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3 :: Only",
    ],
    keywords="sample, report, development, testing, api, framework",
    packages=["anna"],
    python_requires=">=3.7, <4",
    install_requires=[
        "pytest>=4.5.0",
        "allure-pytest",
        "requests",
    ],
    project_urls={  # Optional
        "Bug Reports": "https://github.com/EvgeniiGerasin/anna-api-framework/issues",
        "Source": "https://github.com/EvgeniiGerasin/anna-api-framework/tree/main/anna",
    },
)
