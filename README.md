# Automation Testing Framework Using Python

Description
=============
This Automation Testing Framework Using selenium and Python With The Below Features:

* Framework is based on page object model.
* Reporting using Allure report.
* Reading locators from JSON file.
* Reading test data from Excel / JSON file.
* Integrated with TestRail to update test cases status after each run.
* Framework can integrate with CodeShip.


Module Installation
=====================
Use the package manager [pip](https://pypi.org/) Install the depended packages

```bash
pip install pytest
```
```bash
pip install selenium
```
```bash
pip install webdriver-manager
```
```bash
pip install ipython
```
```bash
pip install openpyxl
```
```bash
pip install allure-pytest
```
```bash
pip install allure-python-commons
```
```bash
pip install pytest-order
```
```bash
pip install pytest-testrail
```


Create new test case
=====================

In order to create a new test case using the **Framework**, you have to follow the below steps:

* In **Locators Module**, create a new locator for the element you would like to use, as below:


        [{
          "pageName": "HomePage",
          "name": "input_email",
          "locateUsing": "xpath",
          "locator": "//input[@formcontrolname='username']"
          },
          {
            "pageName": "HomePage",
            "name": "input_password",
            "locateUsing": "xpath",
            "locator": "//input[@formcontrolname='password']"
          },
          {
            "pageName": "HomePage",
            "name": "btn_login",
            "locateUsing": "xpath",
            "locator": "//button[contains(text(),'LOGIN')]"
          }
        ]



* If the element exists in only one page, go to **PageObject Module** and create a new script for that page e.g: ``login_page.py`` and add all the actions in that page, as below:

        class LoginPage(BasePage):
              def __init__(self, driver):
                  super().__init__(driver)
                  self.driver = driver
                  self.loginPage_locators = self.pageLocators('HomePage')
          
              def login(self, email, password):
                  self.sendKeys(email, *self.locator(self.loginPage_locators, 'input_email'))
                  self.sendKeys(password, *self.locator(self.loginPage_locators, 'input_password'))
                  self.elementClick(*self.locator(self.loginPage_locators, 'btn_login'))

* Then, in **TestScripts Module**, create a new script for your test case(s) e.g: ``test_login.py`` and add your test case, as below:

        @allure.story('epic_1') # story of the test case
        @allure.severity(allure.severity_level.MINOR) # severity of the test case
        @pytestrail.case('C48') # test case id on test rail
        def test_login_successfully(self):
        
            with allure.step('Navigate to login page'):
                self.homeNavigation.goToLoginPage()
                self.ts.markFinal(self.loginPage.isAt, "navigation to login page failed") # check if the navigation to login page occurs successfully

            with allure.step('Login'): # name of the test step
                self.loginPage.login(email=td.testData("email"), password=td.testData("password"))
                self.ts.markFinal(self.dashboardPage.isAt, "login failed") # check if login successfully


**Notes:**
   * use ``@allure.story('[epic name]')`` decorator before each test case to define the related epic / story.
   * use ``@allure.severity(allure.severity_level.[severity])`` decorator before each test case to define the severity of the test case Minor/Major/Critical/Blocker.
   * use ``@pytestrail.case('[test case id on testrail]')`` decorator before each test case to defione the related test case id on test rail to make the script update run status on test rail.


Run the test case
==================

In order to run the test case after creation, use on of the below commands:

* To run the test case and create allure report but without update the status run on TestRail:

``py.test --alluredir=allure_report tests/test_login.py``

``allure serve allure_report``


* To run the test case, create allure report and update the status of run on TestRail:

``py.test --alluredir=allure_report tests/test_login.py --testrail``

``allure serve allure_report``

**Note:**
   * There are other options of run that you can search for them, as running all the test cases for specific epic/story or with specific severity


Integration with TestRail
=========================

In order to setup the integration with TestRail, edit ``testrail.cfg`` with your testrail domain and credentials, as below:

        [API]
        url = https://[your testrail domain].testrail.io
        email = [testrail email]
        password = [testrail password]

        [TESTRUN]
        project_id = [project id]
