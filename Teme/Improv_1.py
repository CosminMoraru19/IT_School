import unittest
from time import sleep
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class Test(unittest.TestCase):
    AB_ELEMENTS = (By.XPATH, '//*[@id="content"]/ul/li[1]/a')
    ADD_REMOVE_ELEMENTS = (By.XPATH, '//*[@id="content"]/ul/li[2]/a')
    BASIC_AUTENTIF = (By.XPATH,'//*[@id="content"]/ul/li[3]/a')
    BROKEN_IMAGE = (By.XPATH, '//*[@id="content"]/ul/li[4]/a')
    CHALLENGING_DOM = (By.XPATH, '//*[@id="content"]/ul/li[5]/a')
    CHECK_BOX = (By.XPATH, '//*[@id="content"]/ul/li[6]/a')
    CONTEXT_MENU = (By.XPATH, '//*[@id="content"]/ul/li[7]/a')
    DIGEST_AUTENTIF = (By.XPATH, '//*[@id="content"]/ul/li[8]/a')
    DISSAPEARING_ELEMENTS = (By.XPATH, '//*[@id="content"]/ul/li[9]/a')
    DRAG_DROP = (By.XPATH, '//*[@id="content"]/ul/li[10]/a')
    DROP_DOWN = (By.XPATH, '//*[@id="content"]/ul/li[11]/a')
    DYNAMIC_CONTENT = (By.XPATH,'//*[@id="content"]/ul/li[12]/a')
    DYNAMIC_CONTROL = (By.XPATH, '//*[@id="content"]/ul/li[13]/a')
    DYNAMIC_LOADING = (By.XPATH, '//*[@id="content"]/ul/li[14]/a')
    ENTRY_AD = (By.XPATH, '//*[@id="content"]/ul/li[15]/a')
    EXIT_INTENT = (By.XPATH, '//*[@id="content"]/ul/li[16]/a')
    FILE_DOWNLOAD = (By.XPATH, '//*[@id="content"]/ul/li[17]/a')
    FLOATING_MENU = (By.XPATH, '//*[@id="content"]/ul/li[19]/a')
    FORGET_PASSWORD = (By.XPATH, '//*[@id="content"]/ul/li[20]/a')
    FORM_AUTENTIF = (By.XPATH, '//*[@id="content"]/ul/li[21]/a')
    FRAMES = (By.XPATH, '//*[@id="content"]/ul/li[22]/a')

    def setUp(self) -> None:
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.get('https://the-internet.herokuapp.com')

    def tearDown(self) -> None:
        sleep(2)
        self.chrome.quit()

    def test_ADTesting(self):
        self.chrome.find_element(*self.AB_ELEMENTS).click()
        sleep(2)
        self.chrome.back()
        sleep(2)

    def test_ADRemove(self):
        self.chrome.find_element(*self.ADD_REMOVE_ELEMENTS).click()
        sleep(2)
        self.chrome.back()
        sleep(2)
    def test_BasicAutentif(self):
        self.chrome.find_element(*self.BASIC_AUTENTIF).click()
        sleep(2)
        self.chrome.back()
        sleep(2)

    def test_Broken_image(self):
        self.chrome.find_element(*self.BROKEN_IMAGE).click()
        sleep(2)
        self.chrome.back()
        sleep(2)

    def test_Challenging_Dom(self):
        self.chrome.find_element(*self.CHALLENGING_DOM).click()
        sleep(2)
        self.chrome.back()
        sleep(2)

    def test_check_box(self):
        self.chrome.find_element(*self.CHALLENGING_DOM).click()
        sleep(2)
        self.chrome.back()
        sleep(2)


