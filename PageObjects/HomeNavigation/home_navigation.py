import FrameworkUtilities.logger_utility as log_utils
import logging
from HelperLibraries.basepage import BasePage


class HomeNavigation(BasePage):
    log = log_utils.custom_logger(logging.INFO)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.homePage_locators = self.pageLocators('HomePage')

    def clickCrossCoockiesButton(self):
        self.elementClick(*self.locator(self.homePage_locators, 'CoockiesCrossButton'))

    def checkCrossCoockiesButtonDisplayed(self):
        return self.isElementDisplayed(*self.locator(self.homePage_locators, 'CoockiesCrossButton'))

    def clickAcceptCoockiesButton(self):
        self.elementClick(*self.locator(self.homePage_locators, 'CoockiesAcceptButton'))

    def checkAcceptCoockiesButtonDisplayed(self):
        return self.isElementDisplayed(*self.locator(self.homePage_locators, 'CoockiesAcceptButton'))

    def clickDeclineCoockiesButton(self):
        self.elementClick(*self.locator(self.homePage_locators, 'CoockiesDeclineButton'))

    def checkDeclineCoockiesButtonDisplayed(self):
        return self.isElementDisplayed(*self.locator(self.homePage_locators, 'CoockiesDeclineButton'))

    def clickUserProfileIcon(self):
        self.elementClick(*self.locator(self.homePage_locators, 'UserProfileIcon'))

    def clickMainToolNavDot(self):
        self.elementClick(*self.locator(self.homePage_locators,'mainToolNav'))

    def clickMyGuide(self):
        self.elementClick(*self.locator(self.homePage_locators, 'myGuide'))

    def clickMyMirror(self):
        self.elementClick(*self.locator(self.homePage_locators, 'myMirror'))

    def clickMapOfMeaning(self):
        self.elementClick(*self.locator(self.homePage_locators, 'mapOfMeaning'))


    def clickMeaningCircles(self):
        self.elementClick(*self.locator(self.homePage_locators, 'meaningCircles'))

    def clickMeaningNetwork(self):
        self.elementClick(*self.locator(self.homePage_locators, 'meaningNetwork'))

    def clickMeaningCommunities(self):
        self.elementClick(*self.locator(self.homePage_locators, 'meaningCommunities'))


    def clickMeaningConstellation(self):
        self.elementClick(*self.locator(self.homePage_locators, 'meaningConstellation'))



