import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep


class ContextMenu(unittest.TestCase):
    CONTEXT = (By.XPATH, '//a[text()="Context Menu"]')
    BOX = (By.ID, 'hot-spot')
    FIRST_NAME_INPUT = (By.XPATH, '//input[@id="first-name"]')

    def setUp(self):
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(5)
        self.chrome.get('https://the-internet.herokuapp.com/')

    def tearDown(self):
        self.chrome.quit()

    # @unittest.skip
    def test_context(self):
        self.chrome.find_element(*self.CONTEXT).click()
        # action chains ne ajuta sa dam click dreapta
        action = ActionChains(self.chrome)
        elem = self.chrome.find_element(*self.BOX)
        action.context_click(elem).perform()
        sleep(3)
        # comanda cu care dam ok pe alerte
        self.chrome.switch_to.alert.accept()
        sleep(2)
