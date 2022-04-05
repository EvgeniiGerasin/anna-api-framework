
# API TEST FRAMEWORK

Framework for rapid development of API tests and report generation

[![Supported Versions](https://img.shields.io/pypi/pyversions/anna-api-test-framework.svg)](https://pypi.org/project/anna-api-test-framework)


## Authors

- [@EvgeniiGerasin](https://github.com/EvgeniiGerasin)


## Features

- Rapid and straightforward development of tests using high-level methods
- Generating a report with test results in Allure
- The report will be useful for stakeholder


## Installation

Install my-project with pip:

```bash
  pip install anna-api-test-framework
```


    
## Usage/Examples

```python
from anna import Action, Report, Assert

@Report.epic('Simple tests')
@Report.story('Tests google')
@Report.testcase('https://www.google.com', 'Google')
@Report.link('https://www.google.com', 'Jast another link')
class TestExample:

    @Report.title('Simple test google')
    @Report.severity('CRITICAL')
    def test_simple_request(self):
        url = 'https://google.com'
        method = 'GET'
        want = 200 
        # insert discription of the test
        Report.description(url=url, method=method, other='other information')
        # doing request and geting response
        action = Action(url=url)
        response = action.request(method=method)
        got = response.status_code
        # checking response
        with Report.step('Checking response'):
            Assert.compare(
                variable_first=want,
                comparison_sign='==',
                variable_second=got,
                text_error='Response status code is not equal to expected'
            )

```

For run test and generat a report use following commands:

```bash
  pytest alluredir="./results"
```

For generat and open a report you need to install Allure and use the following commands:
```bash
  allure generate "./results" -c -o "./report"
  allure open "./report"
```
After that, the generated report will automatically open in your browser

![image](https://user-images.githubusercontent.com/50915575/161826281-19556784-f25d-45e0-88c9-14d819516cb6.png)

The report contains all the information you need

![image](https://user-images.githubusercontent.com/50915575/161826715-2c95e233-4741-4e1c-9cfe-d530cffa5f4a.png)



