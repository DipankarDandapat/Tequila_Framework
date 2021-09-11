import FrameworkUtilities.logger_utility as log_utils
import logging
from HelperLibraries.basepage import BasePage


class LoginPage(BasePage):
    log = log_utils.custom_logger(logging.INFO)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.loginPage_locators = self.pageLocators('HomePage')

    def login(self, email='admin@meaningsphere.com', password='Ab1234567@'):
        self.sendKeys(email, *self.locator(self.loginPage_locators, 'input_email'))
        self.sendKeys(password, *self.locator(self.loginPage_locators, 'input_password'))
        self.elementClick(*self.locator(self.loginPage_locators, 'btn_login'))

    def is_emailbox_presece(self):
        return self.elementPresenceCheck(*self.locator(self.loginPage_locators, 'btn_login'))

    def is_passwordbox_presece(self):
        return self.elementPresenceCheck(*self.locator(self.loginPage_locators, 'input_password'))
