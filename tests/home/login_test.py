from pages.home.login_page import LoginPage
from utilities.test_status import TestStatus
import unittest
import pytest

import time


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=2)
    def test_valid_login(self):
        self.lp.login("test@email.com", "abcabc")
        result1 = self.lp.verifyTitle()
        self.ts.mark(result1, "Title Verified")
        result2 = self.lp.verifyLoginSuccess()
        self.ts.markFinal("test_validLogin", result2, "Login was successful")


    @pytest.mark.run(order=1)
    def test_invalid_login(self):
        self.lp.login("test@email.com", "abczzzzzzzabc")
        time.sleep(3)
        result = self.lp.verifyLoginFailed()
        assert result == True


