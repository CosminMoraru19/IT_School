import time
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()
time.sleep(2)
chrome.maximize_window()
chrome.get('https://formy-project.herokuapp.com/autocomplete')
chrome.find_element(By.ID, 'autocomplete').send_keys('Cosmin')
time.sleep(1)
try:
    chrome.find_element(By.CLASS_NAME, 'dismissButton').click()
except:
    print('Nu a functionat')
time.sleep(10)