import pytest
from HelperLibraries.webdriverfactory import WebDriverFactory


# @pytest.fixture()
# def setUp():
#     print("Running method level setUp")
#
#     yield
#     print("Running method level tearDown")


@pytest.fixture(scope="function")
def get_driver(request):
    print("Running class setUp")
    wdf = WebDriverFactory()
    driver = wdf.getWebDriverInstance()

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print("Running class tearDown")


# @pytest.fixture(scope="session")
# def oneTimeSetUp(request):
#     print("Running class setUp")
#     wdf = WebDriverFactory()
#     driver = wdf.getWebDriverInstance()
#
#     session = request.node
#     for item in session.items:
#         cls = item.getparent(pytest.Class)
#         setattr(cls.obj, "driver", driver)
#
#     yield driver
#
#     driver.quit()
#     print("Running class tearDown")

