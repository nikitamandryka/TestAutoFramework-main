"""
@package base

WebDriver Factory class implementation
It creates a webdriver instance based on browser configurations

Example:
    wdf = WebDriverFactory(browser)
    wdf.getWebDriverInstance()
"""
import traceback
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
service = ChromeService(executable_path=ChromeDriverManager().install())







class WebDriverFactory():

    def __init__(self, browser):
        """
        Inits WebDriverFactory class

        Returns:
            None
        """
        self.browser = browser
    """
        Set firefox driver and iexplorer environment based on OS

        firefoxdriver = "C:/.../firefoxdriver.exe"
        os.environ["webdriver.firefox.driver"] = firefoxdriver
        self.driver = webdriver.firefox(firefoxdriver)

        PREFERRED: Set the path on the machine where browser will be executed
    """

    def getWebDriverInstance(self):
        """
       Get WebDriver Instance based on the browser configuration

        Returns:
            'WebDriver Instance'
        """
        baseURL = "https://www.letskodeit.com/"
        if self.browser == "chrome":
            # Set ie driver
            driver = webdriver.Chrome(service=service)
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
        # elif self.browser == "chrome":
            # Set chrome driver
            # driver = webdriver.Chrome(service=service)
        else:
            driver = webdriver.Chrome(service=service)
        # Setting Driver Implicit Time out for An Element
        driver.implicitly_wait(3)
        # Maximize the window
        driver.maximize_window()
        # Loading browser with App URL
        driver.get(baseURL)
        return driver