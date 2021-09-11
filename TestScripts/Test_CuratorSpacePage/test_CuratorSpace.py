from FrameworkUtilities.teststatus_utility import test_Status
from PageObjects.LoginPage.login_page import LoginPage
from FrameworkUtilities.data_reader_utility import DataReader
import unittest
import pytest
import sys
import allure
from PageObjects.HomeNavigation.home_navigation import HomeNavigation
from PageObjects.CuratorSpace.curator_space import CuratorSpace
import FrameworkUtilities.logger_utility as log_utils
import logging
import time
import os


@pytest.mark.usefixtures("get_driver", "initialize")
@allure.story('Test Automation Demo ')
@allure.feature('Verification Using Requests')
class CuratorSpaceTest(unittest.TestCase):
    log = log_utils.custom_logger(logging.INFO)
    data_reader = DataReader()

    @pytest.fixture(scope='function')
    def initialize(self):
        self.homeNavigation = HomeNavigation(self.driver)
        self.loginPage = LoginPage(self.driver)
        self.CuratorSpacePage = CuratorSpace(self.driver)
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


    @allure.testcase("Verify addition of a Book to Meaning Constellation")
    @pytest.mark.smoke
    @allure.severity(allure.severity_level.MINOR)  # severity of the test case
    # @pytestrail.case('C1') # test case if on TestRail
    def test_VerifyAdditionOfABookToMeaningConstellation(self):
        test_name = sys._getframe().f_code.co_name
        self.log.info("###### TEST EXECUTION STARTED :: " + test_name + " ######")

        with allure.step('Login to the platform with Curator credentials'):
            self.homeNavigation.clickAcceptCoockiesButton()
            self.homeNavigation.clickUserProfileIcon()
            self.loginPage.login()
            time.sleep(10)
        with allure.step('Click on the top right menu option where a user can access their profile'):
            self.homeNavigation.clickUserProfileIcon()
            self.CuratorSpacePage.clickCuratorSpace()
            time.sleep(5)
            title=self.CuratorSpacePage.getManageConstellationPageTitle()
            if title=="MANAGE CONSTELLATION":
                self.CuratorSpacePage.clickAddNewConstellationButton()
                time.sleep(5)
                title=self.CuratorSpacePage.getAddNewConstellationTitle()
                if title == "ADD TO MEANING CONSTELLATION":
                    self.CuratorSpacePage.selectCategory(selector=1)
                    time.sleep(2)
                    self.CuratorSpacePage.enterTitleBox(data="dipankar")
                    element=self.CuratorSpacePage.getSaveButtonStatus().is_enabled()
                    self.log.info("Beforee enter Description Save button is enabled : " + str(element))
                    self.CuratorSpacePage.enterDescriptionBox(data="dipankar")
                    time.sleep(2)
                    element = self.CuratorSpacePage.getSaveButtonStatus().is_enabled()
                    self.log.info("After enter Description Save button is enabled : " + str(element))
                    l=os.getcwd() + "/sun.jpg"
                    self.log.info(l)
                    self.CuratorSpacePage.meaningSphereuploadImage(os.getcwd() + r'\sun.jpg')
                    time.sleep(5)
                    self.CuratorSpacePage.enterLinkUrl(data="www.google.com")
                    time.sleep(3)
                    element=self.CuratorSpacePage.getMeaningSphereRecommends()
                    self.CuratorSpacePage.ScrollToElements(element)
                    time.sleep(10)
                    self.CuratorSpacePage.clickSuggestedByArrow()
                    userList = self.CuratorSpacePage.getAllSuggestedByUserList()
                    for x in range(len(userList)):
                        self.log.info(" ".join(userList[x].text.split()))
                        if " ".join(userList[x].text.split()) == "Anna Weltner":
                            userList[x].click()
                            break
                    else:
                        self.log.info("user not present")
                    time.sleep(5)
                    self.CuratorSpacePage.enterMeaningSphereRecommends(data="dipankar")
                    self.CuratorSpacePage.clickSaveButton()
                    time.sleep(5)
                    message=self.CuratorSpacePage.getToastMessage()
                    self.log.info(message)
                    time.sleep(10)

                    title=self.CuratorSpacePage.getDetailsPageTitle()
                    self.CuratorSpacePage.verifyTextMatch(actualText=title,expectedText="Dipankar")
                    description=self.CuratorSpacePage.getDetailsPageDescription()
                    self.CuratorSpacePage.verifyTextMatch(actualText=description, expectedText="dipankar")
                    category=self.CuratorSpacePage.getDetailsPageCategory()
                    listofcategory=category.split(': ')
                    self.CuratorSpacePage.verifyTextMatch(actualText=listofcategory[1], expectedText="Book")
                    self.CuratorSpacePage.getDetailsPageRatingDisplayed()
                    self.CuratorSpacePage.clickDetailsPage()
                    time.sleep(3)
                    self.CuratorSpacePage.enterTitleBox(data="1")
                    time.sleep(2)
                    self.CuratorSpacePage.enterDescriptionBox(data="1")
                    time.sleep(2)
                    self.CuratorSpacePage.enterLinkUrl(data="1")

                    element = self.CuratorSpacePage.getMeaningSphereRecommends()
                    self.CuratorSpacePage.ScrollToElements(element)
                    time.sleep(2)
                    self.CuratorSpacePage.clickSuggestedByClearAll()
                    self.CuratorSpacePage.clickSuggestedByArrow()
                    userList = self.CuratorSpacePage.getAllSuggestedByUserList()
                    for x in range(len(userList)):
                        self.log.info(" ".join(userList[x].text.split()))
                        if " ".join(userList[x].text.split()) == "Anna Weltner":
                            userList[x].click()
                            break
                    else:
                        self.log.info("user not present")

                    time.sleep(5)
                    self.CuratorSpacePage.enterMeaningSphereRecommends(data="1")
                    self.CuratorSpacePage.clickSaveButton()
                    time.sleep(5)
                    message=self.CuratorSpacePage.getToastMessage()
                    self.log.info(message)


                    time.sleep(10)


                    title = self.CuratorSpacePage.getDetailsPageTitle()
                    self.CuratorSpacePage.verifyTextMatch(actualText=title, expectedText="Dipankar1")
                    description = self.CuratorSpacePage.getDetailsPageDescription()
                    self.CuratorSpacePage.verifyTextMatch(actualText=description, expectedText="dipankar1")
                    category = self.CuratorSpacePage.getDetailsPageCategory()
                    listofcategory = category.split(': ')
                    self.CuratorSpacePage.verifyTextMatch(actualText=listofcategory[1], expectedText="Book")
                    self.CuratorSpacePage.getDetailsPageRatingDisplayed()
                    self.CuratorSpacePage.clickDetailsPage()
                    time.sleep(4)
                    self.CuratorSpacePage.clickRemoveButton()
                    time.sleep(2)
                    self.CuratorSpacePage.clickYesRemoveButton()
                    time.sleep(4)
                    message = self.CuratorSpacePage.getToastMessage()
                    if message=="Constellation content removed successfully!":
                        self.log.info("Constellation content removed successfully!")
                    else:self.log.info("Unable to Remove Constellation Content!")
                    time.sleep(10)






