from pytest import fixture


def pytest_addoption(parser):
    parser.addoption(
        '--api_key',
        action='store',
        help="Enter youre API key"
    )


@fixture(scope='function')
def user_params(request) -> object:

    api_key = request.config.getoption("api_key")
    yield api_key
