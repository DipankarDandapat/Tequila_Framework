from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.opera import OperaDriverManager
from webdriver_manager.utils import ChromeType
import logging
import FrameworkUtilities.logger_utility as log_utils
from FrameworkUtilities.config_utility import ConfigUtility


class WebDriverFactory:
    log = log_utils.custom_logger(logging.INFO)
    config = ConfigUtility()

    def __init__(self):
        self.prop = self.config.load_properties_file()
        self.browser = self.prop.get('Browser', 'browser_name')
        self.baseUrl = self.prop.get('Environment', 'environment_name')
        self.displayWidth = self.prop.get('Browser', 'browser_width')
        self.displayHeight = self.prop.get('Browser', 'browser_height')

    def getWebDriverInstance(self):
        self.log.info("browser start")

        if self.browser == "firefox":
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

        elif self.browser == "chrome":
            driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

        elif self.browser == "edge":
            driver = webdriver.Edge(executable_path=EdgeChromiumDriverManager().install())

        elif self.browser == "opera":
            driver = webdriver.Opera(executable_path=OperaDriverManager().install())

        else:
            driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())

        driver.implicitly_wait(15)
        driver.set_window_size(self.displayWidth, self.displayHeight)
        driver.get(self.baseUrl)

        return driver
