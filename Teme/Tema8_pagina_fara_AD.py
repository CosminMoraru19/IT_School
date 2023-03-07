from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import datetime

# initializam chrome
s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)
chrome.maximize_window()

# how to get rid of an ad
chrome.get('https://www.techlistic.com/p/selenium-practice-form.html')

# Selector by partial link text

try:
    Click_cookies = chrome.find_element(By.ID, 'ez-accept-all').click()

except Exception as e:
    print('Ceva nu a functionat class accept de cookies')


action = ActionChains(chrome)
action.move_by_offset(10, 10). click().perform()
action.move_by_offset(10, 10). click().perform()
action.move_by_offset(10, 10). click().perform()
action.move_by_offset(10, 10). click().perform()



sleep(10000)
chrome.quit()