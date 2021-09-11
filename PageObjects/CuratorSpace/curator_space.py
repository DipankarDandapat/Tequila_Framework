import FrameworkUtilities.logger_utility as log_utils
from HelperLibraries.basepage import BasePage
import logging


class CuratorSpace(BasePage):
    log = log_utils.custom_logger(logging.INFO)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.CuratorSpace_locators = self.pageLocators('CuratorSpace')

    def clickCuratorSpace(self):
        self.elementClick(*self.locator(self.CuratorSpace_locators, 'curatorSpace_link'))

    def clickManageConstellationLink(self):
        self.elementClick(*self.locator(self.CuratorSpace_locators, 'manage_constellation_link'))

    def getManageConstellationPageTitle(self):
        element = self.getText(*self.locator(self.CuratorSpace_locators, 'manage_constellation_title'))
        return element

    def clickManageMeaningCentralLink(self):
        self.elementClick(*self.locator(self.CuratorSpace_locators, 'manage_meaning_central_link'))

    def clickManageCommunityLink(self):
        self.elementClick(*self.locator(self.CuratorSpace_locators, 'manage_community_link'))

    def clickManageCirclesLink(self):
        self.elementClick(*self.locator(self.CuratorSpace_locators, 'manage_circles_link'))

    def clickManageFlaggedContentLink(self):
        self.elementClick(*self.locator(self.CuratorSpace_locators, 'manage_flagged_content_link'))

    def clickManageTopicsLink(self):
        self.elementClick(*self.locator(self.CuratorSpace_locators, 'manage_topics_link'))

    def clickAddNewConstellationButton(self):
        self.elementClick(*self.locator(self.CuratorSpace_locators, 'add_new_constellation_button'))

    def getAddNewConstellationTitle(self):
        element = self.getText(*self.locator(self.CuratorSpace_locators, 'add_new_constellation_title'))
        return element

    def enterTitleBox(self, data=''):
        self.sendKeys(data, *self.locator(self.CuratorSpace_locators, 'title_box'))

    def enterDescriptionBox(self, data=''):
        self.sendKeys(data, *self.locator(self.CuratorSpace_locators, 'description_box'))

    def enterLinkUrl(self, data=''):
        self.sendKeys(data, *self.locator(self.CuratorSpace_locators, 'link_url'))

    def enterMeaningSphereRecommends(self, data=''):
        self.sendKeys(data, *self.locator(self.CuratorSpace_locators, 'meaningSphere_recommends'))

    def getMeaningSphereRecommends(self):
        element = self.getElement(*self.locator(self.CuratorSpace_locators, 'meaningSphere_recommends'))
        return element

    def clickSuggestedByArrow(self):
        self.elementClick(*self.locator(self.CuratorSpace_locators, 'suggested_by_arrow'))

    def clickSuggestedByClearAll(self):
        self.elementClick(*self.locator(self.CuratorSpace_locators, 'suggested_by_clear_all'))

    def getAllSuggestedByUserList(self):
        element = self.getElementList(*self.locator(self.CuratorSpace_locators, 'suggested_by_user_list'))
        return element

    def selectCategory(self,selector):
        self.dropdownSelectElement(selector,selectorType="index",*self.locator(self.CuratorSpace_locators, 'category_select'))

    def meaningSphereuploadImage(self,data):
        self.sendKeys(data, *self.locator(self.CuratorSpace_locators, 'curatorspace_upload_image'))

    def clickSaveButton(self):
        self.elementClick(*self.locator(self.CuratorSpace_locators, 'save_button'))
    def clickRemoveButton(self):
        self.elementClick(*self.locator(self.CuratorSpace_locators, 'remove_button'))
    def clickYesRemoveButton(self):
        self.elementClick(*self.locator(self.CuratorSpace_locators, 'yes_remove_button'))

    def getSaveButtonStatus(self):
        element = self.getElement(*self.locator(self.CuratorSpace_locators, 'save_button'))
        return element

    def getToastMessage(self):
        element = self.getText(*self.locator(self.CuratorSpace_locators, 'toast_message'))
        return element

    def clickDetailsPage(self):
        self.elementClick(*self.locator(self.CuratorSpace_locators, 'details_page'))

    def getDetailsPageTitle(self):
        element = self.getText(*self.locator(self.CuratorSpace_locators, 'details_page_title'))
        return element
    def getDetailsPageDescription(self):
        element = self.getText(*self.locator(self.CuratorSpace_locators, 'details_page_Description'))
        return element
    def getDetailsPageCategory(self):
        element = self.getText(*self.locator(self.CuratorSpace_locators, 'details_page_Category'))
        return element

    def getDetailsPageRatingDisplayed(self):
        element = self.isElementDisplayed(*self.locator(self.CuratorSpace_locators, 'details_page_rating'))
        return element