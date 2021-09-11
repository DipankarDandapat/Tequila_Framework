from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import *
import FrameworkUtilities.logger_utility as log_utils
import logging
import time
import os
import json
import traceback
import allure


def readJson(jsonFilePath):
    with open(jsonFilePath) as f:
        jsonFile = json.load(f)

    return jsonFile


class SeleniumDriver(object):
    log = log_utils.custom_logger(logging.INFO)

    def __init__(self, driver):
        self.driver = driver

    def pageLocators(self, page):
        """
        read the Locators of specific page
        :param page: page
        :return: list of all Locators in specific page
        """
        self.cur_path = os.path.abspath(os.path.dirname(__file__))
        self.locatorsPath = os.path.join(self.cur_path, r"../Locators/locators.json")
        locatorsJsonFile = readJson(self.locatorsPath)
        pageLocators = [locator for locator in locatorsJsonFile if locator['pageName'] in page]
        return pageLocators

    def locator(self, pageLocators, locatorName):
        """
        get specific locator in specific page
        :param pageLocators: specific page
        :param locatorName: locator name
        :return: locator and locator Type
        """
        for locator in pageLocators:
            if locatorName == locator['name']:
                return locator['locator'], locator['locateUsing']

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        else:
            self.log.info("Locator type" + locatorType + "not correct/supported")
        return False

    def sleep(self, sec, info=""):
        """
        Put the program to wait for the specified amount of time
        """
        if info is not None:
            self.log.info("Wait :: " + str(sec) + " seconds for " + info)
            try:
                time.sleep(sec)
            except:
                traceback.print_stack()

    def dropdownSelectElement(self,selector, locator, locatorType="id", selectorType="value",):
        try:
            element = self.getElement(locator, locatorType)
            sel = Select(element)
            if selectorType == "value":
                sel.select_by_value(selector)
                time.sleep(1)
            elif selectorType == "index":
                sel.select_by_index(selector)
                time.sleep(1)
            elif selectorType == "text":
                sel.select_by_visible_text(selector)
                time.sleep(1)
            self.log.info("Element selected with selector: " + str(selector) + " and selectorType: " + selectorType)

        except:
            self.log.error(
                "Element not selected with selector: " + str(selector) + " and selectorType: " + selectorType)
            print_stack()

    def getDropdownOptionsCount(self, locator, locatorType="id"):
        '''
        get the number of options of drop down list
        :return: number of Options of drop down list
        '''
        options = None
        try:
            element = self.getElement(locator, locatorType)
            sel = Select(element)
            options = sel.options
            self.log.info("Element found with locator: " + locator + " and locatorType: " + locatorType)
        except:
            self.log.error("Element not found with locator: " + locator + " and locatorType: " + locatorType)

        return options

    def getDropdownSelectedOptionText(self, locator, locatorType="id"):
        '''
        get the text of selected option in drop down list
        :return: the text of selected option in drop down list
        '''
        selectedOption_text = None
        try:
            element = self.getElement(locator, locatorType)
            sel = Select(element)
            selectedOption_text = sel.first_selected_option.text
            self.log.info(
                "Return the selected option of drop down list with locator: " + locator + " and locatorType: " + locatorType)
        except:
            self.log.error(
                "Can not return the selected option of drop down list with locator: " + locator + " and locatorType: " + locatorType)

        return selectedOption_text

    def getDropdownSelectedOptionValue(self, locator, locatorType="id"):
        '''
        get the value of selected option in drop down list
        :return: the value of selected option in drop down list
        '''
        selectedOption_value = None
        try:
            element = self.getElement(locator, locatorType)
            sel = Select(element)
            selectedOption_value = sel.first_selected_option.get_attribute("value")
            self.log.info(
                "Return the selected option of drop down list with locator: " + locator + " and locatorType: " + locatorType)
        except:
            self.log.error(
                "Can not return the selected option of drop down list with locator: " + locator + " and locatorType: " + locatorType)

        return selectedOption_value

    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info("Element found with locator: " + locator + " and locatorType: " + locatorType)
        except:
            self.log.error("Element not found with locator: " + locator + " and locatorType: " + locatorType)
        return element

    def isElementSelected(self, locator, locatorType):
        isSelected = None
        try:
            element = self.getElement(locator, locatorType)
            isSelected = element.is_selected()
            self.log.info("Element found with locator: " + locator + " and locatorType: " + locatorType)
        except:
            self.log.error("Element not found with locator: " + locator + " and locatorType: " + locatorType)

        return isSelected

    def getElementList(self, locator, locatorType="id"):
        """
        Get list of elements
        """
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_elements(byType, locator)
            self.log.info("Element list found with locator: " + locator + " and locatorType: " + locatorType)
        except:
            self.log.error("Element list not found with locator: " + locator + " and locatorType: " + locatorType)

        return element

    def elementClick(self, locator="", locatorType="xpath", element=None):
        """
        Either provide element or a combination of locator and locatorType
        """

        try:
            if locator:
                element = self.getElement(locator, locatorType)
            element.click()
            self.log.info("clicked on element with locator: " + locator + " locatorType: " + locatorType)
        except:
            self.log.error("cannot click on the element with locator: " + locator + " locatorType: " + locatorType)
            print_stack()

    def elementHover(self, locator="", locatorType="id", element=None):
        """
        Either provide element or a combination of locator and locatorType
        """

        try:
            if locator:
                element = self.getElement(locator, locatorType)
            hover = ActionChains(self.driver).move_to_element(element)
            hover.perform()
            time.sleep(2)
            self.log.info("hover to element with locator: " + locator + " locatorType: " + locatorType)
        except:
            self.log.error("cannot hover to the element with locator: " + locator + " locatorType: " + locatorType)
            print_stack()

    def sendKeys(self, data, locator="", locatorType="id", element=None):
        """
        Send keys to an element
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            element.send_keys(data)
            self.log.info("send data on element with locator: " + locator + " locatorType: " + locatorType)
        except:
            self.log.error("cannot send data on the element with locator: " + locator + " locatorType: " + locatorType)
            print_stack()

    def clearKeys(self, locator="", locatorType="id", element=None):
        """
        Clear keys of an element
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            element.clear()
            self.log.info("Clear data of element with locator: " + locator + " locatorType: " + locatorType)
        except:
            self.log.error("cannot clear data of the element with locator: " + locator + " locatorType: " + locatorType)
            print_stack()

    def getText(self, locator="", locatorType="id", element=None, info=""):
        """
        Get 'Text' on an element
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:
                self.log.debug("In locator condition")
                element = self.getElement(locator, locatorType)
            self.log.debug("Before finding text")
            text = element.text
            self.log.debug("After finding element, size is: " + str(len(text)))
            if len(text) == 0:
                text = element.get_attribute("innerText")
            if len(text) != 0:
                self.log.info("Getting text on element The text is :: '" + text + "'")
                text = text.strip()
        except:
            self.log.error("Failed to get text on element " + info)
            print_stack()
            text = None
        return text

    def isElementPresent(self, locator="", locatorType="id", element=None):
        """
        Check if element is present
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            if element is not None:
                self.log.info("Element found with locator: " + locator + " and locatorType: " + locatorType)
                return True
            else:
                self.log.error("Element not found with locator: " + locator + " and locatorType: " + locatorType)
                return False
        except:
            self.log.error("Element not found with locator: " + locator + " and locatorType: " + locatorType)
            return False

    def isElementDisplayed(self, locator="", locatorType="id", element=None):
        """
        Check if element is displayed
        Either provide element or a combination of locator and locatorType
        """
        isDisplayed = False
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            if element is not None:
                isDisplayed = element.is_displayed()
                self.log.info("Element is displayed with locator: " + locator + " and locatorType: " + locatorType)
            else:
                self.log.error("Element is not displayed with locator: " + locator + " and locatorType: " + locatorType)
            return isDisplayed
        except:
            self.log.error("Element is not displayed with locator: " + locator + " and locatorType: " + locatorType)
            return False

    def elementPresenceCheck(self, locator="", locatorType="id"):
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            elementList = self.driver.find_elements(byType, locator)
            if len(elementList) > 0:
                self.log.info(
                    "Element present with locator_properties: " + locator + " and locator_type: " + locatorType)
                return True
            else:
                self.log.error(
                    "Element not present with locator_properties: " + locator + " and locator_type: " + locatorType)
                return False
        except:
            self.log.error("Exception occurred during element identification.")
            return False

    def waitForElement(self, locator, locatorType='id', timeout=10, pollFrequency=0.5):
        element = None
        try:
            self.log.info("Waiting for maximum :: " + str(timeout) + " :: seconds for element to be clickable")

            wait = WebDriverWait(self.driver, timeout, poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            ByType = self.getByType(locatorType)
            element = wait.until(EC.element_to_be_clickable((ByType, locator)))

            self.log.info("Element appeared on the web page")

        except:
            self.log.info("Element not appeared on the web page")
            print_stack()

        return element

    def webScroll(self, direction="up"):
        if direction == "up":
            # Scroll Up
            self.driver.execute_script("window.scrollBy(0, -1000);")
        if direction == "down":
            # Scroll Down
            self.driver.execute_script("window.scrollBy(0, 1000);")

    def getTitle(self):
        return self.driver.title

    def getURL(self):
        '''
        Get the current URL
        :return: current URL
        '''
        currentURL = self.driver.current_url
        return currentURL

    def pageBack(self):
        '''page back the browser'''
        self.driver.execute_script("window.history.go(-1)")

    def refresh(self):
        self.driver.get(self.driver.current_url)

    def getAttributeValue(self, locator="", locatorType="id", element=None, attribute=""):
        '''
        get attribute value
        '''
        try:
            if locator:
                self.log.debug("In locator condition")
                element = self.getElement(locator, locatorType)
            attribute_value = element.get_attribute(attribute)
        except:
            self.log.error(
                "Failed to get " + attribute + " in element with locator: " + locator + " and locatorType: " + locatorType)
            print_stack()
            attribute_value = None
        return attribute_value

    def take_screenshots(self, file_name_initials):

        """
        This method takes screen shot for reporting
        :param file_name_initials: it takes the initials for file name
        :return: it returns the destination directory of screenshot
        """

        file_name = file_name_initials + "." + str(round(time.time() * 1000)) + ".png"
        cur_path = os.path.abspath(os.path.dirname(__file__))
        screenshot_directory = os.path.join(cur_path, r"../Logs/Screenshots/")

        destination_directory = os.path.join(screenshot_directory, file_name)

        try:
            if not os.path.exists(screenshot_directory):
                os.makedirs(screenshot_directory)

            self.driver.save_screenshot(destination_directory)
            self.log.info("Screenshot saved to directory: " + destination_directory)
        except Exception as ex:
            self.log.error("### Exception occurred:: ", ex)
            print_stack()

        return destination_directory

    def page_has_loaded(self):
        try:
            WebDriverWait(self.driver, 1000, poll_frequency=0.5).until(
                lambda driver: self.driver.execute_script('return document.readyState == "complete";'))
            WebDriverWait(self.driver, 1000, poll_frequency=0.5).until(
                lambda driver: self.driver.execute_script('return jQuery.active == 0'))
            WebDriverWait(self.driver, 1000, poll_frequency=0.5).until(
                lambda driver: self.driver.execute_script('return typeof jQuery != "undefined"'))
            WebDriverWait(self.driver, 1000, poll_frequency=0.5).until(lambda driver: self.driver.execute_script(
                'return angular.element(document).injector().get("$http").pendingRequests.length === 0'))
        except:
            return False

    def verifyListMatch(self, expectedList, actualList):
        """
        Verify two list matches

        :param expectedList: Expected List
        :param actualList: Actual List
        """
        return set(expectedList) == set(actualList)

    def verifyListContains(self, expectedList, actualList):
        """
        Verify actual list contains elements of expected list

        :param expectedList: Expected List
        :param actualList: Actual List
        """
        length = len(expectedList)
        for i in range(0, length):
            if expectedList[i] not in actualList:
                return False
        else:
            return True

    def verifyTextContains(self, actualText, expectedText):
        """
        verify actual text contains expected text string

        :param actualText: Actual Text
        :param expectedText: Expected Text
        """
        self.log.info("Actual Text From Application Web UI --> :: " + actualText)
        self.log.info("Expected Text From Application Web UI --> :: " + expectedText)

        if expectedText.lower() in actualText.lower():
            self.log.info("### VERIFICATIONS CONTAINS !!!")
            return True
        else:
            self.log.error("### VERIFICATIONS DOES NOT CONTAINS !!!")

    def verifyTextMatch(self, actualText, expectedText):
        """
        verify text match

        :param actualText: Actual Text
        :param expectedText: Expected Text
        """
        self.log.info("Actual Text From Application Web UI --> :: " + actualText)
        self.log.info("Expected Text From Application Web UI --> :: " + expectedText)
        if expectedText.lower() == actualText.lower():
            self.log.info("### VERIFICATIONS MATCHED !!!")
            return True
        else:
            self.log.error("### VERIFICATIONS DOES NOT MATCHED !!!")

    def verifyPageTitle(self, titleToVerify):
        """
        Verify the page Title

        :param titleToVerify: Title on the page that needs to be verified
        """
        try:
            actualTitle = self.getTitle()
            return self.verifyTextContains(actualTitle, titleToVerify)
        except:
            self.log.error("Failed to get page title")
            print_stack()
            return False
