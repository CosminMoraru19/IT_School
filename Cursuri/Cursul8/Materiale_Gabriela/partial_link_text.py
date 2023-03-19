import time
from selenium import webdriver
from selenium.webdriver.common.by import By

"""
<a href="/login">Form Authentication</a>
"""



chrome = webdriver.Chrome()
time.sleep(2)
chrome.maximize_window()
chrome.get('https://the-internet.herokuapp.com')
chrome.find_element(By.PARTIAL_LINK_TEXT, 'Authentication').click()
time.sleep(1)