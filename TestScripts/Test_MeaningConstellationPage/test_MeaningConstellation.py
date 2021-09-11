from FrameworkUtilities.teststatus_utility import test_Status
from PageObjects.LoginPage.login_page import LoginPage
from FrameworkUtilities.data_reader_utility import DataReader
import unittest
import pytest
import sys
import allure
from PageObjects.HomeNavigation.home_navigation import HomeNavigation
from PageObjects.MeaningConstellation.meaning_constellation_page import MeaningConstellation
import FrameworkUtilities.logger_utility as log_utils
import logging
import time


@pytest.mark.usefixtures("get_driver", "initialize")
@allure.story('Test Automation Demo ')
@allure.feature('Verification Using Requests')
class MeaningConstellationTest(unittest.TestCase):
    log = log_utils.custom_logger(logging.INFO)
    data_reader = DataReader()

    @pytest.fixture(scope='function')
    def initialize(self):
        self.homeNavigation = HomeNavigation(self.driver)
        self.loginPage = LoginPage(self.driver)
        self.MeaningConstellationPage = MeaningConstellation(self.driver)
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



    @allure.testcase("Verify details of the articles displayed in Meaning Constellation")
    @pytest.mark.smoke
    @allure.severity(allure.severity_level.MINOR)  # severity of the test case
    # @pytestrail.case('C1') # test case if on TestRail
    def test_VerifyDetailsOfTheArticlesDisplayedInMeaningConstellation(self):
        test_name = sys._getframe().f_code.co_name
        self.log.info("###### TEST EXECUTION STARTED :: " + test_name + " ######")

        with allure.step('Login in to the platform with an Explorer credentials'):
            self.homeNavigation.clickAcceptCoockiesButton()
            self.homeNavigation.clickUserProfileIcon()
            self.loginPage.login()
            time.sleep(10)
        with allure.step('Click on Meaning Constellation in the main menu'):
            self.homeNavigation.clickMainToolNavDot()
            self.homeNavigation.clickMeaningConstellation()
        with allure.step('Now click on the Articles sub menu'):
            self.MeaningConstellationPage.clickArticlesLink()
            time.sleep(10)
            ele = self.MeaningConstellationPage.getListOfConstellation()
        with allure.step('Click on the Article that is Not Recommended by MeaningSphere '):
            for i in range(len(ele)):
                title = self.MeaningConstellationPage.getConstellationListTitle()
                if title[i].get_attribute('title') == "Article":
                    ele[i].click()
                    time.sleep(3)

                    ConstellationName = self.MeaningConstellationPage.getMeaningConstellationName()
                    if len(ConstellationName.text) >= 1:
                        self.log.info("Constellation Name is Present")
                    else:
                        self.log.info("Constellation Name is not Present")

                    ConstellationImage = self.MeaningConstellationPage.getMeaningConstellationImage()
                    if len(ConstellationImage.text) >= 1:
                        self.log.info("ConstellationImage is Present")
                    else:
                        self.log.info("ConstellationImage is not Present")

                    ConstellationDescription = self.MeaningConstellationPage.getMeaningConstellationDescription()
                    if len(ConstellationDescription.text) >= 1:
                        self.log.info("Constellation Description is present")
                    else:
                        self.log.info("ConstellationDescription is not present")

                    seeMoreLink = self.MeaningConstellationPage.checkSeeMoreLinkPresent()
                    if seeMoreLink == True:
                        self.MeaningConstellationPage.clickSeeMoreLink()
                        self.MeaningConstellationPage.handleMultipleWindows()
                    else:
                        self.log.info("See More Link Not Present")

                    self.MeaningConstellationPage.checkRateLinkPresent()
                    self.MeaningConstellationPage.checkCheerLinkPresent()

                    sharelink = self.MeaningConstellationPage.checkShareLinkPresent()
                    if sharelink == True:
                        self.MeaningConstellationPage.clickShareLink()
                        self.MeaningConstellationPage.checkshareAsMessageLinkPresent()
                        self.MeaningConstellationPage.checkShareAsPostLinkPresent()
                        self.MeaningConstellationPage.clickShareLink()
                    else:
                        self.log.info("Share Link Not Present")
                    self.MeaningConstellationPage.checkAddtoMyTreasuresLinkPresent()
                    self.MeaningConstellationPage.checkAddYourCommentsPresent()
                    self.MeaningConstellationPage.clickClosedDetailsPage()
                    time.sleep(3)
                    break

            else:
                self.log.info('Unable to find out Article items')
        with allure.step('Click on the Article that is Recommended by MeaningSphere '):
            for i in range(len(ele)):
                title = self.MeaningConstellationPage.getConstellationListTitle()
                if title[i].get_attribute('title') == "MS Recomended":
                    ele[i].click()
                    time.sleep(3)
                    ConstellationName = self.MeaningConstellationPage.getMeaningConstellationName()
                    if len(ConstellationName.text) >= 1:
                        print("ConstellationName is present")
                        self.log.info("ConstellationName is present")
                    else:
                        print("ConstellationName is not present")

                    ConstellationImage = self.MeaningConstellationPage.getMeaningConstellationImage()
                    if len(ConstellationImage.text) >= 1:
                        print("ConstellationImage is present")
                        self.log.info("ConstellationImage is present")
                    else:
                        print("ConstellationImage is not present")

                    ConstellationDescription = self.MeaningConstellationPage.getMeaningConstellationDescription()
                    if len(ConstellationDescription.text) >= 1:
                        print("ConstellationDescription is present")
                        self.log.info("ConstellationDescription is present")
                    else:
                        print("ConstellationDescription is not present")

                    self.MeaningConstellationPage.checkMeaningsphereRecommended_icon_Present()
                    recommendedDiscretion = self.MeaningConstellationPage.getMeaningsphereRecommendedDiscretion()
                    if len(recommendedDiscretion.text) >= 1:
                        self.log.info("Recommended Discretion Present")
                    else:
                        self.log.info("Recommended Discretion Not Present")

                    seemorelink = self.MeaningConstellationPage.checkSeeMoreLinkPresent()
                    if seemorelink == True:
                        self.MeaningConstellationPage.clickSeeMoreLink()
                        self.MeaningConstellationPage.handleMultipleWindows()
                    else:
                        self.log.info("See More Link Not Present")

                    self.MeaningConstellationPage.checkRateLinkPresent()
                    self.MeaningConstellationPage.checkCheerLinkPresent()
                    sharelink = self.MeaningConstellationPage.checkShareLinkPresent()
                    if sharelink == True:
                        self.MeaningConstellationPage.clickShareLink()
                        self.MeaningConstellationPage.checkshareAsMessageLinkPresent()
                        self.MeaningConstellationPage.checkShareAsPostLinkPresent()
                        self.MeaningConstellationPage.clickShareLink()
                    else:
                        self.log.info("Share Link Not Present")
                    self.MeaningConstellationPage.checkAddtoMyTreasuresLinkPresent()
                    self.MeaningConstellationPage.checkAddYourCommentsPresent()
                    self.MeaningConstellationPage.clickClosedDetailsPage()
                    time.sleep(3)
                    break

            else:
                self.log.info('Unable to find out MS Recomended items')


    @allure.testcase("Verify details of the books displayed in Meaning Constellation")
    @pytest.mark.smoke
    @allure.severity(allure.severity_level.MINOR)  # severity of the test case
    # @pytestrail.case('C1') # test case if on TestRail
    def test_VerifyDetailsOfTheBookDisplayedInMeaningConstellation(self):

        test_name = sys._getframe().f_code.co_name
        self.log.info("###### TEST EXECUTION STARTED :: " + test_name + " ######")

        with allure.step('Login in to the platform with an Explorer credentials'):
            self.homeNavigation.clickAcceptCoockiesButton()
            self.homeNavigation.clickUserProfileIcon()
            self.loginPage.login()
            time.sleep(10)
        with allure.step('Click on Meaning Constellation in the main menu'):
            self.homeNavigation.clickMainToolNavDot()
            self.homeNavigation.clickMeaningConstellation()
        with allure.step('Now click on the Books sub menu'):
            self.MeaningConstellationPage.clickBooksLink()
            time.sleep(10)
            ele = self.MeaningConstellationPage.getListOfConstellation()
            for i in range(len(ele)):
                title = self.MeaningConstellationPage.getConstellationListTitle()
                if title[i].get_attribute('title') == "Book":
                    ele[i].click()
                    time.sleep(3)

                    ConstellationName = self.MeaningConstellationPage.getMeaningConstellationName()
                    if len(ConstellationName.text) >= 1:
                        self.log.info("Constellation Name is present")
                    else:
                        self.log.info("Constellation Name is not present")

                    ConstellationImage = self.MeaningConstellationPage.getMeaningConstellationImage()
                    if len(ConstellationImage.text) >= 1:
                        self.log.info("Constellation Image is present")
                    else:
                        self.log.info("Constellation Image is not present")

                    ConstellationDescription = self.MeaningConstellationPage.getMeaningConstellationDescription()
                    if len(ConstellationDescription.text) >= 1:
                        self.log.info("Constellation Description is present")
                    else:
                        self.log.info("Constellation Description is not present")

                    seeMoreLink = self.MeaningConstellationPage.checkSeeMoreLinkPresent()
                    if seeMoreLink == True:
                        self.MeaningConstellationPage.clickSeeMoreLink()
                        self.MeaningConstellationPage.handleMultipleWindows()
                    else:
                        self.log.info("See More Link Not Present")

                    self.MeaningConstellationPage.checkRateLinkPresent()
                    self.MeaningConstellationPage.checkCheerLinkPresent()

                    sharelink = self.MeaningConstellationPage.checkShareLinkPresent()
                    if sharelink == True:
                        self.MeaningConstellationPage.clickShareLink()
                        self.MeaningConstellationPage.checkshareAsMessageLinkPresent()
                        self.MeaningConstellationPage.checkShareAsPostLinkPresent()
                        self.MeaningConstellationPage.clickShareLink()
                    else:
                        self.log.info("Share Link Not Present")
                    self.MeaningConstellationPage.checkAddtoMyTreasuresLinkPresent()
                    self.MeaningConstellationPage.checkAddYourCommentsPresent()
                    self.MeaningConstellationPage.clickClosedDetailsPage()
                    time.sleep(3)
                    break

            else:
                self.log.info('Unable to find out Book items')

            for i in range(len(ele)):
                title = self.MeaningConstellationPage.getConstellationListTitle()
                if title[i].get_attribute('title') == "MS Recomended":
                    ele[i].click()
                    time.sleep(3)
                    ConstellationName = self.MeaningConstellationPage.getMeaningConstellationName()
                    if len(ConstellationName.text) >= 1:
                        self.log.info("Constellation Name is present")
                    else:
                        self.log.info("Constellation Name is not present")

                    ConstellationImage = self.MeaningConstellationPage.getMeaningConstellationImage()
                    if len(ConstellationImage.text) >= 1:
                        self.log.info("Constellation Image is present")
                    else:
                        self.log.info("Constellation Image is not present")

                    ConstellationDescription = self.MeaningConstellationPage.getMeaningConstellationDescription()
                    if len(ConstellationDescription.text) >= 1:
                        self.log.info("Constellation Description is present")
                    else:
                        self.log.info("Constellation Description is not present")

                    self.MeaningConstellationPage.checkMeaningsphereRecommended_icon_Present()
                    recommendedDiscretion = self.MeaningConstellationPage.getMeaningsphereRecommendedDiscretion()
                    if len(recommendedDiscretion.text) >= 1:
                        self.log.info("Recommended Discretion Present")
                    else:
                        self.log.info("Recommended Discretion Not Present")

                    seeMoreLink = self.MeaningConstellationPage.checkSeeMoreLinkPresent()
                    if seeMoreLink == True:
                        self.MeaningConstellationPage.clickSeeMoreLink()
                        self.MeaningConstellationPage.handleMultipleWindows()
                    else:
                        self.log.info("See More Link Not Present")

                    self.MeaningConstellationPage.checkRateLinkPresent()
                    self.MeaningConstellationPage.checkCheerLinkPresent()

                    sharelink = self.MeaningConstellationPage.checkShareLinkPresent()
                    if sharelink == True:
                        self.MeaningConstellationPage.clickShareLink()
                        self.MeaningConstellationPage.checkshareAsMessageLinkPresent()
                        self.MeaningConstellationPage.checkShareAsPostLinkPresent()
                        self.MeaningConstellationPage.clickShareLink()
                    else:
                        self.log.info("Share Link Not Present")
                    self.MeaningConstellationPage.checkAddtoMyTreasuresLinkPresent()
                    self.MeaningConstellationPage.checkAddYourCommentsPresent()
                    self.MeaningConstellationPage.clickClosedDetailsPage()
                    time.sleep(3)
                    break

            else:
                self.log.info('Unable to find out MS Recomended Book items ')

    @allure.testcase("Verify details of the Movies displayed in Meaning Constellation")
    @pytest.mark.smoke
    @allure.severity(allure.severity_level.MINOR)
    # @pytestrail.case('C1')
    def test_VerifyDetailsOfTheMoviesDisplayedInMeaningConstellation(self):

        test_name = sys._getframe().f_code.co_name
        self.log.info("###### TEST EXECUTION STARTED :: " + test_name + " ######")

        with allure.step('Login in to the platform with an Explorer credentials'):
            self.homeNavigation.clickAcceptCoockiesButton()
            self.homeNavigation.clickUserProfileIcon()
            self.loginPage.login()
            time.sleep(10)
        with allure.step('Click on Meaning Constellation in the main menu'):
            self.homeNavigation.clickMainToolNavDot()
            self.homeNavigation.clickMeaningConstellation()
        with allure.step('Now click on the Movies sub menu'):
            self.MeaningConstellationPage.clickMoviesLink()
            time.sleep(10)
            ele = self.MeaningConstellationPage.getListOfConstellation()
            for i in range(len(ele)):
                title = self.MeaningConstellationPage.getConstellationListTitle()
                if title[i].get_attribute('title') == "Movie":
                    ele[i].click()
                    time.sleep(3)

                    ConstellationName = self.MeaningConstellationPage.getMeaningConstellationName()
                    if len(ConstellationName.text) >= 1:
                        print("ConstellationName is present")
                        self.log.info("ConstellationName is present")
                    else:
                        print("ConstellationName is not present")

                    ConstellationImage = self.MeaningConstellationPage.getMeaningConstellationImage()
                    if len(ConstellationImage.text) >= 1:
                        print("ConstellationImage is present")
                        self.log.info("ConstellationImage is present")
                    else:
                        print("ConstellationImage is not present")

                    ConstellationDescription = self.MeaningConstellationPage.getMeaningConstellationDescription()
                    if len(ConstellationDescription.text) >= 1:
                        print("ConstellationDescription is present")
                        self.log.info("ConstellationDescription is present")
                    else:
                        print("ConstellationDescription is not present")

                    seeMoreLink = self.MeaningConstellationPage.checkSeeMoreLinkPresent()
                    if seeMoreLink == True:
                        self.MeaningConstellationPage.clickSeeMoreLink()
                        self.MeaningConstellationPage.handleMultipleWindows()
                    else:
                        self.log.info("See More Link Not Present")

                    self.MeaningConstellationPage.checkRateLinkPresent()
                    self.MeaningConstellationPage.checkCheerLinkPresent()

                    sharelink = self.MeaningConstellationPage.checkShareLinkPresent()
                    if sharelink == True:
                        self.MeaningConstellationPage.clickShareLink()
                        self.MeaningConstellationPage.checkshareAsMessageLinkPresent()
                        self.MeaningConstellationPage.checkShareAsPostLinkPresent()
                        self.MeaningConstellationPage.clickShareLink()
                    else:
                        self.log.info("Share Link Not Present")
                    self.MeaningConstellationPage.checkAddtoMyTreasuresLinkPresent()
                    self.MeaningConstellationPage.checkAddYourCommentsPresent()
                    self.MeaningConstellationPage.clickClosedDetailsPage()
                    time.sleep(3)
                    break

            else:
                self.log.info('Unable to find out Movies items ')

            for i in range(len(ele)):
                title = self.MeaningConstellationPage.getConstellationListTitle()
                if title[i].get_attribute('title') == "MS Recomended":
                    ele[i].click()
                    time.sleep(3)
                    ConstellationName = self.MeaningConstellationPage.getMeaningConstellationName()
                    if len(ConstellationName.text) >= 1:
                        print("ConstellationName is present")
                        self.log.info("ConstellationName is present")
                    else:
                        print("ConstellationName is not present")

                    ConstellationImage = self.MeaningConstellationPage.getMeaningConstellationImage()
                    if len(ConstellationImage.text) >= 1:
                        print("ConstellationImage is present")
                        self.log.info("ConstellationImage is present")
                    else:
                        print("ConstellationImage is not present")

                    ConstellationDescription = self.MeaningConstellationPage.getMeaningConstellationDescription()
                    if len(ConstellationDescription.text) >= 1:
                        print("ConstellationDescription is present")
                        self.log.info("ConstellationDescription is present")
                    else:
                        print("ConstellationDescription is not present")

                    self.MeaningConstellationPage.checkMeaningsphereRecommended_icon_Present()
                    recommendedDiscretion = self.MeaningConstellationPage.getMeaningsphereRecommendedDiscretion()
                    if len(recommendedDiscretion.text) >= 1:
                        self.log.info("Recommended Discretion Present")
                    else:
                        self.log.info("Recommended Discretion Not Present")

                    seeMoreLink = self.MeaningConstellationPage.checkSeeMoreLinkPresent()
                    if seeMoreLink == True:
                        self.MeaningConstellationPage.clickSeeMoreLink()
                        self.MeaningConstellationPage.handleMultipleWindows()
                    else:
                        self.log.info("See More Link Not Present")

                    self.MeaningConstellationPage.checkRateLinkPresent()
                    self.MeaningConstellationPage.checkCheerLinkPresent()

                    sharelink = self.MeaningConstellationPage.checkShareLinkPresent()
                    if sharelink == True:
                        self.MeaningConstellationPage.clickShareLink()
                        self.MeaningConstellationPage.checkshareAsMessageLinkPresent()
                        self.MeaningConstellationPage.checkShareAsPostLinkPresent()
                        self.MeaningConstellationPage.clickShareLink()
                    else:
                        self.log.info("Share Link Not Present")
                    self.MeaningConstellationPage.checkAddtoMyTreasuresLinkPresent()
                    self.MeaningConstellationPage.checkAddYourCommentsPresent()
                    self.MeaningConstellationPage.clickClosedDetailsPage()
                    time.sleep(3)
                    break

            else:
                self.log.info('Unable to find out MS Recomended Movies items ')

    @allure.testcase("Verify details of the Videos displayed in Meaning Constellation")
    @pytest.mark.smoke
    @allure.severity(allure.severity_level.MINOR)  # severity of the test case
    # @pytestrail.case('C1') # test case if on TestRail
    def test_VerifyDetailsOfTheVideosDisplayedInMeaningConstellation(self):

        test_name = sys._getframe().f_code.co_name
        self.log.info("###### TEST EXECUTION STARTED :: " + test_name + " ######")

        with allure.step('Login in to the platform with an Explorer credentials'):
            self.homeNavigation.clickAcceptCoockiesButton()
            self.homeNavigation.clickUserProfileIcon()
            self.loginPage.login()
            time.sleep(10)
        with allure.step('Click on Meaning Constellation in the main menu'):
            self.homeNavigation.clickMainToolNavDot()
            self.homeNavigation.clickMeaningConstellation()
        with allure.step('Now click on the Videos sub menu'):
            self.MeaningConstellationPage.clickVideosLink()
            time.sleep(10)
            ele = self.MeaningConstellationPage.getListOfConstellation()
            for i in range(len(ele)):
                title = self.MeaningConstellationPage.getConstellationListTitle()
                if title[i].get_attribute('title') == "Video":
                    ele[i].click()
                    time.sleep(3)

                    ConstellationName = self.MeaningConstellationPage.getMeaningConstellationName()
                    if len(ConstellationName.text) >= 1:
                        self.log.info("Constellation Name is present")
                    else:
                        self.log.info("ConstellationName is not present")

                    ConstellationImage = self.MeaningConstellationPage.getMeaningConstellationImage()
                    if len(ConstellationImage.text) >= 1:
                        self.log.info("Constellation Image is present")
                    else:
                        self.log.info("Constellation Image is not present")

                    ConstellationDescription = self.MeaningConstellationPage.getMeaningConstellationDescription()
                    if len(ConstellationDescription.text) >= 1:
                        self.log.info("Constellation Description is present")
                    else:
                        self.log.info("Constellation Description is not present")

                    seeMoreLink = self.MeaningConstellationPage.checkSeeMoreLinkPresent()
                    if seeMoreLink == True:
                        self.MeaningConstellationPage.clickSeeMoreLink()
                        self.MeaningConstellationPage.handleMultipleWindows()
                    else:
                        self.log.info("See More Link Not Present")

                    self.MeaningConstellationPage.checkRateLinkPresent()
                    self.MeaningConstellationPage.checkCheerLinkPresent()

                    sharelink = self.MeaningConstellationPage.checkShareLinkPresent()
                    if sharelink == True:
                        self.MeaningConstellationPage.clickShareLink()
                        self.MeaningConstellationPage.checkshareAsMessageLinkPresent()
                        self.MeaningConstellationPage.checkShareAsPostLinkPresent()
                        self.MeaningConstellationPage.clickShareLink()
                    else:
                        self.log.info("Share Link Not Present")
                    self.MeaningConstellationPage.checkAddtoMyTreasuresLinkPresent()
                    self.MeaningConstellationPage.checkAddYourCommentsPresent()
                    self.MeaningConstellationPage.clickClosedDetailsPage()
                    time.sleep(3)
                    break

            else:
                self.log.info('Unable to find out Videos items')

            for i in range(len(ele)):
                title = self.MeaningConstellationPage.getConstellationListTitle()
                if title[i].get_attribute('title') == "MS Recomended":
                    ele[i].click()
                    time.sleep(3)
                    ConstellationName = self.MeaningConstellationPage.getMeaningConstellationName()
                    if len(ConstellationName.text) >= 1:
                        self.log.info("Constellation Name is present")
                    else:
                        self.log.info("Constellation Name is not present")

                    ConstellationImage = self.MeaningConstellationPage.getMeaningConstellationImage()
                    if len(ConstellationImage.text) >= 1:
                        self.log.info("Constellation Image is present")
                    else:
                        self.log.info("Constellation Image is not present")

                    ConstellationDescription = self.MeaningConstellationPage.getMeaningConstellationDescription()
                    if len(ConstellationDescription.text) >= 1:
                        self.log.info("Constellation Description is present")
                    else:
                        self.log.info("Constellation Description is not present")

                    self.MeaningConstellationPage.checkMeaningsphereRecommended_icon_Present()
                    recommendedDiscretion = self.MeaningConstellationPage.getMeaningsphereRecommendedDiscretion()
                    if len(recommendedDiscretion.text) >= 1:
                        self.log.info("Recommended Discretion Present")
                    else:
                        self.log.info("Recommended Discretion Not Present")

                    seeMoreLink = self.MeaningConstellationPage.checkSeeMoreLinkPresent()
                    if seeMoreLink == True:
                        self.MeaningConstellationPage.clickSeeMoreLink()
                        self.MeaningConstellationPage.handleMultipleWindows()
                    else:
                        self.log.info("See More Link Not Present")

                    self.MeaningConstellationPage.checkRateLinkPresent()
                    self.MeaningConstellationPage.checkCheerLinkPresent()

                    sharelink = self.MeaningConstellationPage.checkShareLinkPresent()
                    if sharelink == True:
                        self.MeaningConstellationPage.clickShareLink()
                        self.MeaningConstellationPage.checkshareAsMessageLinkPresent()
                        self.MeaningConstellationPage.checkShareAsPostLinkPresent()
                        self.MeaningConstellationPage.clickShareLink()
                    else:
                        self.log.info("Share Link Not Present")
                    self.MeaningConstellationPage.checkAddtoMyTreasuresLinkPresent()
                    self.MeaningConstellationPage.checkAddYourCommentsPresent()
                    self.MeaningConstellationPage.clickClosedDetailsPage()
                    time.sleep(3)
                    break

            else:
                self.log.info('Unable to find out MS Recomended Videos items ')

    @allure.testcase("Verify items displayed in the Meaning Constellation page")
    @pytest.mark.smoke
    @allure.severity(allure.severity_level.MINOR)  # severity of the test case
    # @pytestrail.case('C1') # test case if on TestRail
    def test_VerifyItemsDisplayedInTheMeaningConstellationPage(self):

        test_name = sys._getframe().f_code.co_name
        self.log.info("###### TEST EXECUTION STARTED :: " + test_name + " ######")

        with allure.step('Login in to the platform with an Explorer credentials'):
            self.homeNavigation.clickAcceptCoockiesButton()
            self.homeNavigation.clickUserProfileIcon()
            self.loginPage.login()
            time.sleep(10)
        with allure.step('Click on Meaning Constellation in the main menu'):
            self.homeNavigation.clickMainToolNavDot()
            self.homeNavigation.clickMeaningConstellation()
        with allure.step('Click on Articles sub menu'):
            self.MeaningConstellationPage.clickArticlesLink()
            time.sleep(3)
            articlesTitle = self.MeaningConstellationPage.getArticlesTitle()
            self.MeaningConstellationPage.verifyTextMatch(actualText=articlesTitle, expectedText="Articles")
            time.sleep(3)
        with allure.step('Click on Book sub menu'):
            self.MeaningConstellationPage.clickBooksLink()
            time.sleep(3)
            booksTitle = self.MeaningConstellationPage.getBooksTitle()
            self.MeaningConstellationPage.verifyTextMatch(actualText=booksTitle, expectedText="Books")
            time.sleep(3)
        with allure.step('Click on Movies sub menu'):
            self.MeaningConstellationPage.clickMoviesLink()
            time.sleep(3)
            moviesTitle = self.MeaningConstellationPage.getMoviesTitle()
            self.MeaningConstellationPage.verifyTextMatch(actualText=moviesTitle, expectedText="Movies")
            time.sleep(3)
        with allure.step('Click on Videos sub menu'):
            self.MeaningConstellationPage.clickVideosLink()
            time.sleep(3)
            videosTitle = self.MeaningConstellationPage.getVideosTitle()
            self.MeaningConstellationPage.verifyTextMatch(actualText=videosTitle, expectedText="Videos")
            time.sleep(3)

    @allure.testcase("Verify Meaning Constellation filters")
    @pytest.mark.smoke
    @allure.severity(allure.severity_level.MINOR)  # severity of the test case
    # @pytestrail.case('C1') # test case if on TestRail
    def test_VerifyMeaningConstellationFilters(self):

        test_name = sys._getframe().f_code.co_name
        self.log.info("###### TEST EXECUTION STARTED :: " + test_name + " ######")

        with allure.step('Login in to the platform with an Explorer credentials'):
            self.homeNavigation.clickAcceptCoockiesButton()
            self.homeNavigation.clickUserProfileIcon()
            self.loginPage.login()
            time.sleep(10)
        with allure.step('Click on Meaning Constellation in the main menu'):
            self.homeNavigation.clickMainToolNavDot()
            self.homeNavigation.clickMeaningConstellation()
            self.MeaningConstellationPage.clickAllLink()
            time.sleep(5)
            self.MeaningConstellationPage.clickFilterLink()
            time.sleep(5)
            self.MeaningConstellationPage.checkFilterByRatingPresent()
            self.MeaningConstellationPage.checkFilterInArticlesPresent()
            self.MeaningConstellationPage.checkFilterInBooksPresent()
            self.MeaningConstellationPage.checkFilterInMoviesPresent()
            self.MeaningConstellationPage.checkFilterInVideosPresent()
            self.MeaningConstellationPage.checkFiltermsRecomendedPresent()
            self.MeaningConstellationPage.checkFilterResetPresent()
            self.MeaningConstellationPage.checkFilterSearchButtonPresent()
        with allure.step('Click on In Books filter and click Search'):
            self.MeaningConstellationPage.clickFilterInBooks()
            self.MeaningConstellationPage.clickFilterSearchButton()
            time.sleep(10)
            self.MeaningConstellationPage.clickFilterDismiss()
            time.sleep(5)
            ele = self.MeaningConstellationPage.getListOfConstellation()
            self.log.info(len(ele))
            for i in range(len(ele)):
                title = self.MeaningConstellationPage.getConstellationListTitle()
                if title[i].get_attribute('title') == "Book":
                    self.log.info("all are book items")
                else:
                    self.log.info("all are not book items")
            else:
                self.log.info("There is no Book items ")

            time.sleep(5)
            self.MeaningConstellationPage.clickFilterLink()
            time.sleep(5)
            self.MeaningConstellationPage.clickFilterResetButton()
            time.sleep(5)
        with allure.step('Now uncheck the Books filter, click on In Articles filter option and click Search'):
            self.MeaningConstellationPage.clickFilterInArticles()
            self.MeaningConstellationPage.clickFilterSearchButton()
            time.sleep(10)
            self.MeaningConstellationPage.clickFilterDismiss()
            time.sleep(5)
            ele = self.MeaningConstellationPage.getListOfConstellation()
            self.log.info(len(ele))
            for i in range(len(ele)):
                title = self.MeaningConstellationPage.getConstellationListTitle()
                if title[i].get_attribute('title') == "Article":
                    self.log.info("all are Article items")
                else:
                    self.log.info("all are not Article items")
            else:
                self.log.info("There is no Article items ")

            time.sleep(5)
            self.MeaningConstellationPage.clickFilterLink()
            time.sleep(5)
            self.MeaningConstellationPage.clickFilterResetButton()
            time.sleep(5)
        with allure.step('Now uncheck the Articles filter, click on In Videos filter option and click Search'):
            self.MeaningConstellationPage.clickFilterInVideos()
            self.MeaningConstellationPage.clickFilterSearchButton()
            time.sleep(10)
            self.MeaningConstellationPage.clickFilterDismiss()
            time.sleep(5)
            ele = self.MeaningConstellationPage.getListOfConstellation()
            self.log.info(len(ele))
            for i in range(len(ele)):
                title = self.MeaningConstellationPage.getConstellationListTitle()
                if title[i].get_attribute('title') == "Video":
                    self.log.info("all are Video items")
                else:
                    self.log.info("all are not Video items")
            else:
                self.log.info("There is no Video items ")

            time.sleep(5)
            self.MeaningConstellationPage.clickFilterLink()
            time.sleep(5)
            self.MeaningConstellationPage.clickFilterResetButton()
            time.sleep(5)
        with allure.step('Now uncheck the Videos filter, click on In Movies filter option and click Search'):
            self.MeaningConstellationPage.clickFilterInMovies()
            self.MeaningConstellationPage.clickFilterSearchButton()
            time.sleep(10)
            self.MeaningConstellationPage.clickFilterDismiss()
            time.sleep(5)
            ele = self.MeaningConstellationPage.getListOfConstellation()
            self.log.info(len(ele))
            for i in range(len(ele)):
                title = self.MeaningConstellationPage.getConstellationListTitle()
                if title[i].get_attribute('title') == "Movie":
                    self.log.info("all are Movie items")
                else:
                    self.log.info("all are not Movie items")
            else:
                self.log.info("There is no Movie items ")
            time.sleep(10)

            time.sleep(5)
            self.MeaningConstellationPage.clickFilterLink()
            time.sleep(5)
            self.MeaningConstellationPage.clickFilterResetButton()
            time.sleep(5)
        with allure.step('Now check the MS Recommended filter option  and click Search'):
            self.MeaningConstellationPage.clickFiltermsRecomended()
            self.MeaningConstellationPage.clickFilterSearchButton()
            time.sleep(10)
            self.MeaningConstellationPage.clickFilterDismiss()
            time.sleep(5)
            ele = self.MeaningConstellationPage.getListOfConstellation()
            self.log.info(len(ele))
            for i in range(len(ele)):
                title = self.MeaningConstellationPage.getConstellationListTitle()
                if title[i].get_attribute('title') == "MS Recomended":
                    self.log.info("all are MS Recomended items")
                else:
                    self.log.info("all are not MS Recomended items")

            else:
                self.log.info("there is no MS Recomended items ")
            time.sleep(5)

    @allure.testcase("Verify option to share a Meaning Constellation item in a post")
    @pytest.mark.smoke
    @allure.severity(allure.severity_level.MINOR)  # severity of the test case
    # @pytestrail.case('C1') # test case if on TestRail
    def test_VerifyOptiontoShareaMeaningConstellationItemInaPost(self):

        test_name = sys._getframe().f_code.co_name
        self.log.info("###### TEST EXECUTION STARTED :: " + test_name + " ######")

        with allure.step('Login in to the platform with an Explorer credentials'):
            self.homeNavigation.clickAcceptCoockiesButton()
            self.homeNavigation.clickUserProfileIcon()
            self.loginPage.login()
            time.sleep(10)
        with allure.step('Click on Meaning Constellation in the main menu'):
            self.homeNavigation.clickMainToolNavDot()
            self.homeNavigation.clickMeaningConstellation()
            self.MeaningConstellationPage.clickArticlesLink()
            time.sleep(10)
            ele = self.MeaningConstellationPage.getListOfConstellation()
            for i in range(len(ele)):
                title = self.MeaningConstellationPage.getConstellationListTitle()
                if title[i].get_attribute('title') == "Article":
                    ele[i].click()
                    time.sleep(3)
                    self.MeaningConstellationPage.clickShareLink()
                    time.sleep(1)
                    self.MeaningConstellationPage.clickShareAsPostLink()
                    time.sleep(5)
                    self.MeaningConstellationPage.enterYourThoughts(data="dipankar")
                    time.sleep(1)
                    self.MeaningConstellationPage.clickShareButton()
                    time.sleep(3)
                    self.MeaningConstellationPage.clickClosedDetailsPage()
                    break

            else:
                self.log.info("There is No Article Items")



    @allure.testcase("Verify sharing of a Meaning Constellation item in a Message")
    @pytest.mark.smoke
    @allure.severity(allure.severity_level.MINOR)  # severity of the test case
    # @pytestrail.case('C1') # test case if on TestRail
    def test_VerifySharingOfaMeaningConstellationItemInaMessage(self):

        test_name = sys._getframe().f_code.co_name
        self.log.info("###### TEST EXECUTION STARTED :: " + test_name + " ######")

        with allure.step('Login as an Explorer'):
            self.homeNavigation.clickAcceptCoockiesButton()
            self.homeNavigation.clickUserProfileIcon()
            self.loginPage.login()
            time.sleep(10)
        with allure.step('Click on the Meaning Constellation option in the main menu'):
            self.homeNavigation.clickMainToolNavDot()
            self.homeNavigation.clickMeaningConstellation()
            self.MeaningConstellationPage.clickArticlesLink()
            time.sleep(10)
            ele = self.MeaningConstellationPage.getListOfConstellation()
            for i in range(len(ele)):
                title = self.MeaningConstellationPage.getConstellationListTitle()
                if title[i].get_attribute('title') == "Article":
                    ele[i].click()
                    time.sleep(3)
                    self.MeaningConstellationPage.clickShareLink()
                    time.sleep(3)
                    self.MeaningConstellationPage.clickShareAsMessageLink()
                    time.sleep(2)
                    self.MeaningConstellationPage.clickSendMessageArrow()
                    time.sleep(2)
                    userList = self.MeaningConstellationPage.getAllSendMessageUserList()
                    for x in range(len(userList)):
                        if userList[x].text == "Rob Lake":
                            userList[x].click()
                            break
                        else:
                            self.log.info("user not present")

                    time.sleep(2)
                    self.MeaningConstellationPage.enterMessage(data="dipankar")
                    time.sleep(2)
                    self.MeaningConstellationPage.clickMessageSendButton()
                    time.sleep(3)
                    self.MeaningConstellationPage.clickClosedDetailsPage()
                    break

            else:
                self.log.info("There is No Article Items ")

    @allure.testcase("Verify adding a Meaning Constellation item to My Treasures")
    @pytest.mark.smoke
    @allure.severity(allure.severity_level.MINOR)  # severity of the test case
    # @pytestrail.case('C1') # test case if on TestRail
    def test_VerifyAddingAMeaningConstellationItemToMyTreasures(self):

        test_name = sys._getframe().f_code.co_name
        self.log.info("###### TEST EXECUTION STARTED :: " + test_name + " ######")

        with allure.step('Login as an Explorer'):
            self.homeNavigation.clickAcceptCoockiesButton()
            self.homeNavigation.clickUserProfileIcon()
            self.loginPage.login()
            time.sleep(10)
        with allure.step('Click on the Meaning Constellation option in the main menu'):
            self.homeNavigation.clickMainToolNavDot()
            self.homeNavigation.clickMeaningConstellation()
            self.MeaningConstellationPage.clickArticlesLink()
            time.sleep(10)
            ele = self.MeaningConstellationPage.getListOfConstellation()
            for i in range(len(ele)):
                title = self.MeaningConstellationPage.getConstellationListTitle()
                if title[i].get_attribute('title') == "Article":
                    ele[i].click()
                    time.sleep(3)
                    self.MeaningConstellationPage.clickAddtoMyTreasuresLink()
                    time.sleep(1)
                    message = self.MeaningConstellationPage.getToastMessage()
                    self.log.info(message)
                    if message == "You have already added to your Treasures!":
                        self.log.info("item already added on your Treasures ")
                    elif message == "Added to your Treasures successfully!":
                        self.log.info("item is added in Treasures ")
                    else:
                        self.log.info("Toast message not coming")
                    time.sleep(10)
                    self.MeaningConstellationPage.clickClosedDetailsPage()
                    break

            else:self.log.info("There is No Article Items")

    @allure.testcase("Verify commenting on a Meaning Constellation item")
    @pytest.mark.smoke
    @allure.severity(allure.severity_level.MINOR)  # severity of the test case
    # @pytestrail.case('C1') # test case if on TestRail
    def test_VerifyCommentingOnAMeaningConstellationItem(self):

        test_name = sys._getframe().f_code.co_name
        self.log.info("###### TEST EXECUTION STARTED :: " + test_name + " ######")

        with allure.step('Login as an Explorer'):
            self.homeNavigation.clickAcceptCoockiesButton()
            self.homeNavigation.clickUserProfileIcon()
            self.loginPage.login()
            time.sleep(10)
        with allure.step('Click on the Meaning Constellation option in the main menu'):
            self.homeNavigation.clickMainToolNavDot()
            self.homeNavigation.clickMeaningConstellation()
            self.MeaningConstellationPage.clickArticlesLink()
            time.sleep(10)
            ele = self.MeaningConstellationPage.getListOfConstellation()
            for i in range(len(ele)):
                title = self.MeaningConstellationPage.getConstellationListTitle()
                if title[i].get_attribute('title') == "Article":
                    ele[i].click()
                    time.sleep(3)
                    comment = self.MeaningConstellationPage.getCommentStatus()
                    commentlist = comment.split()
                    commentCounts = int(commentlist[0])
                    self.log.info(commentCounts)
                    self.MeaningConstellationPage.enterAddYourComments(data="dipankar")
                    time.sleep(2)
                    self.MeaningConstellationPage.cickAddYourCommentsSubmitButton()
                    time.sleep(4)
                    newcomment = self.MeaningConstellationPage.getCommentStatus()
                    newcommentlist = newcomment.split()
                    newcommentCounts = int(newcommentlist[0])
                    self.log.info(newcommentCounts)
                    if commentCounts + 1 == newcommentCounts:
                        self.log.info("comment working fine")
                    else:
                        self.log.info("comment not working")

                    time.sleep(5)
                    self.MeaningConstellationPage.clickClosedDetailsPage()
                    break
            else:
                self.log.info("There is No Article Items")

    @allure.testcase("Verify suggesting a new Meaning Constellation item")
    @pytest.mark.smoke
    @allure.severity(allure.severity_level.MINOR)  # severity of the test case
    # @pytestrail.case('C1') # test case if on TestRail
    def test_VerifySuggestingANewMeaningConstellationitem(self):

        test_name = sys._getframe().f_code.co_name
        self.log.info("###### TEST EXECUTION STARTED :: " + test_name + " ######")

        with allure.step('Login as an Explorer'):
            self.homeNavigation.clickAcceptCoockiesButton()
            self.homeNavigation.clickUserProfileIcon()
            self.loginPage.login()
            time.sleep(10)
        with allure.step('Click on the Meaning Constellation option in the main menu'):
            self.homeNavigation.clickMainToolNavDot()
            self.homeNavigation.clickMeaningConstellation()
            time.sleep(3)
            self.MeaningConstellationPage.clickNewRequestLink()
            time.sleep(3)
            self.MeaningConstellationPage.checkNewRequestSuggestedByPresent()
            self.MeaningConstellationPage.checkNewRequestCreatedOnPresent()
            self.MeaningConstellationPage.checkNewRequestCategoryPresent()
            self.MeaningConstellationPage.checkNewRequestTitlePresent()
            self.MeaningConstellationPage.checkNewRequestDescriptionPresent()
            self.MeaningConstellationPage.checkNewRequestLinkPresent()
            self.MeaningConstellationPage.checkNewRequestImageUploadPresent()
            self.MeaningConstellationPage.checkNewRequestVideoUploadPresent()
            self.MeaningConstellationPage.enterNewRequestTitle(data="dipankar")
            self.MeaningConstellationPage.enterNewRequestDescription(data="dipankar")
            self.MeaningConstellationPage.enterNewRequestLink(data="www.google.com")
            self.MeaningConstellationPage.clickNewRequestSaveButton()
            time.sleep(4)
            message = self.MeaningConstellationPage.getToastMessage()
            self.log.info(message)
            time.sleep(10)


    @allure.testcase("Verify cheering a Meaning Constellation item")
    @pytest.mark.smoke
    @allure.severity(allure.severity_level.MINOR)  # severity of the test case
    # @pytestrail.case('C1') # test case if on TestRail
    def test_VerifyCheeringAMeaningConstellationItem(self):

        test_name = sys._getframe().f_code.co_name
        self.log.info("###### TEST EXECUTION STARTED :: " + test_name + " ######")

        with allure.step('Login as an Explorer'):
            self.homeNavigation.clickAcceptCoockiesButton()
            self.homeNavigation.clickUserProfileIcon()
            self.loginPage.login()
            time.sleep(10)
        with allure.step('Click on the Meaning Constellation option in the main menu'):
            self.homeNavigation.clickMainToolNavDot()
            self.homeNavigation.clickMeaningConstellation()
            self.MeaningConstellationPage.clickArticlesLink()
            time.sleep(10)
            ele = self.MeaningConstellationPage.getListOfConstellation()
            for i in range(len(ele)):
                title = self.MeaningConstellationPage.getConstellationListTitle()
                if title[i].get_attribute('title') == "Article":
                    ele[i].click()
                    time.sleep(3)
                    self.MeaningConstellationPage.checkCheerLinkPresent()
                    cheercount=self.MeaningConstellationPage.getCheerLinkCheerTitleCounts()
                    self.MeaningConstellationPage.clickCheerLink()
                    time.sleep(2)
                    self.MeaningConstellationPage.clickCheerLinkCheerTitle()
                    time.sleep(3)
                    message = self.MeaningConstellationPage.getToastMessage()
                    self.MeaningConstellationPage.clickCheerLink()
                    newCheercount = self.MeaningConstellationPage.getCheerLinkCheerTitleCounts()
                    if message=="Tagged as 'Cheer' successfully!":
                        if int(cheercount)+1==int(newCheercount):
                            self.log.info("cheer tagged working properly")
                    elif message=="Untagged as 'Cheer' successfully!":
                        if int(cheercount)-1==int(newCheercount):
                            self.log.info("cheer tagged working properly.........")
                    else:self.log.info("cheer tagged Not working ")
                    time.sleep(10)

                    resonateCount = self.MeaningConstellationPage.getCheerLinkIResonateTitleCounts()
                    self.MeaningConstellationPage.clickCheerLink()
                    time.sleep(2)
                    self.MeaningConstellationPage.clickCheerLinkIResonateTitle()
                    time.sleep(3)
                    message = self.MeaningConstellationPage.getToastMessage()
                    self.MeaningConstellationPage.clickCheerLink()
                    newResonatecount = self.MeaningConstellationPage.getCheerLinkIResonateTitleCounts()
                    if message=="Tagged as 'I Resonate' successfully!":
                        if int(resonateCount)+1==int(newResonatecount):
                            self.log.info("Resonate tagged working properly")
                    elif message=="Untagged as 'I Resonate' successfully!":
                        if int(resonateCount)-1==int(newResonatecount):
                            self.log.info("Resonate tagged working properly............")
                    else:self.log.info("Resonate tagged Not working ")
                    time.sleep(10)

                    learnedCount = self.MeaningConstellationPage.getCheerLinkILearnedTitleCounts()
                    self.MeaningConstellationPage.clickCheerLink()
                    time.sleep(2)
                    self.MeaningConstellationPage.clickCheerLinkILearnedTitle()
                    time.sleep(3)
                    message = self.MeaningConstellationPage.getToastMessage()
                    self.MeaningConstellationPage.clickCheerLink()
                    newLearnedcount = self.MeaningConstellationPage.getCheerLinkILearnedTitleCounts()
                    if message == "Tagged as 'I Learned' successfully!":
                        if int(learnedCount) + 1 == int(newLearnedcount):
                            self.log.info("Learned tagged working properly")
                    elif message == "Untagged as 'I Learned' successfully!":
                        if int(learnedCount) - 1 == int(newLearnedcount):
                            self.log.info("Learned tagged working properly........")
                    else:
                        self.log.info("Learned tagged Not working ")

                    time.sleep(10)

                    inspiredCount = self.MeaningConstellationPage.getCheerLinkIamInspiredTitleCounts()
                    self.MeaningConstellationPage.clickCheerLink()
                    time.sleep(2)
                    self.MeaningConstellationPage.clickCheerLinkIamInspiredTitle()
                    time.sleep(3)
                    message = self.MeaningConstellationPage.getToastMessage()
                    self.MeaningConstellationPage.clickCheerLink()
                    newInspiredcount = self.MeaningConstellationPage.getCheerLinkIamInspiredTitleCounts()
                    if message == "Tagged as 'I am Inspired' successfully!":
                        if int(inspiredCount) + 1 == int(newInspiredcount):
                            self.log.info("Inspired tagged working properly")
                    elif message == "Untagged as 'I am Inspired' successfully!":
                        if int(inspiredCount) - 1 == int(newInspiredcount):
                            self.log.info("Inspired tagged working properly...........")
                    else:
                        self.log.info("Inspired tagged Not working ")

                    time.sleep(5)
                    self.MeaningConstellationPage.clickClosedDetailsPage()
                    break

            else:
                self.log.info("There is No Article Items")