from FrameworkUtilities.teststatus_utility import test_Status
from PageObjects.LoginPage.login_page import LoginPage
from FrameworkUtilities.data_reader_utility import DataReader
import unittest
import pytest
import sys
import allure
from PageObjects.HomeNavigation.home_navigation import HomeNavigation
from PageObjects.AdminSpace.admin_space import AdminSpace
import FrameworkUtilities.logger_utility as log_utils
import logging
import time


@pytest.mark.usefixtures("get_driver", "initialize")
@allure.story('Test Automation Demo ')
@allure.feature('Verification Using Requests')
class AdminSpaceTest(unittest.TestCase):
    log = log_utils.custom_logger(logging.INFO)
    data_reader = DataReader()

    @pytest.fixture(scope='function')
    def initialize(self):
        self.homeNavigation = HomeNavigation(self.driver)
        self.loginPage = LoginPage(self.driver)
        self.AdminSpacePage = AdminSpace(self.driver)
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


    @allure.testcase("Verify that an admin has access to the Admin Space")
    @pytest.mark.order(1)
    @pytest.mark.smoke
    @allure.severity(allure.severity_level.MINOR)  # severity of the test case
    # @pytestrail.case('C1') # test case if on TestRail
    def test_VerifyThatAnAdminHasAccessToTheAdminSpace(self):
        test_name = sys._getframe().f_code.co_name

        self.log.info("###### TEST EXECUTION STARTED :: " + test_name + " ######")

        with allure.step('Login in to the platform with an Admin credentials'):
            self.homeNavigation.clickAcceptCoockiesButton()
            self.homeNavigation.clickUserProfileIcon()
            self.loginPage.login()
            time.sleep(10)
            self.homeNavigation.clickUserProfileIcon()
            time.sleep(3)
            try:
                element=self.AdminSpacePage.checkAdminSpaceLinkPresent()
                self.log.info(element)
                self.log.info(" have access to the Admin Space")
            except:self.log.info("admin does't have access to the Admin Space")
            time.sleep(10)

    @allure.testcase("Verify that an explorer does not have access to the Admin Space")
    @pytest.mark.order(2)
    @pytest.mark.smoke
    @allure.severity(allure.severity_level.MINOR)  # severity of the test case
    # @pytestrail.case('C1') # test case if on TestRail
    def test_VerifyThatAnExplorerDoesNotHaveAccessToTheAdminSpace(self):
        test_name = sys._getframe().f_code.co_name

        self.log.info("###### TEST EXECUTION STARTED :: " + test_name + " ######")

        with allure.step('Login in to the platform with an explorer credentials'):
            self.homeNavigation.clickAcceptCoockiesButton()
            self.homeNavigation.clickUserProfileIcon()
            self.loginPage.login(email=self.data_reader.get_data(test_name, 'UserName'),password=self.data_reader.get_data(test_name, 'Password'))
            time.sleep(10)
            self.homeNavigation.clickUserProfileIcon()
            time.sleep(3)
            element = self.AdminSpacePage.checkAdminSpaceLinkPresent()
            self.log.info(element)
            self.log.info("Explorer does't have access to the Admin Space")
            time.sleep(10)

    @allure.testcase("Verify creation on new user account")
    @pytest.mark.order(3)
    @pytest.mark.smoke
    @allure.severity(allure.severity_level.MINOR)  # severity of the test case
    # @pytestrail.case('C1') # test case if on TestRail
    def test_VerifyCreationOnNewUserAccount(self):
        test_name = sys._getframe().f_code.co_name

        self.log.info("###### TEST EXECUTION STARTED :: " + test_name + " ######")

        with allure.step('Login in to the platform with an Admin credentials'):
            self.homeNavigation.clickAcceptCoockiesButton()
            self.homeNavigation.clickUserProfileIcon()
            self.loginPage.login()
            time.sleep(10)
            self.homeNavigation.clickUserProfileIcon()
            self.AdminSpacePage.clickAdminSpaceLink()
            time.sleep(10)
            self.AdminSpacePage.checkManageExplorersPageheaderLabelPresent()
            self.AdminSpacePage.clickAddExplorersButton()
            time.sleep(2)
            self.AdminSpacePage.checkAddExplorersPageheaderLabelPresent()
            self.AdminSpacePage.enterAddExplorersFirstName(self.data_reader.get_data(test_name, 'FirstName'))
            status = self.AdminSpacePage.getSaveButtonStatus()
            if status == False:
                self.log.info("After enter First name Save Button is Disable --Pass")
            else:
                self.log.info("After enter First name Save Button is Enable --Fail")

            self.AdminSpacePage.enterAddExplorersLastName(data=self.data_reader.get_data(test_name, 'LastName'))
            status = self.AdminSpacePage.getSaveButtonStatus()
            if status == False:
                self.log.info("After enter Last name Save Button is Disable --Pass")
            else:
                self.log.info("After enter Last name Save Button is Enable --Fail")

            self.AdminSpacePage.enterAddExplorersEmail(data=self.data_reader.get_data(test_name, 'Email'))
            status = self.AdminSpacePage.getSaveButtonStatus()
            if status == False:
                self.log.info("After enter Email id Save Button is Disable --Pass")
            else:
                self.log.info("After enter Email id Save Button is Enable --Fail")

            self.AdminSpacePage.clickAsAGuideNoRadioButton()
            status = self.AdminSpacePage.getSaveButtonStatus()
            if status == False:
                self.log.info("After click As a Guide check box Save Button is Disable --Pass")
            else:
                self.log.info("After click As a Guide check boxSave Button is Enable --Fail")

            self.AdminSpacePage.clickAsACuratorNoRadioButton()
            status = self.AdminSpacePage.getSaveButtonStatus()
            if status == False:
                self.log.info("After click As a Curator check box Save Button is Disable --Pass")
            else:
                self.log.info("After click As a Curator check boxSave Button is Enable --Fail")

            time.sleep(2)
            self.AdminSpacePage.clickAsAAdministratorNoRadioButton()
            status = self.AdminSpacePage.getSaveButtonStatus()
            if status == False:
                self.log.info("After click As a Administrator check box Save Button is Disable --Fail")
            else:
                self.log.info("After click As a Administrator check box Save Button is Enable --Pass")

            self.AdminSpacePage.clickSaveButton()
            time.sleep(4)
            message=self.AdminSpacePage.getToastMessage()
            if message=="Explorer added successfully!":
                self.log.info("Explorer user records added successfully!")
            else:self.log.info("Unable to added Explorer user records ")
            self.AdminSpacePage.enterSearchBox(data=self.data_reader.get_data(test_name, 'SearchBox'))
            time.sleep(10)
            element=self.AdminSpacePage.getAllUserTitle()
            for i in range(len(element)):
                if element[i].text==self.data_reader.get_data(test_name, 'SearchBox'):
                    explorersince=self.AdminSpacePage.getExplorerSince()
                    date=explorersince.split(': ')
                    if date[1]==self.data_reader.get_data(test_name, 'CreatedDate'):
                        self.log.info("explorersince date is correct")

                break
            else:self.log.info("No user present base on search")

    @allure.testcase("Verify user search by name")
    @pytest.mark.order(4)
    @pytest.mark.smoke
    @allure.severity(allure.severity_level.MINOR)
    def test_VerifyUserSearchByName(self):
        test_name = sys._getframe().f_code.co_name

        self.log.info("###### TEST EXECUTION STARTED :: " + test_name + " ######")
        with allure.step('Login in to the platform with an Admin credentials'):
            self.homeNavigation.clickAcceptCoockiesButton()
            self.homeNavigation.clickUserProfileIcon()
            self.loginPage.login()
            time.sleep(10)
            self.homeNavigation.clickUserProfileIcon()
            self.AdminSpacePage.clickAdminSpaceLink()
            time.sleep(10)
            self.AdminSpacePage.checkManageExplorersPageheaderLabelPresent()
            self.AdminSpacePage.enterSearchBox(data=self.data_reader.get_data(test_name, 'FirstName'))
            element=self.AdminSpacePage.getAllUserTitle()
            for i in range(len(element)):
                if element[i].text==self.data_reader.get_data(test_name, 'FirstName'):
                    self.log.info("User is present on the list")
                break
            else:self.log.info("No user present base on search")
            time.sleep(5)
            self.AdminSpacePage.clearSearchBox()
            self.AdminSpacePage.enterSearchBox(data=self.data_reader.get_data(test_name, 'SearchBox'))
            time.sleep(5)
            self.AdminSpacePage.checkNoDataFoundMessagePresent()

    @allure.testcase("Verify the options listed for an active Explorer record")
    @pytest.mark.order(5)
    @pytest.mark.smoke
    @allure.severity(allure.severity_level.MINOR)
    def test_VerifyTheOptionsListedForAnActiveExplorerRecord(self):
        test_name = sys._getframe().f_code.co_name
        self.log.info("###### TEST EXECUTION STARTED :: " + test_name + " ######")
        with allure.step('Login in to the platform with an Admin credentials'):
            self.homeNavigation.clickAcceptCoockiesButton()
            self.homeNavigation.clickUserProfileIcon()
            self.loginPage.login()
            time.sleep(10)
            self.homeNavigation.clickUserProfileIcon()
            self.AdminSpacePage.clickAdminSpaceLink()
            time.sleep(10)
            self.AdminSpacePage.checkManageExplorersPageheaderLabelPresent()
            self.AdminSpacePage.enterSearchBox(data=self.data_reader.get_data(test_name, 'SearchBox'))
            time.sleep(5)
            self.AdminSpacePage.clickThreeVerticalDotsLink()
            self.AdminSpacePage.checkViewProfileLinkPresent()
            self.AdminSpacePage.checkEditProfileLinkPresent()
            self.AdminSpacePage.checkAddAsCuratorLinkPresent()
            self.AdminSpacePage.checkAddAsAdminLinkPresent()
            self.AdminSpacePage.checkAddAsGuideLinkPresent()
            self.AdminSpacePage.checkLockExplorerLinkPresent()
            self.AdminSpacePage.checkViewAccountActivityLinkPresent()
            self.AdminSpacePage.checkPasswordResetLinkPresent()
            self.AdminSpacePage.clickDismissFilter()
            time.sleep(5)

    @allure.testcase("Verify the options listed for an active Guide record")
    @pytest.mark.order(6)
    @pytest.mark.smoke
    @allure.severity(allure.severity_level.MINOR)
    def test_VerifyTheOptionsListedForAnActiveGuideRecord(self):
        test_name = sys._getframe().f_code.co_name
        self.log.info("###### TEST EXECUTION STARTED :: " + test_name + " ######")
        with allure.step('Login in to the platform with an Admin credentials'):
            self.homeNavigation.clickAcceptCoockiesButton()
            self.homeNavigation.clickUserProfileIcon()
            self.loginPage.login()
            time.sleep(10)
            self.homeNavigation.clickUserProfileIcon()
            self.AdminSpacePage.clickAdminSpaceLink()
            time.sleep(10)
            self.AdminSpacePage.checkManageExplorersPageheaderLabelPresent()
            self.AdminSpacePage.enterSearchBox(data=self.data_reader.get_data(test_name, 'SearchBox'))
            time.sleep(10)
            self.AdminSpacePage.clickThreeVerticalDotsLink()
            self.AdminSpacePage.checkViewProfileLinkPresent()
            self.AdminSpacePage.checkEditProfileLinkPresent()
            self.AdminSpacePage.checkAddAsCuratorLinkPresent()
            self.AdminSpacePage.checkAddAsAdminLinkPresent()
            self.AdminSpacePage.checkRemoveAsGuideLinkPresent()
            self.AdminSpacePage.checkLockExplorerLinkPresent()
            self.AdminSpacePage.checkViewAccountActivityLinkPresent()
            self.AdminSpacePage.checkPasswordResetLinkPresent()
            self.AdminSpacePage.clickDismissFilter()
            time.sleep(5)

    @allure.testcase("Verify the options listed for an active Curator record")
    @pytest.mark.order(7)
    @pytest.mark.smoke
    @allure.severity(allure.severity_level.MINOR)
    def test_VerifyTheOptionsListedForAnActiveCuratorRecord(self):
        test_name = sys._getframe().f_code.co_name
        self.log.info("###### TEST EXECUTION STARTED :: " + test_name + " ######")
        with allure.step('Login in to the platform with an Admin credentials'):
            self.homeNavigation.clickAcceptCoockiesButton()
            self.homeNavigation.clickUserProfileIcon()
            self.loginPage.login()
            time.sleep(10)
            self.homeNavigation.clickUserProfileIcon()
            self.AdminSpacePage.clickAdminSpaceLink()
            time.sleep(10)
            self.AdminSpacePage.checkManageExplorersPageheaderLabelPresent()
            self.AdminSpacePage.enterSearchBox(data=self.data_reader.get_data(test_name, 'SearchBox'))
            time.sleep(10)
            self.AdminSpacePage.clickThreeVerticalDotsLink()
            time.sleep(2)
            self.AdminSpacePage.checkViewProfileLinkPresent()
            self.AdminSpacePage.checkEditProfileLinkPresent()
            self.AdminSpacePage.checkRemoveAsCuratorLinkPresent()
            self.AdminSpacePage.checkAddAsAdminLinkPresent()
            self.AdminSpacePage.checkAddAsGuideLinkPresent()
            self.AdminSpacePage.checkLockExplorerLinkPresent()
            self.AdminSpacePage.checkViewAccountActivityLinkPresent()
            self.AdminSpacePage.checkPasswordResetLinkPresent()
            self.AdminSpacePage.clickDismissFilter()
            time.sleep(5)

    @allure.testcase("Verify information displayed and the options listed for a locked user")
    @pytest.mark.order(8)
    @pytest.mark.smoke
    @allure.severity(allure.severity_level.MINOR)
    def test_VerifyInformationDisplayedAndTheOptionsListedForALockedUser(self):
        test_name = sys._getframe().f_code.co_name
        self.log.info("###### TEST EXECUTION STARTED :: " + test_name + " ######")
        with allure.step('Login in to the platform with an Admin credentials'):
            self.homeNavigation.clickAcceptCoockiesButton()
            self.homeNavigation.clickUserProfileIcon()
            self.loginPage.login()
            time.sleep(10)
            self.homeNavigation.clickUserProfileIcon()
            self.AdminSpacePage.clickAdminSpaceLink()
            time.sleep(10)
            self.AdminSpacePage.checkManageExplorersPageheaderLabelPresent()
            self.AdminSpacePage.enterSearchBox(data=self.data_reader.get_data(test_name, 'SearchBox'))
            time.sleep(10)
            self.AdminSpacePage.clickThreeVerticalDotsLink()
            time.sleep(2)
            self.AdminSpacePage.checkViewProfileLinkPresent()
            self.AdminSpacePage.checkEditProfileLinkPresent()
            self.AdminSpacePage.checkUnlockExplorerLinkPresent()
            self.AdminSpacePage.checkViewAccountActivityLinkPresent()
            self.AdminSpacePage.checkPasswordResetLinkPresent()
            self.AdminSpacePage.clickDismissFilter()
            time.sleep(5)

    @allure.testcase("Verify icons and options displayed for an active user who has been assigned to Guide & Curator roles")
    @pytest.mark.order(9)
    @pytest.mark.smoke
    @allure.severity(allure.severity_level.MINOR)
    def test_VerifyIconsAndOptionsDisplayedForAnActiveUserWhoHasBeenAssignedToGuideAndCuratorRoles(self):
        test_name = sys._getframe().f_code.co_name
        self.log.info("###### TEST EXECUTION STARTED :: " + test_name + " ######")
        with allure.step('Login in to the platform with an Admin credentials'):
            self.homeNavigation.clickAcceptCoockiesButton()
            self.homeNavigation.clickUserProfileIcon()
            self.loginPage.login()
            time.sleep(10)
            self.homeNavigation.clickUserProfileIcon()
            self.AdminSpacePage.clickAdminSpaceLink()
            time.sleep(10)
            self.AdminSpacePage.checkManageExplorersPageheaderLabelPresent()
            self.AdminSpacePage.enterSearchBox(data=self.data_reader.get_data(test_name, 'SearchBox'))
            time.sleep(10)
            self.AdminSpacePage.checkGuideIconPresent()
            self.AdminSpacePage.checkCuratorIconPresent()
            self.AdminSpacePage.clickThreeVerticalDotsLink()
            time.sleep(2)
            self.AdminSpacePage.checkViewProfileLinkPresent()
            self.AdminSpacePage.checkEditProfileLinkPresent()
            self.AdminSpacePage.checkAddAsAdminLinkPresent()
            self.AdminSpacePage.checkRemoveAsGuideLinkPresent()
            self.AdminSpacePage.checkRemoveAsCuratorLinkPresent()
            self.AdminSpacePage.checkViewAccountActivityLinkPresent()
            self.AdminSpacePage.checkPasswordResetLinkPresent()
            self.AdminSpacePage.clickDismissFilter()
            time.sleep(5)


    @allure.testcase("Verify icons and options displayed for an active user who has been assigned to Guide & Admin roles")
    @pytest.mark.order(10)
    @pytest.mark.smoke
    @allure.severity(allure.severity_level.MINOR)
    def test_VerifyIconsAndOptionsDisplayedForAnActiveUserWhoHasBeenAssignedToGuideAndAdminRoles(self):
        test_name = sys._getframe().f_code.co_name
        self.log.info("###### TEST EXECUTION STARTED :: " + test_name + " ######")
        with allure.step('Login in to the platform with an Admin credentials'):
            self.homeNavigation.clickAcceptCoockiesButton()
            self.homeNavigation.clickUserProfileIcon()
            self.loginPage.login()
            time.sleep(10)
            self.homeNavigation.clickUserProfileIcon()
            self.AdminSpacePage.clickAdminSpaceLink()
            time.sleep(10)
            self.AdminSpacePage.checkManageExplorersPageheaderLabelPresent()
            self.AdminSpacePage.enterSearchBox(data=self.data_reader.get_data(test_name, 'SearchBox'))
            time.sleep(10)
            self.AdminSpacePage.checkGuideIconPresent()
            self.AdminSpacePage.checkAdminIconPresent()
            self.AdminSpacePage.clickThreeVerticalDotsLink()
            time.sleep(2)
            self.AdminSpacePage.checkViewProfileLinkPresent()
            self.AdminSpacePage.checkEditProfileLinkPresent()
            self.AdminSpacePage.checkAddAsCuratorLinkPresent()
            self.AdminSpacePage.checkRemoveAsGuideLinkPresent()
            self.AdminSpacePage.checkRemoveAsAdminLinkPresent()
            self.AdminSpacePage.checkViewAccountActivityLinkPresent()
            self.AdminSpacePage.checkPasswordResetLinkPresent()
            self.AdminSpacePage.clickDismissFilter()
            time.sleep(5)

    @allure.testcase("Verify icons and options displayed for an active user who has been assigned to Curator & Admin roles")
    @pytest.mark.order(11)
    @pytest.mark.smoke
    @allure.severity(allure.severity_level.MINOR)
    def test_VerifyIconsAndOptionsDisplayedForAnActiveUserWhoHasBeenAssignedToCuratorAndAdminRoles(self):
        test_name = sys._getframe().f_code.co_name
        self.log.info("###### TEST EXECUTION STARTED :: " + test_name + " ######")
        with allure.step('Login in to the platform with an Admin credentials'):
            self.homeNavigation.clickAcceptCoockiesButton()
            self.homeNavigation.clickUserProfileIcon()
            self.loginPage.login()
            time.sleep(10)
            self.homeNavigation.clickUserProfileIcon()
            self.AdminSpacePage.clickAdminSpaceLink()
            time.sleep(10)
            self.AdminSpacePage.checkManageExplorersPageheaderLabelPresent()
            self.AdminSpacePage.enterSearchBox(data=self.data_reader.get_data(test_name, 'SearchBox'))
            time.sleep(10)
            self.AdminSpacePage.checkCuratorIconPresent()
            self.AdminSpacePage.checkAdminIconPresent()
            self.AdminSpacePage.clickThreeVerticalDotsLink()
            time.sleep(2)
            self.AdminSpacePage.checkViewProfileLinkPresent()
            self.AdminSpacePage.checkEditProfileLinkPresent()
            self.AdminSpacePage.checkAddAsGuideLinkPresent()
            self.AdminSpacePage.checkRemoveAsCuratorLinkPresent()
            self.AdminSpacePage.checkRemoveAsAdminLinkPresent()
            self.AdminSpacePage.checkViewAccountActivityLinkPresent()
            self.AdminSpacePage.checkPasswordResetLinkPresent()
            self.AdminSpacePage.clickDismissFilter()
            time.sleep(5)

    @allure.testcase("Verify icons and options displayed for an active user who has been assigned to Guide, Curator & Admin roles")
    @pytest.mark.order(12)
    @pytest.mark.smoke
    @allure.severity(allure.severity_level.MINOR)
    def test_VerifyIconsAndOptionsDisplayedForAnActiveUserWhoHasBeenAssignedToGuideCuratorAndAdminRoles(self):
        test_name = sys._getframe().f_code.co_name
        self.log.info("###### TEST EXECUTION STARTED :: " + test_name + " ######")
        with allure.step('Login in to the platform with an Admin credentials'):
            self.homeNavigation.clickAcceptCoockiesButton()
            self.homeNavigation.clickUserProfileIcon()
            self.loginPage.login()
            time.sleep(10)
            self.homeNavigation.clickUserProfileIcon()
            self.AdminSpacePage.clickAdminSpaceLink()
            time.sleep(10)
            self.AdminSpacePage.checkManageExplorersPageheaderLabelPresent()
            self.AdminSpacePage.enterSearchBox(data=self.data_reader.get_data(test_name, 'SearchBox'))
            time.sleep(10)
            self.AdminSpacePage.checkGuideIconPresent()
            self.AdminSpacePage.checkCuratorIconPresent()
            self.AdminSpacePage.checkAdminIconPresent()
            self.AdminSpacePage.clickThreeVerticalDotsLink()
            time.sleep(2)
            self.AdminSpacePage.checkViewProfileLinkPresent()
            self.AdminSpacePage.checkEditProfileLinkPresent()
            self.AdminSpacePage.checkRemoveAsGuideLinkPresent()
            self.AdminSpacePage.checkRemoveAsCuratorLinkPresent()
            self.AdminSpacePage.checkRemoveAsAdminLinkPresent()
            self.AdminSpacePage.checkViewAccountActivityLinkPresent()
            self.AdminSpacePage.checkPasswordResetLinkPresent()
            self.AdminSpacePage.clickDismissFilter()
            time.sleep(5)

    @allure.testcase("Verify user search filtered by Locked Users")
    @pytest.mark.order(13)
    @pytest.mark.smoke
    @allure.severity(allure.severity_level.MINOR)
    def test_VerifyUserSearchFilteredByLockedUsers(self):
        test_name = sys._getframe().f_code.co_name
        self.log.info("###### TEST EXECUTION STARTED :: " + test_name + " ######")
        with allure.step('Login in to the platform with an Admin credentials'):
            self.homeNavigation.clickAcceptCoockiesButton()
            self.homeNavigation.clickUserProfileIcon()
            self.loginPage.login()
            time.sleep(10)
            self.homeNavigation.clickUserProfileIcon()
            self.AdminSpacePage.clickAdminSpaceLink()
            time.sleep(10)
            self.AdminSpacePage.checkManageExplorersPageheaderLabelPresent()
            self.AdminSpacePage.clickFilterLink()
            element=self.AdminSpacePage.checkFilterisLockedCheckboxStatus()
            if element==False:
                self.AdminSpacePage.clickFilterisLockedCheckbox()
                self.AdminSpacePage.clickFilterGoButton()
            self.AdminSpacePage.clickDismissFilter()
            time.sleep(7)

    @allure.testcase("Verify user search filtered by InActive Users")
    @pytest.mark.order(14)
    @pytest.mark.smoke
    @allure.severity(allure.severity_level.MINOR)
    def test_VerifyUserSearchFilteredByInActiveUsers(self):
        test_name = sys._getframe().f_code.co_name
        self.log.info("###### TEST EXECUTION STARTED :: " + test_name + " ######")
        with allure.step('Login in to the platform with an Admin credentials'):
            self.homeNavigation.clickAcceptCoockiesButton()
            self.homeNavigation.clickUserProfileIcon()
            self.loginPage.login()
            time.sleep(10)
            self.homeNavigation.clickUserProfileIcon()
            self.AdminSpacePage.clickAdminSpaceLink()
            time.sleep(10)
            self.AdminSpacePage.checkManageExplorersPageheaderLabelPresent()
            self.AdminSpacePage.clickFilterLink()
            element = self.AdminSpacePage.checkFilterisInactiveCheckboxStatus()
            if element == False:
                self.AdminSpacePage.clickFilterisInactiveCheckbox()
                self.AdminSpacePage.clickFilterGoButton()
            self.AdminSpacePage.clickDismissFilter()
            time.sleep(7)

    @allure.testcase("Verify user search filtered by Curators")
    @pytest.mark.order(15)
    @pytest.mark.smoke
    @allure.severity(allure.severity_level.MINOR)
    def test_VerifyUserSearchFilteredByCurators(self):
        test_name = sys._getframe().f_code.co_name
        self.log.info("###### TEST EXECUTION STARTED :: " + test_name + " ######")
        with allure.step('Login in to the platform with an Admin credentials'):
            self.homeNavigation.clickAcceptCoockiesButton()
            self.homeNavigation.clickUserProfileIcon()
            self.loginPage.login()
            time.sleep(10)
            self.homeNavigation.clickUserProfileIcon()
            self.AdminSpacePage.clickAdminSpaceLink()
            time.sleep(10)
            self.AdminSpacePage.checkManageExplorersPageheaderLabelPresent()
            self.AdminSpacePage.clickFilterLink()
            element = self.AdminSpacePage.checkFilterisCuratorCheckboxStatus()
            if element == False:
                self.AdminSpacePage.clickFilterisCuratorCheckbox()
                self.AdminSpacePage.clickFilterGoButton()
            self.AdminSpacePage.clickDismissFilter()
            time.sleep(7)
            #verify the icon
            self.AdminSpacePage.clickFilterLink()
            element = self.AdminSpacePage.checkFilterpastCuratorCheckboxStatus()
            if element == False:
                time.sleep(2)
                self.AdminSpacePage.clickFilterpastCuratorCheckbox()
                time.sleep(2)
                self.AdminSpacePage.clickFilterGoButton()
            self.AdminSpacePage.clickDismissFilter()
            time.sleep(7)

    @allure.testcase("Verify user search filtered by Guides")
    @pytest.mark.order(16)
    @pytest.mark.smoke
    @allure.severity(allure.severity_level.MINOR)
    def test_VerifyUserSearchFilteredByGuides(self):
        test_name = sys._getframe().f_code.co_name
        self.log.info("###### TEST EXECUTION STARTED :: " + test_name + " ######")
        with allure.step('Login in to the platform with an Admin credentials'):
            self.homeNavigation.clickAcceptCoockiesButton()
            self.homeNavigation.clickUserProfileIcon()
            self.loginPage.login()
            time.sleep(10)
            self.homeNavigation.clickUserProfileIcon()
            self.AdminSpacePage.clickAdminSpaceLink()
            time.sleep(10)
            self.AdminSpacePage.checkManageExplorersPageheaderLabelPresent()
            self.AdminSpacePage.clickFilterLink()
            element = self.AdminSpacePage.checkFilterisGuideCheckboxStatus()
            if element == False:
                self.AdminSpacePage.clickFilterisGuideCheckbox()
                self.AdminSpacePage.clickFilterGoButton()
            self.AdminSpacePage.clickDismissFilter()
            time.sleep(7)
            # verify the icon
            self.AdminSpacePage.clickFilterLink()
            element = self.AdminSpacePage.checkFilterpastGuideCheckboxStatus()
            if element == False:
                time.sleep(2)
                self.AdminSpacePage.clickFilterpastGuideCheckbox()
                time.sleep(2)
                self.AdminSpacePage.clickFilterGoButton()
            self.AdminSpacePage.clickDismissFilter()
            time.sleep(7)

    @allure.testcase("Verify user search result as per the Order By value")
    @pytest.mark.order(17)
    @pytest.mark.smoke
    @allure.severity(allure.severity_level.MINOR)
    def test_VerifyUserSearchResultAsPerTheOrderByValue(self):
        test_name = sys._getframe().f_code.co_name
        self.log.info("###### TEST EXECUTION STARTED :: " + test_name + " ######")
        with allure.step('Login in to the platform with an Admin credentials'):
            self.homeNavigation.clickAcceptCoockiesButton()
            self.homeNavigation.clickUserProfileIcon()
            self.loginPage.login()
            time.sleep(10)
            self.homeNavigation.clickUserProfileIcon()
            self.AdminSpacePage.clickAdminSpaceLink()
            time.sleep(10)
            self.AdminSpacePage.checkManageExplorersPageheaderLabelPresent()

            self.AdminSpacePage.clickFilterLink()
            element = self.AdminSpacePage.checkFilterorderByCheckboxStatus()
            if element == False:
                self.AdminSpacePage.clickFilterorderByCheckbox()
                time.sleep(5)
                self.AdminSpacePage.selectorderByOption(selector='0')
                time.sleep(5)
                self.AdminSpacePage.clickFilterGoButton()
            self.AdminSpacePage.clickDismissFilter()
            time.sleep(10)
            self.AdminSpacePage.clickFilterLink()
            element = self.AdminSpacePage.checkFilterorderByCheckboxStatus()
            if element == True:
                self.AdminSpacePage.selectorderByOption(selector='1')
                time.sleep(5)
                self.AdminSpacePage.clickFilterGoButton()
            self.AdminSpacePage.clickDismissFilter()
            time.sleep(10)
            self.AdminSpacePage.clickFilterLink()
            element = self.AdminSpacePage.checkFilterorderByCheckboxStatus()
            if element == True:
                self.AdminSpacePage.selectorderByOption(selector='2')
                time.sleep(5)
                self.AdminSpacePage.clickFilterGoButton()
            self.AdminSpacePage.clickDismissFilter()
            time.sleep(10)
            self.AdminSpacePage.clickFilterLink()
            element = self.AdminSpacePage.checkFilterorderByCheckboxStatus()
            if element == True:
                self.AdminSpacePage.selectorderByOption(selector='3')
                time.sleep(5)
                self.AdminSpacePage.clickFilterGoButton()
            self.AdminSpacePage.clickDismissFilter()
            time.sleep(10)

    @allure.testcase("Verify user search results when filtered by Curators & Mentors Users")
    @pytest.mark.order(18)
    @pytest.mark.smoke
    @allure.severity(allure.severity_level.MINOR)
    def test_VerifyUserSearchResultsWhenFilteredByCuratorsAndMentorsUsers(self):
        test_name = sys._getframe().f_code.co_name
        self.log.info("###### TEST EXECUTION STARTED :: " + test_name + " ######")
        with allure.step('Login in to the platform with an Admin credentials'):
            self.homeNavigation.clickAcceptCoockiesButton()
            self.homeNavigation.clickUserProfileIcon()
            self.loginPage.login()
            time.sleep(10)
            self.homeNavigation.clickUserProfileIcon()
            self.AdminSpacePage.clickAdminSpaceLink()
            time.sleep(10)
            self.AdminSpacePage.checkManageExplorersPageheaderLabelPresent()

            self.AdminSpacePage.clickFilterLink()
            element = self.AdminSpacePage.checkFilterisCuratorCheckboxStatus()
            if element == False:
                self.AdminSpacePage.clickFilterisCuratorCheckbox()
                time.sleep(5)
                element = self.AdminSpacePage.checkFilterisGuideCheckboxStatus()
                if element == False:
                    self.AdminSpacePage.clickFilterisGuideCheckbox()
                time.sleep(5)
                self.AdminSpacePage.clickFilterGoButton()
            self.AdminSpacePage.clickDismissFilter()
            time.sleep(10)

    @allure.testcase("Verify user search results when filtered by Curators and Locked Users")
    @pytest.mark.order(19)
    @pytest.mark.smoke
    @allure.severity(allure.severity_level.MINOR)
    def test_VerifyUserSearchResultsWhenFilteredByCuratorsAndLockedUsers(self):
        test_name = sys._getframe().f_code.co_name
        self.log.info("###### TEST EXECUTION STARTED :: " + test_name + " ######")
        with allure.step('Login in to the platform with an Admin credentials'):
            self.homeNavigation.clickAcceptCoockiesButton()
            self.homeNavigation.clickUserProfileIcon()
            self.loginPage.login()
            time.sleep(10)
            self.homeNavigation.clickUserProfileIcon()
            self.AdminSpacePage.clickAdminSpaceLink()
            time.sleep(10)
            self.AdminSpacePage.checkManageExplorersPageheaderLabelPresent()

            self.AdminSpacePage.clickFilterLink()
            element = self.AdminSpacePage.checkFilterisCuratorCheckboxStatus()
            if element == False:
                self.AdminSpacePage.clickFilterisCuratorCheckbox()
                time.sleep(5)
                element = self.AdminSpacePage.checkFilterisLockedCheckboxStatus()
                if element == False:
                    self.AdminSpacePage.clickFilterisLockedCheckbox()
                time.sleep(5)
                self.AdminSpacePage.clickFilterGoButton()
            self.AdminSpacePage.clickDismissFilter()
            time.sleep(10)

    @allure.testcase("Verify user search results when filtered by Guide and Locked Users")
    @pytest.mark.order(20)
    @pytest.mark.smoke
    @allure.severity(allure.severity_level.MINOR)
    def test_VerifyUserSearchResultsWhenFilteredByGuideAndLockedUsers(self):
        test_name = sys._getframe().f_code.co_name
        self.log.info("###### TEST EXECUTION STARTED :: " + test_name + " ######")
        with allure.step('Login in to the platform with an Admin credentials'):
            self.homeNavigation.clickAcceptCoockiesButton()
            self.homeNavigation.clickUserProfileIcon()
            self.loginPage.login()
            time.sleep(10)
            self.homeNavigation.clickUserProfileIcon()
            self.AdminSpacePage.clickAdminSpaceLink()
            time.sleep(10)
            self.AdminSpacePage.checkManageExplorersPageheaderLabelPresent()

            self.AdminSpacePage.clickFilterLink()
            element = self.AdminSpacePage.checkFilterisGuideCheckboxStatus()
            if element == False:
                self.AdminSpacePage.clickFilterisGuideCheckbox()
                time.sleep(5)
                element = self.AdminSpacePage.checkFilterisLockedCheckboxStatus()
                if element == False:
                    self.AdminSpacePage.clickFilterisLockedCheckbox()
                time.sleep(5)
                self.AdminSpacePage.clickFilterGoButton()
            self.AdminSpacePage.clickDismissFilter()
            time.sleep(10)

    @allure.testcase("Verify user search results when filtered by Curators and  by Inactive Users")
    @pytest.mark.order(21)
    @pytest.mark.smoke
    @allure.severity(allure.severity_level.MINOR)
    def test_VerifyUserSearchResultsWhenFilteredByCuratorsAndbyInactiveUsers(self):
        test_name = sys._getframe().f_code.co_name
        self.log.info("###### TEST EXECUTION STARTED :: " + test_name + " ######")
        with allure.step('Login in to the platform with an Admin credentials'):
            self.homeNavigation.clickAcceptCoockiesButton()
            self.homeNavigation.clickUserProfileIcon()
            self.loginPage.login()
            time.sleep(10)
            self.homeNavigation.clickUserProfileIcon()
            self.AdminSpacePage.clickAdminSpaceLink()
            time.sleep(10)
            self.AdminSpacePage.checkManageExplorersPageheaderLabelPresent()

            self.AdminSpacePage.clickFilterLink()
            element = self.AdminSpacePage.checkFilterisCuratorCheckboxStatus()
            if element == False:
                self.AdminSpacePage.clickFilterisCuratorCheckbox()
                time.sleep(5)
                element = self.AdminSpacePage.checkFilterisInactiveCheckboxStatus()
                if element == False:
                    self.AdminSpacePage.clickFilterisInactiveCheckbox()
                time.sleep(5)
                self.AdminSpacePage.clickFilterGoButton()
            self.AdminSpacePage.clickDismissFilter()
            time.sleep(10)

    @allure.testcase("Verify user search results when filtered by Guide and by Inactive Users")
    @pytest.mark.order(22)
    @pytest.mark.smoke
    @allure.severity(allure.severity_level.MINOR)
    def test_VerifyUserSearchResultsWhenFilteredByGuideAndbyInactiveUsers(self):
        test_name = sys._getframe().f_code.co_name
        self.log.info("###### TEST EXECUTION STARTED :: " + test_name + " ######")
        with allure.step('Login in to the platform with an Admin credentials'):
            self.homeNavigation.clickAcceptCoockiesButton()
            self.homeNavigation.clickUserProfileIcon()
            self.loginPage.login()
            time.sleep(10)
            self.homeNavigation.clickUserProfileIcon()
            self.AdminSpacePage.clickAdminSpaceLink()
            time.sleep(10)
            self.AdminSpacePage.checkManageExplorersPageheaderLabelPresent()

            self.AdminSpacePage.clickFilterLink()
            element = self.AdminSpacePage.checkFilterisGuideCheckboxStatus()
            if element == False:
                self.AdminSpacePage.clickFilterisGuideCheckbox()
                time.sleep(5)
                element = self.AdminSpacePage.checkFilterisInactiveCheckboxStatus()
                if element == False:
                    self.AdminSpacePage.clickFilterisInactiveCheckbox()
                time.sleep(5)
                self.AdminSpacePage.clickFilterGoButton()
            self.AdminSpacePage.clickDismissFilter()
            time.sleep(10)

    @allure.testcase("Verify user assignment to Curator role")
    @pytest.mark.order(23)
    @pytest.mark.smoke
    @allure.severity(allure.severity_level.MINOR)
    def test_VerifyUserAssignmentToCuratorRole(self):
        test_name = sys._getframe().f_code.co_name
        self.log.info("###### TEST EXECUTION STARTED :: " + test_name + " ######")
        with allure.step('Login in to the platform with an Admin credentials'):
            self.homeNavigation.clickAcceptCoockiesButton()
            self.homeNavigation.clickUserProfileIcon()
            self.loginPage.login()
            time.sleep(10)
            self.homeNavigation.clickUserProfileIcon()
            self.AdminSpacePage.clickAdminSpaceLink()
            time.sleep(10)
            self.AdminSpacePage.checkManageExplorersPageheaderLabelPresent()
            self.AdminSpacePage.enterSearchBox(data=self.data_reader.get_data(test_name, 'SearchBox'))
            time.sleep(10)
            self.AdminSpacePage.clickThreeVerticalDotsLink()
            self.AdminSpacePage.checkViewProfileLinkPresent()
            self.AdminSpacePage.checkEditProfileLinkPresent()
            self.AdminSpacePage.checkAddAsCuratorLinkPresent()
            self.AdminSpacePage.checkViewAccountActivityLinkPresent()
            self.AdminSpacePage.checkPasswordResetLinkPresent()
            time.sleep(5)
            self.AdminSpacePage.clickAddAsCuratorLink()
            self.AdminSpacePage.addRemark(data=self.data_reader.get_data(test_name, 'Remark'))
            status = self.AdminSpacePage.getSaveButtonStatus()
            if status == False:
                self.log.info("After enter Remark Save Button is Disable --Pass")
            else:
                self.log.info("After enter Remark Save Button is Enable --Fail")
            self.AdminSpacePage.clickIConfirmThisChangeCheckbox()
            self.AdminSpacePage.clickSaveButton()
            time.sleep(3)
            message=self.AdminSpacePage.getToastMessage()
            if message=='Explorer privileges have been updated!':
                self.log.info('Explorer privileges have been updated!')
            else:self.log.info('Toast Message not coming ')
            time.sleep(10)
            self.AdminSpacePage.checkManageExplorersPageheaderLabelPresent()
            self.AdminSpacePage.enterSearchBox(data=self.data_reader.get_data(test_name, 'SearchBox'))
            time.sleep(10)
            self.AdminSpacePage.clickThreeVerticalDotsLink()
            self.AdminSpacePage.checkViewProfileLinkPresent()
            self.AdminSpacePage.checkEditProfileLinkPresent()
            self.AdminSpacePage.checkRemoveAsCuratorLinkPresent()
            self.AdminSpacePage.checkViewAccountActivityLinkPresent()
            self.AdminSpacePage.checkPasswordResetLinkPresent()
            self.AdminSpacePage.clickDismissFilter()
            time.sleep(5)



    @allure.testcase("Verify unassigning user to curator role")
    @pytest.mark.order(24)
    @pytest.mark.smoke
    @allure.severity(allure.severity_level.MINOR)
    def test_VerifyUnassigningUserToCuratorRole(self):
        test_name = sys._getframe().f_code.co_name
        self.log.info("###### TEST EXECUTION STARTED :: " + test_name + " ######")
        with allure.step('Login in to the platform with an Admin credentials'):
            self.homeNavigation.clickAcceptCoockiesButton()
            self.homeNavigation.clickUserProfileIcon()
            self.loginPage.login()
            time.sleep(10)
            self.homeNavigation.clickUserProfileIcon()
            self.AdminSpacePage.clickAdminSpaceLink()
            time.sleep(10)
            self.AdminSpacePage.checkManageExplorersPageheaderLabelPresent()
            self.AdminSpacePage.enterSearchBox(data=self.data_reader.get_data(test_name, 'SearchBox'))
            time.sleep(10)
            self.AdminSpacePage.clickThreeVerticalDotsLink()
            self.AdminSpacePage.checkViewProfileLinkPresent()
            self.AdminSpacePage.checkEditProfileLinkPresent()
            self.AdminSpacePage.checkRemoveAsCuratorLinkPresent()
            self.AdminSpacePage.checkViewAccountActivityLinkPresent()
            self.AdminSpacePage.checkPasswordResetLinkPresent()
            time.sleep(5)
            self.AdminSpacePage.clickRemoveAsCuratorLink()
            self.AdminSpacePage.addRemark(data=self.data_reader.get_data(test_name, 'Remark'))
            status = self.AdminSpacePage.getSaveButtonStatus()
            if status == False:
                self.log.info("After enter Remark Save Button is Disable --Pass")
            else:
                self.log.info("After enter Remark Save Button is Enable --Fail")
            self.AdminSpacePage.clickIConfirmThisChangeCheckbox()
            self.AdminSpacePage.clickSaveButton()
            time.sleep(3)
            message = self.AdminSpacePage.getToastMessage()

            if message == 'Explorer privileges have been updated!':
                self.log.info('Explorer privileges have been updated!')
            else:
                self.log.info('Toast Message not coming ')

            time.sleep(10)
            self.AdminSpacePage.checkManageExplorersPageheaderLabelPresent()
            self.AdminSpacePage.enterSearchBox(data=self.data_reader.get_data(test_name, 'SearchBox'))
            time.sleep(10)
            self.AdminSpacePage.clickThreeVerticalDotsLink()
            self.AdminSpacePage.checkViewProfileLinkPresent()
            self.AdminSpacePage.checkEditProfileLinkPresent()
            self.AdminSpacePage.checkAddAsCuratorLinkPresent()
            self.AdminSpacePage.checkViewAccountActivityLinkPresent()
            self.AdminSpacePage.checkPasswordResetLinkPresent()
            self.AdminSpacePage.clickDismissFilter()
            time.sleep(5)

    @allure.testcase("Verify user assignment to Guide role")
    @pytest.mark.order(25)
    @pytest.mark.smoke
    @allure.severity(allure.severity_level.MINOR)
    def test_VerifyUserAssignmentToGuideRole(self):
        test_name = sys._getframe().f_code.co_name
        self.log.info("###### TEST EXECUTION STARTED :: " + test_name + " ######")
        with allure.step('Login in to the platform with an Admin credentials'):
            self.homeNavigation.clickAcceptCoockiesButton()
            self.homeNavigation.clickUserProfileIcon()
            self.loginPage.login()
            time.sleep(10)
            self.homeNavigation.clickUserProfileIcon()
            self.AdminSpacePage.clickAdminSpaceLink()
            time.sleep(10)
            self.AdminSpacePage.checkManageExplorersPageheaderLabelPresent()
            self.AdminSpacePage.enterSearchBox(data=self.data_reader.get_data(test_name, 'SearchBox'))
            time.sleep(10)
            self.AdminSpacePage.clickThreeVerticalDotsLink()
            self.AdminSpacePage.checkViewProfileLinkPresent()
            self.AdminSpacePage.checkEditProfileLinkPresent()
            self.AdminSpacePage.checkAddAsGuideLinkPresent()
            self.AdminSpacePage.checkViewAccountActivityLinkPresent()
            self.AdminSpacePage.checkPasswordResetLinkPresent()
            time.sleep(5)
            self.AdminSpacePage.clickAddAsGuideLink()
            self.AdminSpacePage.addRemark(data=self.data_reader.get_data(test_name, 'Remark'))
            status = self.AdminSpacePage.getSaveButtonStatus()
            if status == False:
                self.log.info("After enter Remark Save Button is Disable --Pass")
            else:
                self.log.info("After enter Remark Save Button is Enable --Fail")
            time.sleep(2)
            self.AdminSpacePage.clickIConfirmThisChangeCheckbox()
            self.AdminSpacePage.clickSaveButton()
            time.sleep(3)
            message = self.AdminSpacePage.getToastMessage()
            if message == 'Explorer privileges have been updated!':
                self.log.info('Explorer privileges have been updated!')
            else:
                self.log.info('Toast Message not coming ')
            time.sleep(10)
            self.AdminSpacePage.checkManageExplorersPageheaderLabelPresent()
            self.AdminSpacePage.enterSearchBox(data=self.data_reader.get_data(test_name, 'SearchBox'))
            time.sleep(10)
            self.AdminSpacePage.clickThreeVerticalDotsLink()
            self.AdminSpacePage.checkViewProfileLinkPresent()
            self.AdminSpacePage.checkEditProfileLinkPresent()
            self.AdminSpacePage.checkRemoveAsGuideLinkPresent()
            self.AdminSpacePage.checkViewAccountActivityLinkPresent()
            self.AdminSpacePage.checkPasswordResetLinkPresent()
            self.AdminSpacePage.clickDismissFilter()
            time.sleep(5)

    @allure.testcase("Verify unassigning user to Guide role")
    @pytest.mark.order(26)
    @pytest.mark.smoke
    @allure.severity(allure.severity_level.MINOR)
    def test_VerifyUnassigningUserToGuideRole(self):
        test_name = sys._getframe().f_code.co_name
        self.log.info("###### TEST EXECUTION STARTED :: " + test_name + " ######")
        with allure.step('Login in to the platform with an Admin credentials'):
            self.homeNavigation.clickAcceptCoockiesButton()
            self.homeNavigation.clickUserProfileIcon()
            self.loginPage.login()
            time.sleep(10)
            self.homeNavigation.clickUserProfileIcon()
            self.AdminSpacePage.clickAdminSpaceLink()
            time.sleep(10)
            self.AdminSpacePage.checkManageExplorersPageheaderLabelPresent()
            self.AdminSpacePage.enterSearchBox(data=self.data_reader.get_data(test_name, 'SearchBox'))
            time.sleep(10)
            self.AdminSpacePage.clickThreeVerticalDotsLink()
            self.AdminSpacePage.checkViewProfileLinkPresent()
            self.AdminSpacePage.checkEditProfileLinkPresent()
            self.AdminSpacePage.checkRemoveAsGuideLinkPresent()
            self.AdminSpacePage.checkViewAccountActivityLinkPresent()
            self.AdminSpacePage.checkPasswordResetLinkPresent()
            time.sleep(5)
            self.AdminSpacePage.clickRemoveAsGuideLink()
            self.AdminSpacePage.addRemark(data=self.data_reader.get_data(test_name, 'Remark'))
            status = self.AdminSpacePage.getSaveButtonStatus()
            if status == False:
                self.log.info("After enter Remark Save Button is Disable --Pass")
            else:
                self.log.info("After enter Remark Save Button is Enable --Fail")
            time.sleep(2)
            self.AdminSpacePage.clickIConfirmThisChangeCheckbox()
            self.AdminSpacePage.clickSaveButton()
            time.sleep(3)
            message = self.AdminSpacePage.getToastMessage()

            if message == 'Explorer privileges have been updated!':
                self.log.info('Explorer privileges have been updated!')
            else:
                self.log.info('Toast Message not coming ')

            time.sleep(10)
            self.AdminSpacePage.checkManageExplorersPageheaderLabelPresent()
            self.AdminSpacePage.enterSearchBox(data=self.data_reader.get_data(test_name, 'SearchBox'))
            time.sleep(10)
            self.AdminSpacePage.clickThreeVerticalDotsLink()
            self.AdminSpacePage.checkViewProfileLinkPresent()
            self.AdminSpacePage.checkEditProfileLinkPresent()
            self.AdminSpacePage.checkAddAsGuideLinkPresent()
            self.AdminSpacePage.checkViewAccountActivityLinkPresent()
            self.AdminSpacePage.checkPasswordResetLinkPresent()
            self.AdminSpacePage.clickDismissFilter()
            time.sleep(5)

    @allure.testcase("Verify user assignment to Admin role")
    @pytest.mark.order(27)
    @pytest.mark.smoke
    @allure.severity(allure.severity_level.MINOR)
    def test_VerifyUserAssignmentToAdminRole(self):
        test_name = sys._getframe().f_code.co_name
        self.log.info("###### TEST EXECUTION STARTED :: " + test_name + " ######")
        with allure.step('Login in to the platform with an Admin credentials'):
            self.homeNavigation.clickAcceptCoockiesButton()
            self.homeNavigation.clickUserProfileIcon()
            self.loginPage.login()
            time.sleep(10)
            self.homeNavigation.clickUserProfileIcon()
            self.AdminSpacePage.clickAdminSpaceLink()
            time.sleep(10)
            self.AdminSpacePage.checkManageExplorersPageheaderLabelPresent()
            self.AdminSpacePage.enterSearchBox(data=self.data_reader.get_data(test_name, 'SearchBox'))
            time.sleep(10)
            self.AdminSpacePage.clickThreeVerticalDotsLink()
            self.AdminSpacePage.checkViewProfileLinkPresent()
            self.AdminSpacePage.checkEditProfileLinkPresent()
            self.AdminSpacePage.checkAddAsAdminLinkPresent()
            self.AdminSpacePage.checkViewAccountActivityLinkPresent()
            self.AdminSpacePage.checkPasswordResetLinkPresent()
            time.sleep(5)
            self.AdminSpacePage.clickAddAsAdminLink()
            self.AdminSpacePage.addRemark(data=self.data_reader.get_data(test_name, 'Remark'))
            status = self.AdminSpacePage.getSaveButtonStatus()
            if status == False:
                self.log.info("After enter Remark Save Button is Disable --Pass")
            else:
                self.log.info("After enter Remark Save Button is Enable --Fail")
            time.sleep(2)
            self.AdminSpacePage.clickIConfirmThisChangeCheckbox()
            self.AdminSpacePage.clickSaveButton()
            time.sleep(3)
            message = self.AdminSpacePage.getToastMessage()
            if message == 'Explorer privileges have been updated!':
                self.log.info('Explorer privileges have been updated!')
            else:
                self.log.info('Toast Message not coming ')
            time.sleep(10)
            self.AdminSpacePage.checkManageExplorersPageheaderLabelPresent()
            self.AdminSpacePage.enterSearchBox(data=self.data_reader.get_data(test_name, 'SearchBox'))
            time.sleep(10)
            self.AdminSpacePage.clickThreeVerticalDotsLink()
            self.AdminSpacePage.checkViewProfileLinkPresent()
            self.AdminSpacePage.checkEditProfileLinkPresent()
            self.AdminSpacePage.checkRemoveAsAdminLinkPresent()
            self.AdminSpacePage.checkViewAccountActivityLinkPresent()
            self.AdminSpacePage.checkPasswordResetLinkPresent()
            self.AdminSpacePage.clickDismissFilter()
            time.sleep(5)

    @allure.testcase("Verify lock user account function")
    @pytest.mark.order(28)
    @pytest.mark.smoke
    @allure.severity(allure.severity_level.MINOR)
    def test_VerifyLockUserAccountFunction(self):
        test_name = sys._getframe().f_code.co_name
        self.log.info("###### TEST EXECUTION STARTED :: " + test_name + " ######")
        with allure.step('Login in to the platform with an Admin credentials'):
            self.homeNavigation.clickAcceptCoockiesButton()
            self.homeNavigation.clickUserProfileIcon()
            self.loginPage.login()
            time.sleep(10)
            self.homeNavigation.clickUserProfileIcon()
            self.AdminSpacePage.clickAdminSpaceLink()
            time.sleep(10)
            self.AdminSpacePage.checkManageExplorersPageheaderLabelPresent()
            self.AdminSpacePage.enterSearchBox(data=self.data_reader.get_data(test_name, 'SearchBox'))
            time.sleep(10)
            self.AdminSpacePage.clickThreeVerticalDotsLink()
            self.AdminSpacePage.checkViewProfileLinkPresent()
            self.AdminSpacePage.checkEditProfileLinkPresent()
            self.AdminSpacePage.checkLockExplorerLinkPresent()
            self.AdminSpacePage.checkViewAccountActivityLinkPresent()
            self.AdminSpacePage.checkPasswordResetLinkPresent()
            time.sleep(5)
            self.AdminSpacePage.clickLockExplorerLink()
            time.sleep(2)
            self.AdminSpacePage.addRemark(data=self.data_reader.get_data(test_name, 'Remark'))
            status = self.AdminSpacePage.getSaveButtonStatus()
            if status == False:
                self.log.info("After enter Remark Save Button is Disable --Pass")
            else:
                self.log.info("After enter Remark Save Button is Enable --Fail")
            time.sleep(2)
            self.AdminSpacePage.clickIConfirmThisChangeCheckbox()
            self.AdminSpacePage.clickSaveButton()
            time.sleep(3)
            message = self.AdminSpacePage.getToastMessage()

            if message == 'Explorer privileges have been updated!':
                self.log.info('Explorer privileges have been updated!')
            else:
                self.log.info('Toast Message not coming ')

            time.sleep(10)
            self.AdminSpacePage.checkManageExplorersPageheaderLabelPresent()
            self.AdminSpacePage.enterSearchBox(data=self.data_reader.get_data(test_name, 'SearchBox'))
            time.sleep(10)
            self.AdminSpacePage.clickThreeVerticalDotsLink()
            self.AdminSpacePage.checkViewProfileLinkPresent()
            self.AdminSpacePage.checkEditProfileLinkPresent()
            self.AdminSpacePage.checkUnlockExplorerLinkPresent()
            self.AdminSpacePage.checkViewAccountActivityLinkPresent()
            self.AdminSpacePage.checkPasswordResetLinkPresent()
            self.AdminSpacePage.clickViewAccountActivityLink()
            self.AdminSpacePage.checkViewAccountActivityPageHeaderPresent()
            activityType=self.AdminSpacePage.getViewAccountActivityType()
            if activityType=='Locked Explorer':
                self.log.info("user is locked")
            else:self.log.info("user is Not locked")
            activityRemark=self.AdminSpacePage.getViewAccountActivityRemark()
            if activityRemark==self.data_reader.get_data(test_name, 'Remark'):
                self.log.info("Remark is correct")
            else:self.log.info("Remark is Not correct")
            time.sleep(2)
            self.AdminSpacePage.clickCancelButton()

            time.sleep(5)

    @allure.testcase("Verify that a locked user cannot access the platform")
    @pytest.mark.order(29)
    @pytest.mark.smoke
    @allure.severity(allure.severity_level.MINOR)
    def test_VerifyThatALockedUserCannotAccessThePlatform(self):
        test_name = sys._getframe().f_code.co_name
        self.log.info("###### TEST EXECUTION STARTED :: " + test_name + " ######")
        with allure.step('Login in to the platform with locked Explorer account'):
            self.homeNavigation.clickAcceptCoockiesButton()
            self.homeNavigation.clickUserProfileIcon()
            self.loginPage.login(email=self.data_reader.get_data(test_name, 'UserName'),password=self.data_reader.get_data(test_name, 'Password'))
            time.sleep(3)
            message = self.AdminSpacePage.getToastMessage()
            if message==self.data_reader.get_data(test_name, 'Text_Message'):
                self.log.info("locked user can't access the platform")
            else:self.log.info("locked user can access the platform")



    @allure.testcase("Verify unlock user account function")
    @pytest.mark.order(30)
    @pytest.mark.smoke
    @allure.severity(allure.severity_level.MINOR)
    def test_VerifyUnlockUserAccountFunction(self):
        test_name = sys._getframe().f_code.co_name
        self.log.info("###### TEST EXECUTION STARTED :: " + test_name + " ######")
        with allure.step('Login in to the platform with an Admin credentials'):
            self.homeNavigation.clickAcceptCoockiesButton()
            self.homeNavigation.clickUserProfileIcon()
            self.loginPage.login()
            time.sleep(10)
            self.homeNavigation.clickUserProfileIcon()
            self.AdminSpacePage.clickAdminSpaceLink()
            time.sleep(10)
            self.AdminSpacePage.checkManageExplorersPageheaderLabelPresent()
            self.AdminSpacePage.enterSearchBox(data=self.data_reader.get_data(test_name, 'SearchBox'))
            time.sleep(10)
            self.AdminSpacePage.clickThreeVerticalDotsLink()
            self.AdminSpacePage.checkViewProfileLinkPresent()
            self.AdminSpacePage.checkEditProfileLinkPresent()
            self.AdminSpacePage.checkUnlockExplorerLinkPresent()
            self.AdminSpacePage.checkViewAccountActivityLinkPresent()
            self.AdminSpacePage.checkPasswordResetLinkPresent()
            time.sleep(5)
            self.AdminSpacePage.clickUnlockExplorerLink()
            time.sleep(2)
            self.AdminSpacePage.addRemark(data=self.data_reader.get_data(test_name, 'Remark'))
            status = self.AdminSpacePage.getSaveButtonStatus()
            if status == False:
                self.log.info("After enter Remark Save Button is Disable --Pass")
            else:
                self.log.info("After enter Remark Save Button is Enable --Fail")
            time.sleep(2)
            self.AdminSpacePage.clickIConfirmThisChangeCheckbox()
            self.AdminSpacePage.clickSaveButton()
            time.sleep(3)
            message = self.AdminSpacePage.getToastMessage()

            if message == 'Explorer privileges have been updated!':
                self.log.info('Explorer privileges have been updated!')
            else:
                self.log.info('Toast Message not coming ')

            time.sleep(10)
            self.AdminSpacePage.checkManageExplorersPageheaderLabelPresent()
            self.AdminSpacePage.enterSearchBox(data=self.data_reader.get_data(test_name, 'SearchBox'))
            time.sleep(10)
            self.AdminSpacePage.clickThreeVerticalDotsLink()
            self.AdminSpacePage.checkViewProfileLinkPresent()
            self.AdminSpacePage.checkEditProfileLinkPresent()
            self.AdminSpacePage.checkLockExplorerLinkPresent()
            self.AdminSpacePage.checkViewAccountActivityLinkPresent()
            self.AdminSpacePage.checkPasswordResetLinkPresent()
            self.AdminSpacePage.clickViewAccountActivityLink()
            self.AdminSpacePage.checkViewAccountActivityPageHeaderPresent()
            activityType = self.AdminSpacePage.getViewAccountActivityType()
            if activityType == 'Unlocked Explorer':
                self.log.info("user is Unlocked")
            else:
                self.log.info("user is still locked")
            activityRemark = self.AdminSpacePage.getViewAccountActivityRemark()
            if activityRemark == self.data_reader.get_data(test_name, 'Remark'):
                self.log.info("Remark is correct")
            else:
                self.log.info("Remark is Not correct")
            time.sleep(2)
            self.AdminSpacePage.clickCancelButton()

            time.sleep(5)

    @allure.testcase("Verify that an unlocked user can access the platform")
    @pytest.mark.order(31)
    @pytest.mark.smoke
    @allure.severity(allure.severity_level.MINOR)
    def test_VerifyThatAnUnlockedUserCanAccessThePlatform(self):
        test_name = sys._getframe().f_code.co_name
        self.log.info("###### TEST EXECUTION STARTED :: " + test_name + " ######")
        with allure.step('Login in to the platform with unlocked Explorer account'):
            self.homeNavigation.clickAcceptCoockiesButton()
            self.homeNavigation.clickUserProfileIcon()
            self.loginPage.login(email=self.data_reader.get_data(test_name, 'UserName'),
                                 password=self.data_reader.get_data(test_name, 'Password'))
            time.sleep(3)
            message = self.AdminSpacePage.getToastMessage()
            self.log.info(message)
            if message == self.data_reader.get_data(test_name, 'Text_Message'):
                self.log.info("Unlocked user can access the platform")
            else:
                self.log.info("Unlocked user can't access the platform")


    @allure.testcase("Verify unassigning user to Admin role")
    @pytest.mark.order(32)
    @pytest.mark.smoke
    @allure.severity(allure.severity_level.MINOR)
    def test_VerifyUnassigningUserToAdminRole(self):
        test_name = sys._getframe().f_code.co_name
        self.log.info("###### TEST EXECUTION STARTED :: " + test_name + " ######")
        with allure.step('Login in to the platform with an Admin credentials'):
            self.homeNavigation.clickAcceptCoockiesButton()
            self.homeNavigation.clickUserProfileIcon()
            self.loginPage.login()
            time.sleep(10)
            self.homeNavigation.clickUserProfileIcon()
            self.AdminSpacePage.clickAdminSpaceLink()
            time.sleep(10)
            self.AdminSpacePage.checkManageExplorersPageheaderLabelPresent()
            self.AdminSpacePage.enterSearchBox(data=self.data_reader.get_data(test_name, 'SearchBox'))
            time.sleep(10)
            self.AdminSpacePage.clickThreeVerticalDotsLink()
            self.AdminSpacePage.checkViewProfileLinkPresent()
            self.AdminSpacePage.checkEditProfileLinkPresent()
            self.AdminSpacePage.checkRemoveAsAdminLinkPresent()
            self.AdminSpacePage.checkViewAccountActivityLinkPresent()
            self.AdminSpacePage.checkPasswordResetLinkPresent()
            time.sleep(5)
            self.AdminSpacePage.clickRemoveAsAdminLink()
            self.AdminSpacePage.addRemark(data=self.data_reader.get_data(test_name, 'Remark'))
            status = self.AdminSpacePage.getSaveButtonStatus()
            if status == False:
                self.log.info("After enter Remark Save Button is Disable --Pass")
            else:
                self.log.info("After enter Remark Save Button is Enable --Fail")
            time.sleep(2)
            self.AdminSpacePage.clickIConfirmThisChangeCheckbox()
            self.AdminSpacePage.clickSaveButton()
            time.sleep(3)
            message = self.AdminSpacePage.getToastMessage()

            if message == 'Explorer privileges have been updated!':
                self.log.info('Explorer privileges have been updated!')
            else:
                self.log.info('Toast Message not coming ')

            time.sleep(10)


    @allure.testcase("Verify data displayed in Manage Guide page")
    @pytest.mark.order(33)
    @pytest.mark.smoke
    @allure.severity(allure.severity_level.MINOR)
    def test_VerifyDataDisplayedInManageGuidePage(self):
        test_name = sys._getframe().f_code.co_name
        self.log.info("###### TEST EXECUTION STARTED :: " + test_name + " ######")
        with allure.step('Login in to the platform with an Admin credentials'):
            self.homeNavigation.clickAcceptCoockiesButton()
            self.homeNavigation.clickUserProfileIcon()
            self.loginPage.login()
            time.sleep(10)
            self.homeNavigation.clickUserProfileIcon()
            self.AdminSpacePage.clickAdminSpaceLink()
            time.sleep(5)
            self.AdminSpacePage.clickManageGuidesLink()
            time.sleep(5)
            self.AdminSpacePage.checkManageGuidesPageheaderLabelPresent()
            self.AdminSpacePage.enterSearchBox(data=self.data_reader.get_data(test_name, 'SearchBox'))
            time.sleep(5)
            self.AdminSpacePage.clickThreeVerticalDotsLink()
            self.AdminSpacePage.checkViewProfileLinkPresent()
            self.AdminSpacePage.checkRemoveAsGuideLinkPresent()
            self.AdminSpacePage.checkViewGuidedExplorersLinkPresent()
            self.AdminSpacePage.checkViewAccountActivityLinkPresent()
            self.AdminSpacePage.clickDismissFilter()
            time.sleep(5)
            self.AdminSpacePage.clickNameOfGuidedExplorers()
            time.sleep(2)
            self.AdminSpacePage.clickCancelButton()
            time.sleep(2)
            self.AdminSpacePage.checkManageGuidesPageheaderLabelPresent()
            self.AdminSpacePage.clickThreeVerticalDotsLink()
            self.AdminSpacePage.clickViewProfileLink()
            time.sleep(2)
            self.AdminSpacePage.clickCancelButton()
            time.sleep(2)
            self.AdminSpacePage.checkManageGuidesPageheaderLabelPresent()
            time.sleep(5)


    @allure.testcase("Verify Guide search result as per the Order By value")
    @pytest.mark.order(34)
    @pytest.mark.smoke
    @allure.severity(allure.severity_level.MINOR)
    def test_VerifyGuideSearchResultAsPerTheOrderByValue(self):
        test_name = sys._getframe().f_code.co_name
        self.log.info("###### TEST EXECUTION STARTED :: " + test_name + " ######")
        with allure.step('Login in to the platform with an Admin credentials'):
            self.homeNavigation.clickAcceptCoockiesButton()
            self.homeNavigation.clickUserProfileIcon()
            self.loginPage.login()
            time.sleep(10)
            self.homeNavigation.clickUserProfileIcon()
            self.AdminSpacePage.clickAdminSpaceLink()
            time.sleep(5)
            self.AdminSpacePage.clickManageGuidesLink()
            time.sleep(5)
            self.AdminSpacePage.checkManageGuidesPageheaderLabelPresent()
            elements=self.AdminSpacePage.checkTotalCardCounts()
            self.log.info(len(elements))
            time.sleep(5)
            self.AdminSpacePage.clickFilterLink()
            element = self.AdminSpacePage.checkFilterorderByCheckboxStatus()
            if element == False:
                self.AdminSpacePage.clickFilterorderByCheckbox()
                time.sleep(5)
                self.AdminSpacePage.selectorderByOption(selector='0')
                time.sleep(5)
                self.AdminSpacePage.clickFilterGoButton()
            self.AdminSpacePage.clickDismissFilter()
            time.sleep(5)
            elements = self.AdminSpacePage.checkTotalCardCounts()
            self.log.info(len(elements))
            time.sleep(5)
            self.AdminSpacePage.clickFilterLink()
            element = self.AdminSpacePage.checkFilterorderByCheckboxStatus()
            if element == True:
                time.sleep(5)
                self.AdminSpacePage.selectorderByOption(selector='1')
                time.sleep(5)
                self.AdminSpacePage.clickFilterGoButton()
            self.AdminSpacePage.clickDismissFilter()
            time.sleep(5)
            elements = self.AdminSpacePage.checkTotalCardCounts()
            self.log.info(len(elements))
            time.sleep(5)

            self.AdminSpacePage.clickFilterLink()
            element = self.AdminSpacePage.checkFilterorderByCheckboxStatus()
            if element == True:
                time.sleep(5)
                self.AdminSpacePage.selectorderByOption(selector='2')
                time.sleep(5)
                self.AdminSpacePage.clickFilterGoButton()
            self.AdminSpacePage.clickDismissFilter()
            time.sleep(5)
            elements = self.AdminSpacePage.checkTotalCardCounts()
            self.log.info(len(elements))

            time.sleep(5)
            self.AdminSpacePage.clickFilterLink()
            element = self.AdminSpacePage.checkFilterorderByCheckboxStatus()
            if element == True:
                time.sleep(5)
                self.AdminSpacePage.selectorderByOption(selector='3')
                time.sleep(5)
                self.AdminSpacePage.clickFilterGoButton()
            self.AdminSpacePage.clickDismissFilter()
            time.sleep(5)
            elements = self.AdminSpacePage.checkTotalCardCounts()
            self.log.info(len(elements))
            time.sleep(10)

    @allure.testcase("Verify search results displayed when filtered by Guides having active Guided Explorer relationship")
    @pytest.mark.order(35)
    @pytest.mark.smoke
    @allure.severity(allure.severity_level.MINOR)
    def test_VerifySearchResultsDisplayedWhenFilteredByGuidesHavingActiveGuidedExplorerRelationship(self):
        test_name = sys._getframe().f_code.co_name
        self.log.info("###### TEST EXECUTION STARTED :: " + test_name + " ######")
        with allure.step('Login in to the platform with an Admin credentials'):
            self.homeNavigation.clickAcceptCoockiesButton()
            self.homeNavigation.clickUserProfileIcon()
            self.loginPage.login()
            time.sleep(10)
            self.homeNavigation.clickUserProfileIcon()
            self.AdminSpacePage.clickAdminSpaceLink()
            time.sleep(5)
            self.AdminSpacePage.clickManageGuidesLink()
            time.sleep(5)
            self.AdminSpacePage.checkManageGuidesPageheaderLabelPresent()
            self.AdminSpacePage.clickFilterLink()
            time.sleep(2)
            self.AdminSpacePage.clickWithActiveGuidedExplorersCheckbox()
            time.sleep(2)
            self.AdminSpacePage.clickFilterGoButton()
            time.sleep(3)
            self.AdminSpacePage.clickDismissFilter()
            time.sleep(10)
            self.AdminSpacePage.checkWithActiveGuidedExplorers()
            time.sleep(10)
            self.AdminSpacePage.clickFilterLink()
            time.sleep(2)
            self.AdminSpacePage.clickFilterResetButton()
            time.sleep(2)
            self.AdminSpacePage.clickWithOutActiveGuidedExplorersCheckbox()
            time.sleep(2)
            self.AdminSpacePage.clickFilterGoButton()
            time.sleep(3)
            self.AdminSpacePage.clickDismissFilter()
            time.sleep(10)
            self.AdminSpacePage.checkWithOutActiveGuidedExplorers()
            time.sleep(10)




