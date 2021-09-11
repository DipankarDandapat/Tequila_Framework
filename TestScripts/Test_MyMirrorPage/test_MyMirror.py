from FrameworkUtilities.teststatus_utility import test_Status
from PageObjects.LoginPage.login_page import LoginPage
from FrameworkUtilities.data_reader_utility import DataReader
import unittest
import pytest
import sys
import allure
from PageObjects.HomeNavigation.home_navigation import HomeNavigation
from PageObjects.MyMirror.my_mirror_page import MyMirror
import FrameworkUtilities.logger_utility as log_utils
import logging
import time


@pytest.mark.usefixtures("get_driver", "initialize")
@allure.story('Test Automation Demo ')
@allure.feature('Verification Using Requests')
class MyMirrorTest(unittest.TestCase):
    log = log_utils.custom_logger(logging.INFO)
    data_reader = DataReader()

    @pytest.fixture(scope='function')
    def initialize(self):
        self.homeNavigation = HomeNavigation(self.driver)
        self.loginPage = LoginPage(self.driver)
        self.MyMirrorPage = MyMirror(self.driver)
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


    @allure.testcase("Verify that the Mirror help video is avaiable for users on Mirror Overview page")
    @pytest.mark.order(1)
    @pytest.mark.smoke
    @allure.severity(allure.severity_level.MINOR)
    def test_VerifyThatTheMirrorHelpVideoIsAvaiableForUsersOnMirrorOverviewPage(self):
        test_name = sys._getframe().f_code.co_name
        self.log.info("###### TEST EXECUTION STARTED :: " + test_name + " ######")
        with allure.step('Navigate to login page'):
            self.homeNavigation.clickAcceptCoockiesButton()
            self.homeNavigation.clickUserProfileIcon()
            self.loginPage.login()
            time.sleep(10)
        with allure.step('Navigate to MyMirror page'):
            self.homeNavigation.clickMainToolNavDot()
            self.homeNavigation.clickMyMirror()
            time.sleep(2)
            self.MyMirrorPage.clickViewAnExampleButton()
            time.sleep(2)
            self.MyMirrorPage.clickCrossButton()


    @allure.testcase("Verify ability to save a draft reflection")
    @pytest.mark.order(2)
    @pytest.mark.smoke
    @allure.severity(allure.severity_level.MINOR)
    def test_VerifyAbilityToSaveADraftReflection(self):
        test_name = sys._getframe().f_code.co_name
        self.log.info("###### TEST EXECUTION STARTED :: " + test_name + " ######")
        with allure.step('Navigate to login page'):
            self.homeNavigation.clickAcceptCoockiesButton()
            self.homeNavigation.clickUserProfileIcon()
            self.loginPage.login()
            time.sleep(10)
        with allure.step('Navigate to MyMirror page'):
            self.homeNavigation.clickMainToolNavDot()
            self.homeNavigation.clickMyMirror()
            time.sleep(2)
            self.MyMirrorPage.clickAddAReflectionLink()
            self.MyMirrorPage.addOnTextbox(data=self.data_reader.get_data(test_name, 'TextBox'))
            self.MyMirrorPage.clickNextButton()
            time.sleep(2)
            self.MyMirrorPage.clickMyReflectionslink()
            time.sleep(2)
            self.MyMirrorPage.checkWithDraftReflection()
            time.sleep(2)

    @allure.testcase("Verify ability to edit draft reflections and continue to save as draft")
    @pytest.mark.order(3)
    @pytest.mark.smoke
    @allure.severity(allure.severity_level.MINOR)
    def test_VerifyAbilityToEditDraftReflectionsAndContinueToSaveAsDraft(self):
        test_name = sys._getframe().f_code.co_name
        self.log.info("###### TEST EXECUTION STARTED :: " + test_name + " ######")
        with allure.step('Navigate to login page'):
            self.homeNavigation.clickAcceptCoockiesButton()
            self.homeNavigation.clickUserProfileIcon()
            self.loginPage.login()
            time.sleep(10)
        with allure.step('Navigate to MyMirror page'):
            self.homeNavigation.clickMainToolNavDot()
            self.homeNavigation.clickMyMirror()
            time.sleep(2)
            self.MyMirrorPage.clickAddAReflectionLink()
            self.MyMirrorPage.addOnTextbox(data=self.data_reader.get_data(test_name, 'TextBox'))
            self.MyMirrorPage.clickNextButton()
            time.sleep(2)
            self.MyMirrorPage.clickMyReflectionslink()
            time.sleep(2)
            self.MyMirrorPage.checkWithDraftReflection()
            self.MyMirrorPage.editInProgressReflection()
            time.sleep(5)

    @allure.testcase("Verify that previously answered questions in a draft reflection can be changed")
    @pytest.mark.order(4)
    @pytest.mark.smoke
    @allure.severity(allure.severity_level.MINOR)
    def test_VerifyThatPreviouslyAnsweredQuestionsInADraftReflectionCanBeChanged(self):
        test_name = sys._getframe().f_code.co_name
        self.log.info("###### TEST EXECUTION STARTED :: " + test_name + " ######")
        with allure.step('Navigate to login page'):
            self.homeNavigation.clickAcceptCoockiesButton()
            self.homeNavigation.clickUserProfileIcon()
            self.loginPage.login()
            time.sleep(10)
        with allure.step('Navigate to MyMirror page'):
            self.homeNavigation.clickMainToolNavDot()
            self.homeNavigation.clickMyMirror()
            time.sleep(2)
            self.MyMirrorPage.clickAddAReflectionLink()
            self.MyMirrorPage.addOnTextbox(data=self.data_reader.get_data(test_name, 'TextBox'))
            self.MyMirrorPage.clickNextButton()
            time.sleep(2)
            self.MyMirrorPage.clickMyReflectionslink()
            time.sleep(2)
            self.MyMirrorPage.checkWithDraftReflection()
            self.MyMirrorPage.editInProgressReflection()
            time.sleep(5)
            self.MyMirrorPage.addOnTextbox(data=self.data_reader.get_data(test_name, 'TextBox'))
            time.sleep(2)
            self.MyMirrorPage.clickNextButton()
            time.sleep(2)
            self.MyMirrorPage.clickMyReflectionslink()
            time.sleep(2)

    @allure.testcase("Verify that a draft reflection can be completed and successfully submitted as a completed entry")
    @pytest.mark.order(5)
    @pytest.mark.smoke
    @allure.severity(allure.severity_level.MINOR)
    def test_VerifyThataDraftReflectionCanBeCompletedAndSuccessfullySubmittedAsACompletedEntry(self):
        test_name = sys._getframe().f_code.co_name
        self.log.info("###### TEST EXECUTION STARTED :: " + test_name + " ######")
        with allure.step('Navigate to login page'):
            self.homeNavigation.clickAcceptCoockiesButton()
            self.homeNavigation.clickUserProfileIcon()
            self.loginPage.login()
            time.sleep(10)
        with allure.step('Navigate to MyMirror page'):
            self.homeNavigation.clickMainToolNavDot()
            self.homeNavigation.clickMyMirror()
            time.sleep(2)
            self.MyMirrorPage.clickAddAReflectionLink()
            self.MyMirrorPage.addOnTextbox(data=self.data_reader.get_data(test_name, 'TextBox'))
            self.MyMirrorPage.clickNextButton()
            time.sleep(2)
            self.MyMirrorPage.clickMyReflectionslink()
            time.sleep(5)
            self.MyMirrorPage.editInProgressReflection()
            time.sleep(5)
            self.MyMirrorPage.clickNextButton()
            listofWords = self.MyMirrorPage.feelingWordsList()
            count = len(listofWords)
            self.log.info(count)
            time.sleep(5)

            for i in range(count):
                time.sleep(2)
                if listofWords[i].text == "Thrilled":
                    listofWords[i].click()
                    time.sleep(2)
                    break

            self.MyMirrorPage.clickNextButton()
            time.sleep(5)
            self.MyMirrorPage.addOnTextbox(data=self.data_reader.get_data(test_name, 'TextBox'))
            self.MyMirrorPage.clickNextButton()
            time.sleep(5)
            self.MyMirrorPage.addOnTextbox(data=self.data_reader.get_data(test_name, 'TextBox'))
            self.MyMirrorPage.clickNextButton()
            time.sleep(5)
            self.MyMirrorPage.addOnTextarea(data=self.data_reader.get_data(test_name, 'TextBox'))
            self.MyMirrorPage.clickNextButton()
            time.sleep(5)
            listoftopics = self.MyMirrorPage.topicsList()
            count = len(listoftopics)
            self.log.info(count)
            time.sleep(5)
            for i in range(count):
                time.sleep(2)
                if listoftopics[i].text == "Life-work balance":
                    listoftopics[i].click()
                    time.sleep(2)
                    break

            self.MyMirrorPage.clickSubmitButton()
            time.sleep(3)
            message = self.MyMirrorPage.getToastMessage()
            self.log.info(message)

    @allure.testcase("Verify that a completed reflection is not editable")
    @pytest.mark.order(6)
    @pytest.mark.smoke
    @allure.severity(allure.severity_level.MINOR)
    def test_VerifyThataACompletedReflectionIsNotEditable(self):
        test_name = sys._getframe().f_code.co_name
        self.log.info("###### TEST EXECUTION STARTED :: " + test_name + " ######")
        with allure.step('Navigate to login page'):
            self.homeNavigation.clickAcceptCoockiesButton()
            self.homeNavigation.clickUserProfileIcon()
            self.loginPage.login()
            time.sleep(10)
        with allure.step('Navigate to MyMirror page'):
            self.homeNavigation.clickMainToolNavDot()
            self.homeNavigation.clickMyMirror()
            time.sleep(5)
            self.MyMirrorPage.clickMyReflectionslink()
            time.sleep(5)
            self.MyMirrorPage.editCompletedReflection()

    @allure.testcase("Veriy if feeling word selection is limited to max 6 values")
    @pytest.mark.order(7)
    @pytest.mark.smoke
    @allure.severity(allure.severity_level.MINOR)
    def test_VeriyIfFeelingWordSelectionIsLimitedToMax_6_Values(self):
        test_name = sys._getframe().f_code.co_name
        self.log.info("###### TEST EXECUTION STARTED :: " + test_name + " ######")
        with allure.step('Navigate to login page'):
            self.homeNavigation.clickAcceptCoockiesButton()
            self.homeNavigation.clickUserProfileIcon()
            self.loginPage.login()
            time.sleep(10)
        with allure.step('Navigate to MyMirror page'):
            self.homeNavigation.clickMainToolNavDot()
            self.homeNavigation.clickMyMirror()
            self.MyMirrorPage.clickAddAReflectionLink()
            self.MyMirrorPage.addOnTextbox(data=self.data_reader.get_data(test_name, 'TextBox'))
            self.MyMirrorPage.clickNextButton()
            listofWords = self.MyMirrorPage.feelingWordsList()
            for row in listofWords:
                if row.text in ["Relieved", "Confident", "Curious", "Hopeful", "Happy", "Inspired", "Excited"]:
                    time.sleep(1)
                    row.click()
            time.sleep(2)
            message = self.MyMirrorPage.getToastMessage()
            if message == "You may select up to six feeling words only.":
                self.log.info("feeling word selection is limited to max 6 values")
            else:
                self.log.info("feeling word selection is Not limited to 6 values")


    @allure.testcase("Verify if reason for each feeling selected is captured")
    @pytest.mark.order(8)
    @pytest.mark.smoke
    @allure.severity(allure.severity_level.MINOR)
    def test_VerifyifReasonForEachFeelingSelectedIsCaptured(self):
        test_name = sys._getframe().f_code.co_name
        self.log.info("###### TEST EXECUTION STARTED :: " + test_name + " ######")
        with allure.step('Navigate to login page'):
            self.homeNavigation.clickAcceptCoockiesButton()
            self.homeNavigation.clickUserProfileIcon()
            self.loginPage.login()
            time.sleep(10)
        with allure.step('Navigate to MyMirror page'):
            self.homeNavigation.clickMainToolNavDot()
            self.homeNavigation.clickMyMirror()
            self.MyMirrorPage.clickAddAReflectionLink()
            self.MyMirrorPage.addOnTextbox(data=self.data_reader.get_data(test_name, 'TextBox'))
            self.MyMirrorPage.clickNextButton()
            listofWords = self.MyMirrorPage.feelingWordsList()
            L1=["Relieved", "Confident", "Curious", "Hopeful", "Happy", "Inspired"]
            for row in listofWords:
                if row.text in L1:
                    time.sleep(1)
                    row.click()
            time.sleep(2)
            self.MyMirrorPage.clickNextButton()
            feeling_words=self.MyMirrorPage.getFeelingWordsCaptured()
            list_offeeling_words= feeling_words.split(", ")
            self.log.info(L1)
            self.log.info(list_offeeling_words)
            time.sleep(3)



    @allure.testcase("Verify tagging of a reflection")
    @pytest.mark.order(9)
    @pytest.mark.smoke
    @allure.severity(allure.severity_level.MINOR)
    def test_VerifyTaggingOfAReflection(self):
        test_name = sys._getframe().f_code.co_name
        self.log.info("###### TEST EXECUTION STARTED :: " + test_name + " ######")
        with allure.step('Navigate to login page'):
            self.homeNavigation.clickAcceptCoockiesButton()
            self.homeNavigation.clickUserProfileIcon()
            self.loginPage.login()
            time.sleep(10)
        with allure.step('Navigate to MyMirror page'):
            self.homeNavigation.clickMainToolNavDot()
            self.homeNavigation.clickMyMirror()
            self.MyMirrorPage.clickAddAReflectionLink()
            self.MyMirrorPage.addOnTextbox(data=self.data_reader.get_data(test_name, 'TextBox'))
            self.MyMirrorPage.clickNextButton()
            listofWords = self.MyMirrorPage.feelingWordsList()
            L1=["Relieved", "Confident", "Curious", "Hopeful", "Happy"]
            for row in listofWords:
                if row.text in L1:
                    time.sleep(1)
                    row.click()
            time.sleep(2)
            self.MyMirrorPage.clickNextButton()
            time.sleep(2)
            self.MyMirrorPage.addOnTextbox(data=self.data_reader.get_data(test_name, 'TextBox'))
            self.MyMirrorPage.clickNextButton()
            time.sleep(2)
            self.MyMirrorPage.addOnTextbox(data=self.data_reader.get_data(test_name, 'TextBox'))
            self.MyMirrorPage.clickNextButton()
            time.sleep(2)
            self.MyMirrorPage.addOnTextarea(data=self.data_reader.get_data(test_name, 'TextBox'))
            self.MyMirrorPage.clickNextButton()
            time.sleep(2)
            listoftopics = self.MyMirrorPage.topicsList()
            list = ['My goals and aspirations', 'Milestones at work', 'My Personal development', 'Life-work balance']
            for row in listoftopics:
                if row.text == 'My goals and aspirations':
                    row.click()
                elif row.text == 'Milestones at work':
                    row.click()
                elif row.text == 'My Personal development':
                    row.click()
                elif row.text == 'Life-work balance':
                    row.click()
            time.sleep(2)
            message = self.MyMirrorPage.getToastMessage()
            if message == "You may select up to three topics only.":
                self.log.info("You may select Topics limited to max 3 values")
            else:
                self.log.info("Topics word selection there is no limit")
            for row in listoftopics:
                if row.text == 'My goals and aspirations':
                    row.click()
            self.MyMirrorPage.clickSubmitButton()
            time.sleep(5)

    @allure.testcase("Verify that tagging a reflection is an optional step")
    @pytest.mark.order(10)
    @pytest.mark.smoke
    @allure.severity(allure.severity_level.MINOR)
    def test_VerifyThatTaggingAReflectionIsAnOptionalStep(self):
        test_name = sys._getframe().f_code.co_name
        self.log.info("###### TEST EXECUTION STARTED :: " + test_name + " ######")
        with allure.step('Navigate to login page'):
            self.homeNavigation.clickAcceptCoockiesButton()
            self.homeNavigation.clickUserProfileIcon()
            self.loginPage.login()
            time.sleep(10)
        with allure.step('Navigate to MyMirror page'):
            self.homeNavigation.clickMainToolNavDot()
            self.homeNavigation.clickMyMirror()
            self.MyMirrorPage.clickAddAReflectionLink()
            self.MyMirrorPage.addOnTextbox(data=self.data_reader.get_data(test_name, 'TextBox'))
            self.MyMirrorPage.clickNextButton()
            listofWords = self.MyMirrorPage.feelingWordsList()
            L1 = ["Relieved", "Confident", "Curious", "Hopeful", "Happy"]
            for row in listofWords:
                if row.text in L1:
                    time.sleep(1)
                    row.click()
            time.sleep(2)
            self.MyMirrorPage.clickNextButton()
            time.sleep(2)
            self.MyMirrorPage.addOnTextbox(data=self.data_reader.get_data(test_name, 'TextBox'))
            self.MyMirrorPage.clickNextButton()
            time.sleep(2)
            self.MyMirrorPage.addOnTextbox(data=self.data_reader.get_data(test_name, 'TextBox'))
            self.MyMirrorPage.clickNextButton()
            time.sleep(2)
            self.MyMirrorPage.addOnTextarea(data=self.data_reader.get_data(test_name, 'TextBox'))
            self.MyMirrorPage.clickNextButton()
            time.sleep(2)
            self.MyMirrorPage.clickSubmitButton()
            time.sleep(5)


    @allure.testcase("Verify modification of tags associated to a reflection")
    @pytest.mark.order(11)
    @pytest.mark.smoke
    @allure.severity(allure.severity_level.MINOR)
    def test_VerifyModificationOfTagsAssociatedToAReflection(self):
        test_name = sys._getframe().f_code.co_name
        self.log.info("###### TEST EXECUTION STARTED :: " + test_name + " ######")
        with allure.step('Navigate to login page'):
            self.homeNavigation.clickAcceptCoockiesButton()
            self.homeNavigation.clickUserProfileIcon()
            self.loginPage.login()
            time.sleep(10)
        with allure.step('Navigate to MyMirror page'):
            self.homeNavigation.clickMainToolNavDot()
            self.homeNavigation.clickMyMirror()
            time.sleep(2)
            self.MyMirrorPage.clickMyReflectionslink()
            time.sleep(2)
            self.MyMirrorPage.editCompletedReflection()
            self.MyMirrorPage.clickTagToTopicsLink()
            time.sleep(5)
            listoftopics = self.MyMirrorPage.topicsList()
            list = ['My goals and aspirations', 'Milestones at work', 'My Personal development', 'Life-work balance']
            for row in listoftopics:
                if row.text == 'My goals and aspirations':
                    row.click()
                elif row.text == 'Milestones at work':
                    row.click()
                elif row.text == 'My Personal development':
                    row.click()
                elif row.text == 'Life-work balance':
                    row.click()
            time.sleep(2)
            message = self.MyMirrorPage.getToastMessage()
            if message == "You may select up to three topics only.":
                self.log.info("You may select Topics limited to max 3 values")
            else:
                self.log.info("Topics word selection there is no limit")
            for row in listoftopics:
                if row.text == 'My goals and aspirations':
                    row.click()
            self.MyMirrorPage.clickSaveButton()
            time.sleep(5)

    @allure.testcase("Verify the function to add to previously completed Reflection")
    @pytest.mark.order(12)
    @pytest.mark.smoke
    @allure.severity(allure.severity_level.MINOR)
    def test_VerifyTheFunctionToAddToPreviouslyCompletedReflection(self):
        test_name = sys._getframe().f_code.co_name
        self.log.info("###### TEST EXECUTION STARTED :: " + test_name + " ######")
        with allure.step('Navigate to login page'):
            self.homeNavigation.clickAcceptCoockiesButton()
            self.homeNavigation.clickUserProfileIcon()
            self.loginPage.login()
            time.sleep(10)
        with allure.step('Navigate to MyMirror page'):
            self.homeNavigation.clickMainToolNavDot()
            self.homeNavigation.clickMyMirror()
            time.sleep(2)
            self.MyMirrorPage.clickMyReflectionslink()
            time.sleep(3)
            self.MyMirrorPage.editCompletedReflection()
            self.MyMirrorPage.clickAddAnUpdateLink()
            time.sleep(2)
            self.MyMirrorPage.enterAddanupdatetoReflection(data=self.data_reader.get_data(test_name, 'TextBox'))
            self.MyMirrorPage.clickSaveButton()
            time.sleep(3)







    # @allure.testcase("test_login_successfully")
    # @pytest.mark.smoke
    # @allure.severity(allure.severity_level.MINOR)
    # def test_login_successfully(self):
    #     test_name = sys._getframe().f_code.co_name
    #     self.log.info("###### TEST EXECUTION STARTED :: " + test_name + " ######")
    #     with allure.step('Navigate to login page'):
    #         self.homeNavigation.clickAcceptCoockiesButton()
    #         self.homeNavigation.clickUserProfileIcon()
    #         self.loginPage.login()
    #         time.sleep(10)
    #     with allure.step('Navigate to MyMirror page'):
    #         self.homeNavigation.clickMainToolNavDot()
    #         self.homeNavigation.clickMyMirror()
    #         # self.MyMirrorPage.clickAddAReflectionLink()
    #         #
    #         # self.MyMirrorPage.addOnTextbox(data="dipankar")
    #         # self.MyMirrorPage.clickNextButton()
    #         # listofWords=self.MyMirrorPage.feelingWordsList()
    #         # count=len(listofWords)
    #         # self.log.info(count)
    #         # time.sleep(10)
    #         #
    #         # for i in range(count):
    #         #     time.sleep(2)
    #         #     if listofWords[i].text == "Thrilled":
    #         #         listofWords[i].click()
    #         #         time.sleep(2)
    #         #         break
    #         #
    #         # self.MyMirrorPage.clickNextButton()
    #         # time.sleep(5)
    #         # self.MyMirrorPage.addOnTextbox(data="dipankar2")
    #         # self.MyMirrorPage.clickNextButton()
    #         # time.sleep(10)
    #         # self.MyMirrorPage.addOnTextbox(data="dipankar3")
    #         # self.MyMirrorPage.clickNextButton()
    #         # time.sleep(10)
    #         # self.MyMirrorPage.addOnTextarea(data="dipankar4")
    #         # self.MyMirrorPage.clickNextButton()
    #         # time.sleep(10)
    #         # listoftopics = self.MyMirrorPage.topicsList()
    #         # count = len(listoftopics)
    #         # self.log.info(count)
    #         # time.sleep(10)
    #         # for i in range(count):
    #         #     time.sleep(2)
    #         #     if listoftopics[i].text == "Life-work balance":
    #         #         listoftopics[i].click()
    #         #         time.sleep(2)
    #         #         break
    #         #
    #         # self.MyMirrorPage.clickSubmitButton()
    #         # time.sleep(10)
    #
    #         self.MyMirrorPage.clickMyReflectionslink()
    #         time.sleep(10)
    #         self.MyMirrorPage.clickFirstReport()
    #         time.sleep(10)
    #         self.MyMirrorPage.clickViewReflection()
    #         time.sleep(10)
