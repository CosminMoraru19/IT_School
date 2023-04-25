from time import sleep
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


# WebDriverWait(self.chrome, 5).until(EC.visibility_of_element_located(*self.TITLE))
# explicatie * din   * self.TITLE
# TITLE = *(By.XPATH, '//head/title') *- aceasta reprezinta tupla pentru constata denumita TITLE
# steluta de mai sus face "TUPLE UNPACKING" - adica despacheteaza tupla si o trimite mai departe informatiile din ea pentru a fi folosite


class Test2(TestCase):
    TITLE = (By.XPATH, '//head/title')
    ELEMENTAL_SELENIUM = (By.XPATH, '//a[contains(text(), "Elemental Selenium")]')
    ERROR = (By.XPATH, '//div/*[@id="flash"]')
    LOGIN_BUTTON = (By.XPATH, '//*[@id="login"]/button/i')
    ELEMENT = ''






    def setUp(self) -> None:
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(5)
        self.chrome.get('https://the-internet.herokuapp.com/login')


    def tearDown(self) -> None:
        self.chrome.quit()


    def test_check_url_title(self):
        actual = self.chrome.title
        expected = 'The Internet'
        self.assertEqual(actual, expected, 'Mesaj de test')


    def test_href_link(self):
        actual = self.chrome.find_element(*self.ELEMENTAL_SELENIUM).get_attribute('href')
        expected = 'http://elementalselenium.com/'
        self.assertEqual(actual, expected, 'The href link is not correct')

    def test_error_displayed(self):
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        actual = self.chrome.find_element(*self.ERROR).text
        expected = 'Your username is invalid!\n×'
        self.assertEqual(actual, expected, f'The {expected} message is not correct')
