import time

import utilities.custom_logger as cl
import logging
from base.base_page import BasePage
class LoginPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)  # added driver instance, won't run without it !!!!!
        self.driver = driver

    # locators
    _login_link = "//a[normalize-space()='Sign In']"
    _email_field = "email"
    _password_field = "login-password"
    _login_button = "login"

    # replaced with methods created in selenium_driver, so that code is cleaner!!
    # def getLoginLink(self):
    #     return self.driver.find_element(By.XPATH, self._login_link)
    #
    # def getEmailDield(self):
    #     return self.driver.find_element(By.ID, self._email_field)
    #
    # def getPassswordField(self):
    #     return self.driver.find_element(By.ID, self._password_field)
    #
    # def getLoginButton(self):
    #     return self.driver.find_element(By.ID, self._login_button)

    # action methods for page elements
    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType="xpath")

    def enterUsername(self, username):  # email
        self.sendKeys(username, self._email_field,)  # by default already used id, if xpath or something else use locatorType

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button)

    def login(self, username="", password=""):  # functionality, what needs to be done
        self.clickLoginLink()
        self.clearFields()
        self.enterUsername(username)
        self.enterPassword(password)
        time.sleep(3)
        self.clickLoginButton()

    def verifyLoginSuccess(self):
        result = self.isElementPresent("//img[@class='zl-navbar-rhs-img ']", locatorType='xpath')

        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent("//span[contains(text(),'Incorrect login details. Please try again.')]",
                                       locatorType='xpath')

        return result

    def verifyTitle(self):
        if "Login121" in self.getTitle():   # Login correct
            return True
        else:
            return False

    def clearFields(self):
        emailField = self.getElement(locator=self._email_field)
        emailField.clear()
        passwordField = self.getElement(locator=self._password_field)
        passwordField.clear()
