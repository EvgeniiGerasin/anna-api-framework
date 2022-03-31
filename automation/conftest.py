

def pytest_addoption(parser):
    
    parser.addoption(
        '--id',
        action='store',
        default='',
        help="Enter id"
    )


