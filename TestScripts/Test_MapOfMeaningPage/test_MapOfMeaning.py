from FrameworkUtilities.teststatus_utility import test_Status
from PageObjects.LoginPage.login_page import LoginPage
from FrameworkUtilities.data_reader_utility import DataReader
import unittest
import pytest
import sys
import allure
from PageObjects.HomeNavigation.home_navigation import HomeNavigation
from PageObjects.MapOfMeaning.map_of_meaning_page import MapOfMeaning
import FrameworkUtilities.logger_utility as log_utils
import logging
import time


@pytest.mark.usefixtures("get_driver","initialize")
@allure.story('Test Automation Demo ')
@allure.feature('Verification Using Requests')
class MapOfMeningTest(unittest.TestCase):

    log = log_utils.custom_logger(logging.INFO)
    data_reader = DataReader()

    @pytest.fixture(scope='function')
    def initialize(self):
        self.homeNavigation = HomeNavigation(self.driver)
        self.loginPage = LoginPage(self.driver)
        self.MapOfMeaningPage=MapOfMeaning(self.driver)
        self.ts = test_Status(self.driver)

        def cleanup():
            self.driver.delete_all_cookies()

        yield
        cleanup()


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
    @allure.severity(allure.severity_level.MINOR)  # severity of the test case
    # @pytestrail.case('C1') # test case if on TestRail
    def test_login_successfully(self):

        test_name = sys._getframe().f_code.co_name
        self.log.info("###### TEST EXECUTION STARTED :: " + test_name + " ######")

        with allure.step('Navigate to login page'):
            self.homeNavigation.clickAcceptCoockiesButton()
            self.homeNavigation.clickUserProfileIcon()
            self.loginPage.login("admin@meaningsphere.com","Ab1234567@")
            time.sleep(10)
        with allure.step('Navigate to MapOfMeaning page'):
            self.homeNavigation.clickMainToolNavDot()
            self.homeNavigation.clickMapOfMeaning()
            self.MapOfMeaningPage.clickTakeTheSurveyButton()
            time.sleep(10)
            self.MapOfMeaningPage.clickContinueButton()
            time.sleep(10)

        for i in range(1,32):
            self.MapOfMeaningPage.clickRadioButton(radiobutton="Seldom")
            time.sleep(5)
            if self.MapOfMeaningPage.checkNextButtonisPresent()==True:
                if self.MapOfMeaningPage.checkNextButtonStatus().is_enabled():
                    self.MapOfMeaningPage.clickNextButton()
            elif self.MapOfMeaningPage.checkSubmitButtoisPresent()==True:
                    if self.MapOfMeaningPage.checkSubmitButtoStatus().is_enabled():
                        self.MapOfMeaningPage.clickSubmitButton()

            else:
                self.log.info("Next button and Submit button not present")
            time.sleep(10)





    if __name__ == '__main__':
        unittest.main(verbosity=2)


