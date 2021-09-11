from HelperLibraries.selenium_driver import SeleniumDriver
import FrameworkUtilities.logger_utility as log_utils
import logging
import allure
from traceback import print_stack
import pytest


class test_Status(SeleniumDriver):

    log = log_utils.custom_logger(logging.INFO)

    def __init__(self, driver):
        """
        Inits CheckPoint class

        """
        super(test_Status, self).__init__(driver)
        self.driver = driver
        self.result_list = []

    def set_result(self, result, test_name):

        """
        This method is used for setting the execution result.
        :param result: this parameter takes the execution status value pass/fail.
        :param test_name: this parameter takes the execution status description.
        :return: this method returns nothing.
        """

        try:
            if result is not None:
                if result:
                    self.result_list.append("PASS")
                    self.log.info("### VERIFICATION SUCCESSFUL :: " + test_name)
                else:
                    self.result_list.append("FAIL")
                    self.log.error("### VERIFICATION FAILED :: " + test_name)
                    # allure.attach.file(self.take_screenshots(test_name), attachment_type=allure.attachment_type.PNG)

            else:
                self.result_list.append("FAIL")
                self.log.error("### VERIFICATION FAILED :: " + test_name)
                allure.attach.file(self.take_screenshots(test_name), attachment_type=allure.attachment_type.PNG)
        except Exception as ex:
            self.result_list.append("FAIL")
            self.log.error("### EXCEPTION OCCURRED :: ", ex)
            allure.attach.file(self.take_screenshots(test_name), attachment_type=allure.attachment_type.PNG)
            print_stack()

    def mark(self, test_step, result):

        """
        This method handles intermediate assertions and saves the result for final mark.
        :param result: this parameter takes the execution status value pass/fail.
        :param test_step: it takes the test case name value
        :return: this method returns nothing.
        """

        self.set_result(result=result, test_name=test_step)

    def mark_final(self, result, test_step):

        """
        This method handles final assertion and saves the result for final mark.
        :param test_step: it takes the test case name value
        :param result: this parameter takes the execution status value pass/fail.
        :return: this method returns nothing.
        """

        # self.set_result(result, test_step)
        #
        # if "FAIL" in self.result_list:
        #     self.log.error("### " + test_step + " ### TEST FAILED")
        #     self.result_list.clear()
        #     assert True is False, "### " + test_step + " ### TEST FAILED"
        #
        # else:
        #     self.log.info("### " + test_step + "### TEST SUCCESSFUL")
        #     self.result_list.clear()
        #     assert True is True, "### " + test_step + "### TEST SUCCESSFUL"

        self.set_result(result, test_step)

        # noinspection PyBroadException
        try:
            if "FAIL" in self.result_list:
                self.result_list.clear()
                assert True is False

            else:
                self.result_list.clear()
                assert True is True, "### TEST SUCCESSFUL :: " + test_step

        except Exception:
            pytest.fail("### TEST FAILED :: " + test_step, pytrace=False)