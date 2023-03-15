import unittest
from time import sleep
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from selenium.webdriver.common.by import By

class Browser(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get('https://formy-project.herokuapp.com/form')

        # self.driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))

    def test_firefox(self):

        first_name = self.driver.find_element(By.ID, 'first-name')
        first_name.send_keys('NUME DE TEST')

    def tearDown(self) -> None:
        sleep(1)
        self.driver.quit()

'''
pt alte browsere
https://pypi.org/project/webdriver-manager/#use-with-firefox
'''