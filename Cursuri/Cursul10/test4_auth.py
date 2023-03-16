import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Authentication(unittest.TestCase):
    USERNAME = 'admin'
    PASSWORD = 'admin'

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get('https://the-internet.herokuapp.com/basic_auth')

    def tearDown(self):
        self.driver.quit()

    # @unittest.skip
    def test_auth(self):
        expected = "Congratulations! You must have the proper credentials."
        self.driver.get('https://' + self.USERNAME + ':' + self.PASSWORD + '@the-internet.herokuapp.com/basic_auth')
        sleep(3)

        actual = WebDriverWait(self.driver, 3).until(EC.text_to_be_present_in_element
                                                     ((By.XPATH, '//*[@id="content"]/div/p'),
                                                      "Congratulations! You must have the proper credentials."))
        self.assertTrue(expected, actual)
        print('Assert True a fost corect')

        # element = self.driver.switch_to.basic_auth = WebDriverWait(self.driver, timeout=30).until(
        # EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, 'The site is asking')))


# https://admin:admin@the-internet.herokuapp.com/basic_auth -> Pagina formatata fara variabile

# https://the-internet.herokuapp.com/basic_auth

