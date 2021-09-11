import FrameworkUtilities.logger_utility as log_utils
import logging
from HelperLibraries.basepage import BasePage


class MapOfMeaning(BasePage):
    log = log_utils.custom_logger(logging.INFO)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.MapOfMeaning_locators = self.pageLocators('MapOfMeaning')

    def clickTakeTheSurveyButton(self):
        self.elementClick(*self.locator(self.MapOfMeaning_locators, 'take_the_survey'))

    def clickContinueButton(self):
        self.elementClick(*self.locator(self.MapOfMeaning_locators, 'continue'))

    def clickNextButton(self):
        self.elementClick(*self.locator(self.MapOfMeaning_locators, 'next_Button'))

    def checkNextButtonStatus(self):
        element = self.getElement(*self.locator(self.MapOfMeaning_locators, 'next_Button'))
        return element

    def checkNextButtonisPresent(self):
        element = self.isElementPresent(*self.locator(self.MapOfMeaning_locators, 'next_Button'))
        return element


    def clickPreviousButton(self):
        self.elementClick(*self.locator(self.MapOfMeaning_locators, 'previous_Button'))

    def checkPreviousButtonStatus(self):
        element = self.getElement(*self.locator(self.MapOfMeaning_locators, 'previous_Button'))
        return element

    def clickSubmitButton(self):
        self.elementClick(*self.locator(self.MapOfMeaning_locators, 'submit_Button'))

    def checkSubmitButtoStatus(self):
        element = self.getElement(*self.locator(self.MapOfMeaning_locators, 'submit_Button'))
        return element

    def checkSubmitButtoisPresent(self):
        element = self.isElementPresent(*self.locator(self.MapOfMeaning_locators, 'submit_Button'))
        return element

    def clickRadioButton(self, radiobutton=""):
        if radiobutton == "Never/hardly ever":
            self.elementClick(*self.locator(self.MapOfMeaning_locators, 'never_hardly_radio_Button'))
        if radiobutton == "Seldom":
            self.elementClick(*self.locator(self.MapOfMeaning_locators, 'seldom_radio_Button'))
        if radiobutton == "Sometimes":
            self.elementClick(*self.locator(self.MapOfMeaning_locators, 'sometimes_radio_Button'))
        if radiobutton == "Often":
            self.elementClick(*self.locator(self.MapOfMeaning_locators, 'often_radio_Button'))
        if radiobutton == "Always/almost always":
            self.elementClick(*self.locator(self.MapOfMeaning_locators, 'always_almost_always_radio_Button'))
        if radiobutton == None:
            self.log.info("unable to click radio dutton")
