import FrameworkUtilities.logger_utility as log_utils
import logging
from selenium.webdriver.common.by import By
from HelperLibraries.basepage import BasePage
import time


class MyMirror(BasePage):
    log = log_utils.custom_logger(logging.INFO)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.MyMirror_locators = self.pageLocators('MyMirror')


    def clickViewAnExampleButton(self):
        self.elementClick(*self.locator(self.MyMirror_locators, 'view_an_example'))
    def clickCrossButton(self):
        self.elementClick(*self.locator(self.MyMirror_locators, 'cross_button'))

    def clickAddAReflectionLink(self):
        self.elementClick(*self.locator(self.MyMirror_locators, 'add_a_Reflection_link'))

    def clickNextButton(self):
        self.elementClick(*self.locator(self.MyMirror_locators, 'next_Button'))
    def clickSubmitButton(self):
        self.elementClick(*self.locator(self.MyMirror_locators, 'submit_Button'))

    def checkNextButtonStatus(self):
        element=self.getElement(*self.locator(self.MyMirror_locators, 'next_Button'))
        return element
    def checkNextButtonisPresent(self):
        element = self.isElementPresent(*self.locator(self.MyMirror_locators, 'next_Button'))
        return element

    def checkSubmitButtonStatus(self):
        element=self.getElement(*self.locator(self.MyMirror_locators, 'submit_Button'))
        return element

    def checkSubmitButtoisPresent(self):
        element = self.isElementPresent(*self.locator(self.MyMirror_locators, 'submit_Button'))
        return element

    def checkPreviousButtonStatus(self):
        element = self.getElement(*self.locator(self.MyMirror_locators, 'previous_Button'))
        return element

    def feelingWordsList(self):
        element =self.getElementList(*self.locator(self.MyMirror_locators, 'feeling_words_list'))
        return element

    def topicsList(self):
        element =self.getElementList(*self.locator(self.MyMirror_locators, 'topics_list'))
        return element

    def addOnTextbox(self,data=""):
        self.sendKeys(data,*self.locator(self.MyMirror_locators,'textbox'))

    def addOnTextarea(self,data=""):
        self.sendKeys(data,*self.locator(self.MyMirror_locators,'headline'))

    def clickMyReflectionslink(self):
        self.elementClick(*self.locator(self.MyMirror_locators, 'my_Reflections_link'))

    def clickFirstReport(self):
        self.elementClick(*self.locator(self.MyMirror_locators, 'first_report'))

    def clickViewReflection(self):
        self.elementClick(*self.locator(self.MyMirror_locators, 'view_Reflection'))

    def clickThreeVerticalDotsLink(self):
        self.elementClick(*self.locator(self.MyMirror_locators, 'three_vertical_dots_link'))
    def clickCompleteReflectionLink(self):
        self.elementClick(*self.locator(self.MyMirror_locators, 'complete_reflection_link'))


    def checkViewReflectionLinkPresent(self):
        element = self.isElementPresent(*self.locator(self.MyMirror_locators, 'view_reflection_link'))
        return element
    def checkTagToTopicsLinkPresent(self):
        element = self.isElementPresent(*self.locator(self.MyMirror_locators, 'tag_to_topics_link'))
        return element

    def clickTagToTopicsLink(self):
        self.elementClick(*self.locator(self.MyMirror_locators, 'tag_to_topics_link'))

    def checkAddAnUpdateLinkPresent(self):
        element = self.isElementPresent(*self.locator(self.MyMirror_locators, 'add_an_update_link'))
        return element

    def clickAddAnUpdateLink(self):
        self.elementClick(*self.locator(self.MyMirror_locators, 'add_an_update_link'))
    def enterAddanupdatetoReflection(self,data):
        self.sendKeys(data, *self.locator(self.MyMirror_locators, 'add_an_update_to_Reflection'))



    def checkShareWithGuideLinkPresent(self):
        element = self.isElementPresent(*self.locator(self.MyMirror_locators, 'share_with_guide_link'))
        return element

    def getToastMessage(self):
        element = self.getText(*self.locator(self.MyMirror_locators, 'toast_message'))
        return element

    def getFeelingWordsCaptured(self):
        element = self.getText(*self.locator(self.MyMirror_locators, 'feeling_words_captured'))
        return element

    def clickSaveButton(self):
        self.elementClick(*self.locator(self.MyMirror_locators, 'save_button'))


    def checkWithDraftReflection(self):
        tab = self.driver.find_element(By.XPATH, "//div[@class='row ng-star-inserted']")
        for row in tab.find_elements_by_xpath("./div"):
            for td in row.find_elements_by_xpath("./div/div/div[2]"):
                l = td.text

                if l == 'In Progress':
                    self.log.info("Ability to save a draft reflection")
                else:
                    self.log.info("Ability to Not save a draft reflection--Fail")
            break

    def editInProgressReflection(self):
        tab = self.driver.find_element(By.XPATH, "//div[@class='row ng-star-inserted']")
        for row in tab.find_elements_by_xpath("./div"):
            for td in row.find_elements_by_xpath("./div/div/div[2]"):
                l = td.text

                if l == 'In Progress':
                    self.clickThreeVerticalDotsLink()
                    self.clickCompleteReflectionLink()


                else:
                    self.log.info("Unable to Edit draft reflection--Fail")
            break

    def editCompletedReflection(self):
        tab = self.driver.find_element(By.XPATH, "//div[@class='row ng-star-inserted']")
        for row in tab.find_elements_by_xpath("./div"):
            for td in row.find_elements_by_xpath("./div/div/div[2]"):
                l = td.text
                if l != 'In Progress':
                    self.clickThreeVerticalDotsLink()
                    self.checkViewReflectionLinkPresent()
                    self.checkTagToTopicsLinkPresent()
                    self.checkAddAnUpdateLinkPresent()
                    self.checkShareWithGuideLinkPresent()

                else:
                    self.log.info("Unable to Edit draft reflection--Fail")
            break




