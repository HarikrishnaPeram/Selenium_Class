import  pytest

@pytest.fixture()

def setUp():

    print("Running Method Level setUp")
    yield
    print("Running method level teardown")

@pytest.fixture(scope="class")

def OnlineTimeSetup(request, browser):
    print("running one time setup")

    if browser == 'Chrome':
        value = 10
        print("Running Test on cc")

    else:
        value=20
        print("Running Test on Chrome")
    if request.cls is  not None:
        request.cls.value = value

    yield  value
    print("Running one time tear down")

def pytest_addoption(parser):
    parser.addoption("--browser--")
    parser.addoption("--osType", help="Type of operating system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser--")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")

