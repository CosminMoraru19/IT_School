import unittest
from time import sleep
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Test(unittest.TestCase):


    # elementele din pagina
    # in loc sa le scriem de n ori in teste, le trecem aici o sg data
    TITLE = (By.XPATH, '//head/title')
    ELEMENTAL_SELENIUM = (By.XPATH, '//a[contains(text(), "Elemental Selenium")]')
    ERROR = (By.XPATH, '//div/*[@id="flash"]')
    LOGIN_BUTTON = (By.XPATH, '//*[@id="login"]/button/i')
    ELEMENT = ''
    USERNAME = (By.XPATH, '//*[@id="username"]')
    PASSWORD = (By.XPATH, '//*[@id="password"]')
    ERROR_CLOSE = (By.XPATH, '// *[ @ id = "flash"] / a')
    LOGOUT_BUTTON = (By.XPATH, '//*[@id="content"]/div/a/i')
    LOGINPAGE = (By.XPATH, '//h2')

    def setUp(self) -> None:
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.get('https://the-internet.herokuapp.com/login')

    def tearDown(self) -> None:
        self.chrome.quit()
#Test1
    def test_check_url(self):
        actual = self.chrome.current_url
        expected = 'https://the-internet.herokuapp.com/login'
        self.assertEqual(actual, expected, 'Pagina deschisa nu este corecta')
#Test2
    def test_check_url_title(self):
        actual = self.chrome.title
        expected = 'The Internet'
        self.assertEqual(actual,expected, 'Nu sunt egale')
# Test 3
    def test_xpath_corect(self):
        actual = self.chrome.find_element(*self.LOGINPAGE).text
        expected = 'Login Page'
        self.assertEqual(actual, expected, 'Nu sunt egale')
# Test4
# de intrebat
    def test_buton_activ(self):
        actual =  self.chrome.find_element(*self.LOGIN_BUTTON).is_enabled()
        expected = True
        self.assertEqual(actual,expected, 'Butonul nu este activ')

# Test5
    def test_href_link(self):
        actual = self.chrome.find_element(*self.ELEMENTAL_SELENIUM).get_attribute('href')
        expected = 'http://elementalselenium.com/'
        self.assertEqual(actual, expected, 'The href link is not correct')
# Test6
    def test_direct_log_in(self):
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        actual = self.chrome.find_element(*self.ERROR).text
        expected = 'Your username is invalid!\n×'
        self.assertEqual(actual, expected, f'The {expected} message is not correct')
# Test7
    def test_login_incorect_user(self):
        self.chrome.find_element(*self.USERNAME).send_keys('CosminMoraru')
        self.chrome.find_element(*self.PASSWORD).send_keys('12345')
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        actual = self.chrome.find_element(*self.ERROR).text
        expected = 'Your username is invalid!\n×'
        self.assertEqual(actual, expected, f'The {expected} message is not correct')

# Test 8

# de verificat

    def test_verificare_eroare(self):
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        self.chrome.find_element(*self.ERROR_CLOSE).click()
        sleep(2)
        actual = self.chrome.find_element(*self.ERROR).text
        expected = None
        self.assertEqual(actual,expected, 'Eroarea nu mai este prezenta')

# Test9

# Test10
# Test11
    def test_Test11(self):
        self.chrome.find_element(*self.USERNAME).send_keys('tomsmith')
        self.chrome.find_element(*self.PASSWORD).send_keys('SuperSecretPassword!')
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        self.chrome.find_element(*self.LOGOUT_BUTTON).click()
        actual = self.chrome.current_url
        expected = 'https://the-internet.herokuapp.com/login'
        self.assertEqual(actual, expected, 'Pagina pe care ai ajuns nu e corecta ')
