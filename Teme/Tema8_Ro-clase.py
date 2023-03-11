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
    CLICK_COOKIES = (By.ID, 'ez-accept-all')
    # SELENIUM_WITH_JAVA = (By.XPATH, '//*[@id="PageList2"]/div/div[1]/div[1]/div/ul/li[2]/div/div/a[1]')
    CLOSE_AD = (By.XPATH, '//*[@id="ezmob-footer-close"]')


    def setUp(self) -> None:
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.get('https://www.techlistic.com/')
        self.chrome.find_element(*self.CLICK_COOKIES).click()
        sleep(5)
        action = ActionChains(self.chrome)
        action.move_by_offset(20, 20).click().perform()
        action.move_by_offset(10, 10).click().perform()
        action.move_by_offset(20, 20).click().perform()
        action.move_by_offset(10, 10).click().perform()
        sleep(2)

    def tearDown(self) -> None:
        sleep(1000)
        self.chrome.quit()

    def test_go_selenium(self):
        self.chrome.get('https://www.techlistic.com/p/selenium-tutorials.html')
        sleep(15)
        self.chrome.find_element(*self.CLOSE_AD).click()
        self.chrome.find_element(By.XPATH, '//*[@id="cookieChoiceDismiss"]').click()
        self.chrome.find_element(By.XPATH, '//*[@id="post-body-1543620792068953318"]/div[3]/ol/li[1]/a').click()
        sleep(15)
        self.chrome.find_element(*self.CLOSE_AD).click()
        self.chrome.find_element(By.XPATH, '//*[@id="post-body-4019118787057659056"]/div/ul[4]/ul/li[2]/a').click()
        sleep(5)
        self.chrome.back()
        sleep(5)
        self.chrome.back()
        sleep(5)
        self.chrome.back()

    def test_simpu(self):
        self.chrome.get('https://www.techlistic.com/p/software-testing.html')
        sleep(20)
        self.chrome.find_element(*self.CLOSE_AD).click()
        self.chrome.find_element(By.XPATH, '//*[@id="cookieChoiceDismiss"]').click()
        self.chrome.find_element(By.XPATH, '//*[@id="post-body-4019118787057659056"]/div/ul[12]/ul/li/span/a').click()
        sleep(10)
