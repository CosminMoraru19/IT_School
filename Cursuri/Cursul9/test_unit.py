import unittest
from time import sleep
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Test(TestCase):


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
    # se rulaza inainte de fiecare test si are rolul de a face setupul de chrome inainte de fiecare test


    def setUp(self) -> None:
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.get('https://formy-project.herokuapp.com/form')

    def tearDown(self) -> None:
        self.chrome.quit()


    def test_check_url(self):
        actual = self.chrome.current_url
        expected = 'https://formy-project.herokuapp.com/form'
        self.assertEqual(actual, expected, 'Pagina deschisa nu este corecta')

    def test_page_title_back_button(self):
        try:
            self.chrome.get('https://formy-project.herokuapp.com/buttons')
            expected = self.chrome.find_element(*self.FORMY_PAGE_TITLE)
            assert expected == 'element="fa956a8c-01e9-4b41-ab2d-4b3137ddd8d8"'
            print(expected)
        except Exception:
            print('The page title button is not displayed')
        try:
            self.chrome.get('https://formy-project.herokuapp.com/buttons')
            self.chrome.find_element(*self.FORMY_PAGE_TITLE).click()
            WebDriverWait(self.chrome, 5).until(EC.visibility_of_element_located(self.WELCOME_TO_FORMY_TEXT))
        except Exception:
            print('The text is not displayed')


    def test_element_visible(self):
        self.chrome.find_element(*self.SUBMIT_BTN).click()
        actual = WebDriverWait(self.chrome, 3).until(EC.text_to_be_present_in_element
                                                     ((By.XPATH, '//div/div[@role="alert"]'),
                                                      "The form was successfully submitted!"))
        if actual:
            print('Message found is correct')
        else:
            print(f'Message found incorrect')

    # to do



    def test_form(self):
        # WebDriverWait(self.chrome, 10).until(EC.presence_of_element_located((By.ID, "cookiedismiss"))).click()
        input_first_name = self.chrome.find_element(*self.FIRST_NAME_INPUT)
        input_first_name.send_keys('Nume')
        self.assertTrue(input_first_name.is_displayed(), 'Mesajul afisat este corect')
        sleep(1)
        self.chrome.find_element(*self.LAST_NAME_INPUT).send_keys('Prenume')
        sleep(1)
        self.chrome.find_element(*self.JOB_TITLE).send_keys('Tester')
        sleep(1)
        self.chrome.find_element(*self.HIGH_SCHOOL_BTN).click()
        sleep(1)
        self.chrome.find_element(*self.MALE_CHEKBOX).click()
        sleep(1)
        self.chrome.find_element(*self.YRS_OF_EXP_0_1).click()
        sleep(1)
        self.chrome.find_element(*self.DATE_SELECT).click()
        sleep(3)
        self.chrome.get_screenshot_as_file('ss_pagina.png')
        self.chrome.find_element(*self.SUBMIT_BTN).click()
        sleep(1)
        actual = WebDriverWait(self.chrome, 3).until(EC.text_to_be_present_in_element
                                                     ((By.XPATH, '//div/div[@role="alert"]'),
                                                      "The form was successfully submitted!"))
        if actual:
            print('Message found is correct')
        else:
            print(f'Message found incorrect')


