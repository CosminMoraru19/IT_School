import unittest
from time import sleep
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Elefant_Login(unittest.TestCase):

    CONNECT_BUTTON = (By.CLASS_NAME, "my-account-link hidden-xs")
    COOCKIES_CLOSE = (By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")
    def setUp(self) -> None:
        self.chrome = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        self.chrome.maximize_window()
        self.chrome.get("https://www.elefant.ro")
        try:
            cookie_accept_button = WebDriverWait(self.chrome, 5).until(EC.presence_of_element_located(*self.COOCKIES_CLOSE))
            cookie_accept_button.click()
        except:
            pass
    def tearDown(self) -> None:
        self.chrome.quit()

    def test_login_to_web_invalid_credentials(self):
        self.chrome.find_element(*self.CONNECT_BUTTON).click()



