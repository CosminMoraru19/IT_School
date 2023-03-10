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
    SUBMIT_BTN = (By.XPATH, '//a[@role="button"]')
    FIRST_NAME_INPUT = (By.XPATH, '//input[@id="first-name"]')
    LAST_NAME_INPUT = (By.XPATH, '//input[@id="last-name"]')
    MESSAGE = (By.XPATH, '//div/div[@role="alert"]')
    JOB_TITLE = (By.XPATH, '//input[@id="job-title"]')
    HIGH_SCHOOL_BTN = (By.XPATH, '//*[@id="radio-button-1"]')
    COLLEGE_BTN = (By.XPATH, '//*[@id="radio-button-2"]')
    GRAD_SCHHOL_BTN = (By.XPATH, '//*[@id="radio-button-3"]')
    MALE_CHEKBOX = (By.XPATH, '//*[@id="checkbox-1"]')
    FEMALE_CHECKBOX = (By.XPATH, '//*[@id="checkbox-2"]')
    NOTHING_TOSAY_CHECKBOX = (By.XPATH, '//*[@id="checkbox-3"]')
    YRS_OF_EXP_0_1 = (By.XPATH, '//*[@id="select-menu"]/option[2]')
    DATE_SELECT = (By.XPATH, '//*[@id="datepicker"]')
    FORMY_PAGE_TITLE = (By.XPATH, '//*[@id="logo"]')
    WELCOME_TO_FORMY_TEXT = (By.XPATH, '//h1')

    def setUp(self) -> None:
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.get('https://the-internet.herokuapp.com')

    def tearDown(self) -> None:
        self.chrome.quit()

    def test_check_url(self):
        actual = self.chrome.current_url
        expected = 'https://the-internet.herokuapp.com/'
        self.assertEqual(actual, expected, 'Pagina deschisa nu este corecta')

    def test_check_url_title(self):
        actual = self.chrome.title
        expected = 'The Internet'
        self.assertEqual(actual,expected, 'Nu sunt egale')
