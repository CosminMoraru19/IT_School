import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys


class Keyboard(unittest.TestCase):
    USER = (By.ID, 'username')

    def setUp(self) -> None:
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.get("https://the-internet.herokuapp.com/login")
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(5)

    # @unittest.skip
    def test_select_all(self):
        user = self.chrome.find_element(*self.USER)
        user.send_keys('Oltean Matei')
        sleep(2)
        user.clear()  #  metoda clear este folosita pentru a sterge tot continutul unui textbox
        sleep(2)
        user.send_keys('Oltean MATEI')
        sleep(2)
        user.send_keys(Keys.CONTROL, 'a')
        sleep(2)
        user.send_keys(Keys.BACKSPACE)
        sleep(2)
        user.send_keys('OLTEAN MATEI')
        sleep(2)
        user.send_keys(Keys.ARROW_LEFT)
        sleep(2)
        user.send_keys('test')
        sleep(2)

    # @unittest.skip
    def test_backs_pace_for(self):
        user = self.chrome.find_element(*self.USER)
        # user.send_keys('QWERTYUIOP')
        user.send_keys('a', 'b', 'c', 'd', 'e', 'f')
        sleep(4)
        for i in range(0, 5):
            user.send_keys(Keys.BACKSPACE)
            print(f'Am sters {i} data')
            sleep(0.5)
            i += 1
        sleep(3)

    def tearDown(self):
        self.chrome.quit()

# https://the-internet.herokuapp.com/key_presses

