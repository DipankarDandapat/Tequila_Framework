import FrameworkUtilities.logger_utility as log_utils
import logging
from HelperLibraries.basepage import BasePage


class MeaningConstellation(BasePage):
    log = log_utils.custom_logger(logging.INFO)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.MeaningConstellation_locators = self.pageLocators('MeaningConstellation')

    def clickOverviewLink(self):
        self.elementClick(*self.locator(self.MeaningConstellation_locators, 'overview_link'))

    def clickAllLink(self):
        self.elementClick(*self.locator(self.MeaningConstellation_locators, 'all_link'))

    def clickArticlesLink(self):
        self.elementClick(*self.locator(self.MeaningConstellation_locators, 'articles_link'))

    def getArticlesTitle(self):
        element = self.getText(*self.locator(self.MeaningConstellation_locators, 'articles_title'))
        return element

    def clickBooksLink(self):
        self.elementClick(*self.locator(self.MeaningConstellation_locators, 'books_link'))

    def getBooksTitle(self):
        element = self.getText(*self.locator(self.MeaningConstellation_locators, 'books_title'))
        return element

    def clickMoviesLink(self):
        self.elementClick(*self.locator(self.MeaningConstellation_locators, 'movies_link'))

    def getMoviesTitle(self):
        element = self.getText(*self.locator(self.MeaningConstellation_locators, 'movies_title'))
        return element

    def clickVideosLink(self):
        self.elementClick(*self.locator(self.MeaningConstellation_locators, 'videos_link'))

    def getVideosTitle(self):
        element = self.getText(*self.locator(self.MeaningConstellation_locators, 'videos_title'))
        return element

    def clickNewRequestLink(self):
        self.elementClick(*self.locator(self.MeaningConstellation_locators, 'new_request_link'))

    def getListOfConstellation(self):
        element = self.getElementList(*self.locator(self.MeaningConstellation_locators, 'list_of_constellation'))
        return element

    def getConstellationListTitle(self):
        element = self.getElementList(*self.locator(self.MeaningConstellation_locators, 'constellation_list_title'))
        return element

    def clickClosedDetailsPage(self):
        self.elementClick(*self.locator(self.MeaningConstellation_locators, 'closed_details_page'))

    def checkRateLinkPresent(self):
        element = self.isElementPresent(*self.locator(self.MeaningConstellation_locators, 'rate_link'))
        return element

    def checkCheerLinkPresent(self):
        element = self.isElementPresent(*self.locator(self.MeaningConstellation_locators, 'cheer_link'))
        return element

    def clickCheerLink(self):
        self.elementClick(*self.locator(self.MeaningConstellation_locators, 'cheer_link'))
    def clickCheerLinkCheerTitle(self):
        self.elementClick(*self.locator(self.MeaningConstellation_locators, 'cheer_link_cheer_title'))
    def getCheerLinkCheerTitleCounts(self):
        element=self.getText(*self.locator(self.MeaningConstellation_locators, 'cheer_link_cheer_title_counts'))
        return element

    def clickCheerLinkIResonateTitle(self):
        self.elementClick(*self.locator(self.MeaningConstellation_locators, 'cheer_link_IResonate_title'))
    def getCheerLinkIResonateTitleCounts(self):
        element=self.getText(*self.locator(self.MeaningConstellation_locators, 'cheer_link_IResonate_title_counts'))
        return element

    def clickCheerLinkILearnedTitle(self):
        self.elementClick(*self.locator(self.MeaningConstellation_locators, 'cheer_link_ILearned_title'))
    def getCheerLinkILearnedTitleCounts(self):
        element=self.getText(*self.locator(self.MeaningConstellation_locators, 'cheer_link_ILearned_title_counts'))
        return element

    def clickCheerLinkIamInspiredTitle(self):
        self.elementClick(*self.locator(self.MeaningConstellation_locators, 'cheer_link_IamInspired_title'))
    def getCheerLinkIamInspiredTitleCounts(self):
        element=self.getText(*self.locator(self.MeaningConstellation_locators, 'cheer_link_IamInspired_title_counts'))
        return element



    def checkShareLinkPresent(self):
        element = self.isElementPresent(*self.locator(self.MeaningConstellation_locators, 'share_link'))
        return element

    def checkAddtoMyTreasuresLinkPresent(self):
        element = self.isElementPresent(*self.locator(self.MeaningConstellation_locators, 'add_to_my_treasures_link'))
        return element

    def clickAddtoMyTreasuresLink(self):
        self.elementClick(*self.locator(self.MeaningConstellation_locators, 'add_to_my_treasures_link'))

    def checkSeeMoreLinkPresent(self):
        element = self.isElementPresent(*self.locator(self.MeaningConstellation_locators, 'meaning_constellation_seemore'))
        return element

    def clickSeeMoreLink(self):
        self.elementClick(*self.locator(self.MeaningConstellation_locators, 'meaning_constellation_seemore'))

    def checkAddYourCommentsPresent(self):
        element = self.isElementPresent(*self.locator(self.MeaningConstellation_locators, 'meaning_constellation_add_your_comments'))
        return element

    def enterAddYourComments(self, data=''):
        self.sendKeys(data,*self.locator(self.MeaningConstellation_locators, 'meaning_constellation_add_your_comments'))

    def getCommentStatus(self):
        element = self.getText(*self.locator(self.MeaningConstellation_locators, 'comments_status'))
        return element

    def cickAddYourCommentsSubmitButton(self):
        self.elementClick(*self.locator(self.MeaningConstellation_locators, 'meaning_constellation_add_your_comments_submit_button'))

    def checkMeaningsphereRecommended_icon_Present(self):
        element = self.isElementPresent(*self.locator(self.MeaningConstellation_locators, 'meaningsphere_recommended_icon'))
        return element

    def getMeaningsphereRecommendedDiscretion(self):
        element = self.getElement(*self.locator(self.MeaningConstellation_locators, 'meaningsphere_recommended_discretion'))
        return element

    def checkshareAsMessageLinkPresent(self):
        element = self.isElementPresent(*self.locator(self.MeaningConstellation_locators, 'share_as_message_link'))
        return element

    def clickShareAsMessageLink(self):
        self.elementClick(*self.locator(self.MeaningConstellation_locators, 'share_as_message_link'))

    def clickSendMessageArrow(self):
        self.elementClick(*self.locator(self.MeaningConstellation_locators, 'send_message_arrow'))

    def getAllSendMessageUserList(self):
        element = self.getElementList(*self.locator(self.MeaningConstellation_locators, 'send_message_user_list'))
        return element

    def enterMessage(self, data=''):
        self.sendKeys(data, *self.locator(self.MeaningConstellation_locators, 'message'))

    def clickMessageSendButton(self):
        self.elementClick(*self.locator(self.MeaningConstellation_locators, 'message_send_button'))

    def checkShareAsPostLinkPresent(self):
        element = self.isElementPresent(*self.locator(self.MeaningConstellation_locators, 'share_as_post_link'))
        return element

    def clickShareAsPostLink(self):
        self.elementClick(*self.locator(self.MeaningConstellation_locators, 'share_as_post_link'))

    def enterYourThoughts(self, data=''):
        self.sendKeys(data, *self.locator(self.MeaningConstellation_locators, 'thoughts'))

    def clickShareButton(self):
        self.elementClick(*self.locator(self.MeaningConstellation_locators, 'shareButton'))

    def clickShareLink(self):
        self.elementClick(*self.locator(self.MeaningConstellation_locators, 'share_link'))

    def getMeaningConstellationName(self):
        element = self.getElement(*self.locator(self.MeaningConstellation_locators, 'meaning_constellation_name'))
        return element

    def getMeaningConstellationImage(self):
        element = self.getElement(*self.locator(self.MeaningConstellation_locators, 'meaning_constellation_image'))
        return element

    def getMeaningConstellationDescription(self):
        element = self.getElement(
            *self.locator(self.MeaningConstellation_locators, 'meaning_constellation_description'))
        return element

    def checkFilterByRatingPresent(self):
        element = self.isElementPresent(*self.locator(self.MeaningConstellation_locators, 'filter_byRating'))
        return element

    def checkFilterInBooksPresent(self):
        element = self.isElementPresent(*self.locator(self.MeaningConstellation_locators, 'filter_inBooks'))
        return element

    def checkFilterInArticlesPresent(self):
        element = self.isElementPresent(*self.locator(self.MeaningConstellation_locators, 'filter_inArticles'))
        return element

    def checkFilterInVideosPresent(self):
        element = self.isElementPresent(*self.locator(self.MeaningConstellation_locators, 'filter_inVideos'))
        return element

    def checkFilterInMoviesPresent(self):
        element = self.isElementPresent(*self.locator(self.MeaningConstellation_locators, 'filter_inMovies'))
        return element

    def checkFiltermsRecomendedPresent(self):
        element = self.isElementPresent(*self.locator(self.MeaningConstellation_locators, 'filter_msRecomended'))
        return element

    def checkFilterResetPresent(self):
        element = self.isElementPresent(*self.locator(self.MeaningConstellation_locators, 'filter_reset'))
        return element

    def checkFilterSearchButtonPresent(self):
        element = self.isElementPresent(*self.locator(self.MeaningConstellation_locators, 'filter_search_button'))
        return element

    def clickFilterLink(self):
        self.elementClick(*self.locator(self.MeaningConstellation_locators, 'filter'))

    def clickFilterInBooks(self):
        self.elementClick(*self.locator(self.MeaningConstellation_locators, 'filter_inBooks'))

    def clickFilterInArticles(self):
        self.elementClick(*self.locator(self.MeaningConstellation_locators, 'filter_inArticles'))

    def clickFilterInVideos(self):
        self.elementClick(*self.locator(self.MeaningConstellation_locators, 'filter_inVideos'))

    def clickFilterInMovies(self):
        self.elementClick(*self.locator(self.MeaningConstellation_locators, 'filter_inMovies'))

    def clickFiltermsRecomended(self):
        self.elementClick(*self.locator(self.MeaningConstellation_locators, 'filter_msRecomended'))

    def clickFilterResetButton(self):
        self.elementClick(*self.locator(self.MeaningConstellation_locators, 'filter_reset'))

    def clickFilterSearchButton(self):
        self.elementClick(*self.locator(self.MeaningConstellation_locators, 'filter_search_button'))

    def clickFilterDismiss(self):
        self.elementClick(*self.locator(self.MeaningConstellation_locators, 'filter_dismiss'))

    def getToastMessage(self):
        element = self.getText(*self.locator(self.MeaningConstellation_locators, 'toast_message'))
        return element

    def checkNewRequestSuggestedByPresent(self):
        element = self.isElementPresent(*self.locator(self.MeaningConstellation_locators, 'newRequest_suggested_by'))
        return element

    def checkNewRequestCreatedOnPresent(self):
        element = self.isElementPresent(*self.locator(self.MeaningConstellation_locators, 'newRequest_created_on'))
        return element
    def checkNewRequestCategoryPresent(self):
        element = self.isElementPresent(*self.locator(self.MeaningConstellation_locators, 'newRequest_category'))
        return element
    def checkNewRequestTitlePresent(self):
        element = self.isElementPresent(*self.locator(self.MeaningConstellation_locators, 'newRequest_title'))
        return element

    def enterNewRequestTitle(self, data=''):
        self.sendKeys(data, *self.locator(self.MeaningConstellation_locators, 'newRequest_title'))

    def checkNewRequestDescriptionPresent(self):
        element = self.isElementPresent(*self.locator(self.MeaningConstellation_locators, 'newRequest_description'))
        return element

    def enterNewRequestDescription(self, data=''):
        self.sendKeys(data, *self.locator(self.MeaningConstellation_locators, 'newRequest_description'))

    def checkNewRequestLinkPresent(self):
        element = self.isElementPresent(*self.locator(self.MeaningConstellation_locators, 'newRequest_link_url'))
        return element
    def checkNewRequestImageUploadPresent(self):
        element = self.isElementPresent(*self.locator(self.MeaningConstellation_locators, 'newRequest_image_upload'))
        return element
    def checkNewRequestVideoUploadPresent(self):
        element = self.isElementPresent(*self.locator(self.MeaningConstellation_locators, 'newRequest_video_upload'))
        return element

    def enterNewRequestLink(self, data=''):
        self.sendKeys(data, *self.locator(self.MeaningConstellation_locators, 'newRequest_link_url'))
    def clickNewRequestSaveButton(self):
        self.elementClick(*self.locator(self.MeaningConstellation_locators, 'newRequest_save_button'))
    def clickNewRequestCancelButton(self):
        self.elementClick(*self.locator(self.MeaningConstellation_locators, 'newRequest_cancel_button'))