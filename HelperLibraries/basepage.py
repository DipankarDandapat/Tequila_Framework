from HelperLibraries.selenium_driver import SeleniumDriver
from selenium.webdriver.common.action_chains import ActionChains

class BasePage(SeleniumDriver):

    def __init__(self, driver):
        super(BasePage, self).__init__(driver)
        self.driver = driver


    def handleMultipleWindows(self):
        handles = self.driver.window_handles
        size = len(handles)
        parent_handle = self.driver.current_window_handle
        for x in range(size):
          if handles[x] != parent_handle:
            self.driver.switch_to.window(handles[x])
            self.driver.close()
            break
        self.driver.switch_to.window(parent_handle)

    def ScrollToElements(self,elements):
        actions = ActionChains(self.driver)
        actions.move_to_element(elements)
        actions.perform()


