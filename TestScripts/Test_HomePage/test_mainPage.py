import unittest
import pytest
import allure
from pytest_testrail.plugin import pytestrail

from PageObjects.HomeNavigation.home_navigation import HomeNavigation
from FrameworkUtilities.teststatus_utility import test_Status

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class test_main(unittest.TestCase):

    @allure.story('epic_1')
    @allure.severity(allure.severity_level.MINOR)
    #@pytestrail.case('C1')
    def test_CoockiesButton(self):
        self.homeNavigation = HomeNavigation(self.driver)
        self.ts = test_Status(self.driver)

        with allure.step('Verify Coockies Cross Button Displayed'):
            result=self.homeNavigation.checkCrossCoockiesButtonDisplayed()
            self.ts.mark(result,"Coockies Cross Button Not Displayed")

        with allure.step('Verify Coockies Accept Button Displayed'):
            result=self.homeNavigation.checkAcceptCoockiesButtonDisplayed()
            self.ts.mark(result,"Coockies Accept Button Not Displayed")

        with allure.step('Verify Coockies Decline Button Displayed'):
            result=self.homeNavigation.checkDeclineCoockiesButtonDisplayed()
            self.ts.mark(result,"Coockies Decline Button Not Displayed")

        with allure.step('Click Accept Coockies Button'):
            #self.homeNavigation.clickCrossCoockiesButton()
            self.homeNavigation.clickAcceptCoockiesButton()
            #self.homeNavigation.clickDeclineCoockiesButton()


    # @allure.story('epic_1')
    # @allure.severity(allure.severity_level.MINOR)
    # @pytestrail.case('C2')
    # def test_UserProfileIcon(self):
    #     self.homeNavigation = HomeNavigation(self.driver)
    #     self.ts = test_Status(self.driver)
    #     with allure.step('Accept Coockies Button'):
    #         self.homeNavigation.clickAcceptCoockiesButton()
    #     with allure.step('Click User Profile Icon'):
    #         self.homeNavigation.clickUserProfileIcon()
    #
    #
    # @allure.story('epic_1')
    # @allure.severity(allure.severity_level.MINOR)
    # #@pytestrail.case('C2')
    # def test_MainToolNavDot(self):
    #     self.homeNavigation = HomeNavigation(self.driver)
    #     self.ts = test_Status(self.driver)
    #     with allure.step('Accept Coockies Button'):
    #         self.homeNavigation.clickAcceptCoockiesButton()
    #     with allure.step("Click Main Tool Nav Dot"):
    #         self.homeNavigation.clickMainToolNavDot()