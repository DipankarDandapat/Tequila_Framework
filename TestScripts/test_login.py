from FrameworkUtilities.teststatus_utility import test_Status
from PageObjects.LoginPage.login_page import LoginPage
from FrameworkUtilities.data_reader_utility import DataReader
import unittest
import pytest
import sys
import allure
from PageObjects.HomeNavigation.home_navigation import HomeNavigation
import FrameworkUtilities.logger_utility as log_utils
import logging
import time


@pytest.mark.usefixtures("get_driver","initialize")
@allure.story('Test Automation Demo ')
@allure.feature('Verification Using Requests')
class LoginTest(unittest.TestCase):

    log = log_utils.custom_logger(logging.INFO)
    data_reader = DataReader()

    @pytest.fixture(scope='function')
    def initialize(self):
        self.homeNavigation = HomeNavigation(self.driver)
        self.loginPage = LoginPage(self.driver)
        self.loggedInPage = LoggedInPage(self.driver)
        self.ts = test_Status(self.driver)

        def cleanup():
            self.driver.delete_all_cookies()

        yield
        cleanup()

    # @pytest.fixture(autouse=True)
    # def classSetup(self):
    #     self.homeNavigation = HomeNavigation(self.driver)
    #     self.loginPage = LoginPage(self.driver)
    #     self.loggedInPage = LoggedInPage(self.driver)
    #     self.ts = test_Status(self.driver)

    # @pytest.fixture(scope="function")
    # def setUp(self):
    #     self.homeNavigation = HomeNavigation(self.driver)
    #     self.loginPage = LoginPage(self.driver)
    #     self.loggedInPage = LoggedInPage(self.driver)
    #     self.ts = test_Status(self.driver)

    @pytest.fixture(autouse=True)
    def class_level_setup(self, request):
        """
        This method is used for one time setup of test execution process.
        :return: it returns nothing
        """

        if self.data_reader.get_data(request.function.__name__, "Runmode") != "Y":
            pytest.skip("Excluded from current execution run.")


    @allure.testcase("test_login_successfully")
    @pytest.mark.smoke
    @allure.severity(allure.severity_level.MINOR) # severity of the test case
    #@pytestrail.case('C1') # test case if on TestRail
    def test_login_successfully(self):

        # self.homeNavigation = HomeNavigation(self.driver)
        # self.loginPage = LoginPage(self.driver)
        # self.loggedInPage = LoggedInPage(self.driver)
        # self.ts = test_Status(self.driver)

        test_name = sys._getframe().f_code.co_name
        self.log.info("###### TEST EXECUTION STARTED :: " + test_name + " ######")

        with allure.step('Navigate to login page'):

            self.homeNavigation.clickCrossCoockiesButton()
            self.homeNavigation.goToLoginPage()
            #self.ts.markFinal(self.loginPage.isAt, "navigation to login page failed")

        with allure.step('Login'):
            r1=self.loginPage.is_emailbox_presece()
            self.ts.mark(test_step="Login", result=r1)


            r2 = self.loginPage.is_passwordbox_presece()

            self.loginPage.login(email="admin@meaningsphere.com", password="Ab1234567@")

            time.sleep(10)

            self.ts.mark_final(result=r2, test_step=test_name)

            #self.ts.markFinal(self.loggedInPage.isAt, "login failed")

    # @allure.testcase("test_login_successfully2")
    # @allure.severity(allure.severity_level.MINOR)  # severity of the test case
    # @pytest.mark.regression
    # def test_login_successfully2(self):
    #     # self.homeNavigation = HomeNavigation(self.driver)
    #     # self.loginPage = LoginPage(self.driver)
    #     # self.loggedInPage = LoggedInPage(self.driver)
    #     # self.ts = test_Status(self.driver)
    #
    #     with allure.step('Navigate to login page'):
    #         self.homeNavigation.clickCrossCoockiesButton()
    #         self.homeNavigation.goToLoginPage()
    #         #self.ts.markFinal(self.loginPage.isAt, "navigation to login page failed")
    #
    #     with allure.step('Login'):
    #         self.loginPage.login(email="admin@meaningsphere.com", password="Ab1234567@")
    #         #self.loginPage.login(email=td.testData("email"), password=td.testData("password"))
    #         #self.ts.markFinal(self.loggedInPage.isAt, "login failed")
    #
    # @allure.story('epic_1')  # epic/story of the test case
    # @allure.severity(allure.severity_level.MINOR)  # severity of the test case
    # def test_login_successfully3(self):
    #     #self.homeNavigation = HomeNavigation(self.driver)
    #     self.loginPage = LoginPage(self.driver)
    #     self.loggedInPage = LoggedInPage(self.driver)
    #     self.ts = test_Status(self.driver)
    #
    #     with allure.step('Navigate to login page'):
    #         self.homeNavigation.goToLoginPage()

    if __name__ == '__main__':
        unittest.main(verbosity=2)