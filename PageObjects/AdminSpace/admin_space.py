import FrameworkUtilities.logger_utility as log_utils
from HelperLibraries.basepage import BasePage
from selenium.webdriver.common.keys import Keys
import logging
from selenium.webdriver.common.by import By


class AdminSpace(BasePage):
    log = log_utils.custom_logger(logging.INFO)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.AdminSpace_locators = self.pageLocators('AdminSpace')

    def clickAdminSpaceLink(self):
        self.elementClick(*self.locator(self.AdminSpace_locators, 'adminSpace_link'))
    def checkAdminSpaceLinkPresent(self):
        element = self.isElementPresent(*self.locator(self.AdminSpace_locators, 'adminSpace_link'))
        return element

    def checkManageExplorersPageheaderLabelPresent(self):
        element = self.isElementPresent(*self.locator(self.AdminSpace_locators, 'manageExplorers_page_header_label'))
        return element

    def clickManageGuidesLink(self):
        self.elementClick(*self.locator(self.AdminSpace_locators, 'manageGuides_link'))

    def checkManageGuidesPageheaderLabelPresent(self):
        element = self.isElementPresent(*self.locator(self.AdminSpace_locators, 'manageGuides_page_header_label'))
        return element

    def clickAddExplorersButton(self):
        self.elementClick(*self.locator(self.AdminSpace_locators, 'add_explorers_button'))

    def checkAddExplorersPageheaderLabelPresent(self):
        element = self.isElementPresent(*self.locator(self.AdminSpace_locators, 'add_explorers_page_header_label'))
        return element

    def enterAddExplorersFirstName(self, data=''):
        self.sendKeys(data, *self.locator(self.AdminSpace_locators, 'add_explorers_firstName'))

    def enterAddExplorersLastName(self, data=''):
        self.sendKeys(data, *self.locator(self.AdminSpace_locators, 'add_explorers_lastName'))

    def enterAddExplorersEmail(self, data=''):
        self.sendKeys(data, *self.locator(self.AdminSpace_locators, 'add_explorers_email'))

    def clickAsAGuideYesRadioButton(self):
        self.elementClick(*self.locator(self.AdminSpace_locators, 'add_explorers_as_a_guide_Yes'))

    def clickAsAGuideNoRadioButton(self):
        self.elementClick(*self.locator(self.AdminSpace_locators, 'add_explorers_as_a_guide_No'))

    def clickAsACuratorYesRadioButton(self):
        self.elementClick(*self.locator(self.AdminSpace_locators, 'add_explorers_as_a_curator_Yes'))

    def clickAsACuratorNoRadioButton(self):
        self.elementClick(*self.locator(self.AdminSpace_locators, 'add_explorers_as_a_curator_No'))

    def clickAsAAdministratorYesRadioButton(self):
        self.elementClick(*self.locator(self.AdminSpace_locators, 'add_explorers_as_a_administrator_Yes'))

    def clickAsAAdministratorNoRadioButton(self):
        self.elementClick(*self.locator(self.AdminSpace_locators, 'add_explorers_as_a_administrator_No'))

    def clickSaveButton(self):
        self.elementClick(*self.locator(self.AdminSpace_locators, 'save_button'))

    def getSaveButtonStatus(self):
        element = self.getElement(*self.locator(self.AdminSpace_locators, 'save_button'))
        return element.is_enabled()

    def enterSearchBox(self, data=''):
        element = self.getElement(*self.locator(self.AdminSpace_locators, 'search_box'))
        element.clear()
        element.send_keys(data)
        element.send_keys(Keys.ENTER)

    def clearSearchBox(self):
        self.clearKeys(*self.locator(self.AdminSpace_locators, 'search_box'))

    def clickThreeVerticalDotsLink(self):
        self.elementClick(*self.locator(self.AdminSpace_locators, 'three_vertical_dots_link'))

    def checkAdminIconPresent(self):
        element = self.isElementPresent(*self.locator(self.AdminSpace_locators, 'admin_icon'))
        return element

    def checkCuratorIconPresent(self):
        element = self.isElementPresent(*self.locator(self.AdminSpace_locators, 'curator_icon'))
        return element

    def checkGuideIconPresent(self):
        element = self.isElementPresent(*self.locator(self.AdminSpace_locators, 'guide_icon'))
        return element

    def checkViewProfileLinkPresent(self):
        element = self.isElementPresent(*self.locator(self.AdminSpace_locators, 'view_profile_link'))
        return element

    def clickViewProfileLink(self):
        self.elementClick(*self.locator(self.AdminSpace_locators, 'view_profile_link'))

    def checkEditProfileLinkPresent(self):
        element = self.isElementPresent(*self.locator(self.AdminSpace_locators, 'edit_profile_link'))
        return element

    def clickEditProfileLink(self):
        self.elementClick(*self.locator(self.AdminSpace_locators, 'edit_profile_link'))

    def checkAddAsCuratorLinkPresent(self):
        element = self.isElementPresent(*self.locator(self.AdminSpace_locators, 'add_as_curator_link'))
        return element

    def clickAddAsCuratorLink(self):
        self.elementClick(*self.locator(self.AdminSpace_locators, 'add_as_curator_link'))

    def checkRemoveAsCuratorLinkPresent(self):
        element = self.isElementPresent(*self.locator(self.AdminSpace_locators, 'remove_as_curator_link'))
        return element

    def clickRemoveAsCuratorLink(self):
        self.elementClick(*self.locator(self.AdminSpace_locators, 'remove_as_curator_link'))

    def addRemark(self, data):
        self.sendKeys(data, *self.locator(self.AdminSpace_locators, 'remarks'))

    def clickIConfirmThisChangeCheckbox(self):
        self.elementClick(*self.locator(self.AdminSpace_locators, 'i_confirm_this_change_checkbox'))

    def checkAddAsAdminLinkPresent(self):
        element = self.isElementPresent(*self.locator(self.AdminSpace_locators, 'add_as_admin_link'))
        return element

    def checkRemoveAsAdminLinkPresent(self):
        element = self.isElementPresent(*self.locator(self.AdminSpace_locators, 'remove_as_admin_link'))
        return element

    def clickAddAsAdminLink(self):
        self.elementClick(*self.locator(self.AdminSpace_locators, 'add_as_admin_link'))

    def clickRemoveAsAdminLink(self):
        self.elementClick(*self.locator(self.AdminSpace_locators, 'remove_as_admin_link'))

    def checkAddAsGuideLinkPresent(self):
        element = self.isElementPresent(*self.locator(self.AdminSpace_locators, 'add_as_guide_link'))
        return element

    def checkRemoveAsGuideLinkPresent(self):
        element = self.isElementPresent(*self.locator(self.AdminSpace_locators, 'remove_as_guide_link'))
        return element

    def clickAddAsGuideLink(self):
        self.elementClick(*self.locator(self.AdminSpace_locators, 'add_as_guide_link'))

    def clickRemoveAsGuideLink(self):
        self.elementClick(*self.locator(self.AdminSpace_locators, 'remove_as_guide_link'))

    def checkLockExplorerLinkPresent(self):
        element = self.isElementPresent(*self.locator(self.AdminSpace_locators, 'lock_explorer_link'))
        return element

    def clickLockExplorerLink(self):
        self.elementClick(*self.locator(self.AdminSpace_locators, 'lock_explorer_link'))

    def checkUnlockExplorerLinkPresent(self):
        element = self.isElementPresent(*self.locator(self.AdminSpace_locators, 'unlock_explorer_link'))
        return element

    def clickUnlockExplorerLink(self):
        self.elementClick(*self.locator(self.AdminSpace_locators, 'unlock_explorer_link'))

    def checkViewAccountActivityLinkPresent(self):
        element = self.isElementPresent(*self.locator(self.AdminSpace_locators, 'view_account_activity_link'))
        return element

    def clickViewAccountActivityLink(self):
        self.elementClick(*self.locator(self.AdminSpace_locators, 'view_account_activity_link'))

    def checkViewAccountActivityPageHeaderPresent(self):
        element = self.isElementPresent(*self.locator(self.AdminSpace_locators, 'view_account_activity_page_header'))
        return element

    def getViewAccountActivityType(self):
        element = self.getText(*self.locator(self.AdminSpace_locators, 'view_account_activity_type'))
        return element

    def getViewAccountActivityRemark(self):
        element = self.getText(*self.locator(self.AdminSpace_locators, 'view_account_activity_remarks'))
        return element

    def checkPasswordResetLinkPresent(self):
        element = self.isElementPresent(*self.locator(self.AdminSpace_locators, 'password_reset_link'))
        return element

    def clickPasswordResetLink(self):
        self.elementClick(*self.locator(self.AdminSpace_locators, 'password_reset_link'))

    def getAllUserTitle(self):
        element = self.getElementList(*self.locator(self.AdminSpace_locators, 'get_all_user_title'))
        return element

    def getExplorerSince(self):
        element = self.getText(*self.locator(self.AdminSpace_locators, 'explorer_since'))
        return element

    def getToastMessage(self):
        element = self.getText(*self.locator(self.AdminSpace_locators, 'toast_message'))
        return element

    def checkNoDataFoundMessagePresent(self):
        element = self.isElementPresent(*self.locator(self.AdminSpace_locators, 'no_data_found_message'))
        return element

    def clickFilterLink(self):
        self.elementClick(*self.locator(self.AdminSpace_locators, 'filter'))

    def clickDismissFilter(self):
        self.elementClick(*self.locator(self.AdminSpace_locators, 'dismiss_filter'))

    def clickFilterResetButton(self):
        self.elementClick(*self.locator(self.AdminSpace_locators, 'filter_reset'))

    def clickFilterGoButton(self):
        self.elementClick(*self.locator(self.AdminSpace_locators, 'filter_go_button'))

    def clickFilterisLockedCheckbox(self):
        self.elementClick(*self.locator(self.AdminSpace_locators, 'filter_isLocked_checkbox'))

    def checkFilterisLockedCheckboxStatus(self):
        elements = self.getElement(*self.locator(self.AdminSpace_locators, 'filter_isLocked_checkbox_status'))
        return elements.is_selected()

    def clickFilterisInactiveCheckbox(self):
        self.elementClick(*self.locator(self.AdminSpace_locators, 'filter_isInactive_checkbox'))

    def checkFilterisInactiveCheckboxStatus(self):
        elements = self.getElement(*self.locator(self.AdminSpace_locators, 'filter_isInactive_checkbox_status'))
        return elements.is_selected()

    def clickFilterisCuratorCheckbox(self):
        self.elementClick(*self.locator(self.AdminSpace_locators, 'filter_isCurator_checkbox'))

    def checkFilterisCuratorCheckboxStatus(self):
        elements = self.getElement(*self.locator(self.AdminSpace_locators, 'filter_isCurator_checkbox_status'))
        return elements.is_selected()

    def clickFilterpastCuratorCheckbox(self):
        self.elementClick(*self.locator(self.AdminSpace_locators, 'filter_pastCurator_checkbox'))

    def checkFilterpastCuratorCheckboxStatus(self):
        elements = self.getElement(*self.locator(self.AdminSpace_locators, 'filter_pastCurator_checkbox_status'))
        return elements.is_selected()

    def clickFilterisGuideCheckbox(self):
        self.elementClick(*self.locator(self.AdminSpace_locators, 'filter_isGuide_checkbox'))

    def checkFilterisGuideCheckboxStatus(self):
        elements = self.getElement(*self.locator(self.AdminSpace_locators, 'filter_isGuide_checkbox_status'))
        return elements.is_selected()

    def clickFilterpastGuideCheckbox(self):
        self.elementClick(*self.locator(self.AdminSpace_locators, 'filter_pastGuide_checkbox'))

    def checkFilterpastGuideCheckboxStatus(self):
        elements = self.getElement(*self.locator(self.AdminSpace_locators, 'filter_pastGuide_checkbox_status'))
        return elements.is_selected()

    def clickFilterorderByCheckbox(self):
        self.elementClick(*self.locator(self.AdminSpace_locators, 'filter_orderBy_checkbox'))

    def checkFilterorderByCheckboxStatus(self):
        elements = self.getElement(*self.locator(self.AdminSpace_locators, 'filter_orderBy_checkbox_status'))
        return elements.is_selected()

    def selectorderByOption(self, selector):
        self.dropdownSelectElement(selector, *self.locator(self.AdminSpace_locators, 'filter_select_orderByOption'),
                                   selectorType="value")

    def checkViewGuidedExplorersLinkPresent(self):
        element = self.isElementPresent(*self.locator(self.AdminSpace_locators, 'View_guided_Explorers'))
        return element

    def clickNameOfGuidedExplorers(self):
        self.elementClick(*self.locator(self.AdminSpace_locators, 'name_of_guided_Explorers'))

    def clickCancelButton(self):
        self.elementClick(*self.locator(self.AdminSpace_locators, 'cancel_button'))

    def checkTotalCardCounts(self):
        elements = self.getElementList(*self.locator(self.AdminSpace_locators, 'card_counts'))
        return elements

    def clickWithActiveGuidedExplorersCheckbox(self):
        self.elementClick(*self.locator(self.AdminSpace_locators, 'with_active_guided_explorers_checkbox'))

    def clickWithOutActiveGuidedExplorersCheckbox(self):
        self.elementClick(*self.locator(self.AdminSpace_locators, 'without_active_guided_explorers_checkbox'))

    def checkWithActiveGuidedExplorers(self):
        tab = self.driver.find_element(By.XPATH, "//div[@class='row ng-star-inserted']")
        for row in tab.find_elements_by_xpath("./div"):
            for td in row.find_elements_by_xpath(".//following-sibling::small"):
                l = td.text.split(': ')
                self.log.info(l[1])
                if int(l[1]) >= 1:
                    self.log.info("User has Active Guided Explorers")
                else:
                    self.log.info("Active Guided Explorers Not present--Fail")

    def checkWithOutActiveGuidedExplorers(self):
        tab = self.driver.find_element(By.XPATH, "//div[@class='row ng-star-inserted']")
        for row in tab.find_elements_by_xpath("./div"):
            for td in row.find_elements_by_xpath(".//following-sibling::small"):
                l = td.text.split(': ')
                self.log.info(l[1])
                if int(l[1]) <= 0:
                    self.log.info("Active Guided Explorers Not present")
                else:
                    self.log.info("User has Active Guided Explorers--Fail")
