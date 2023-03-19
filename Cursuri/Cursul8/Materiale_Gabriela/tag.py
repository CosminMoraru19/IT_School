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
chrome.find_element(By.LINK_TEXT, 'Form Authentication').click()
lista_input = chrome.find_elements(By.TAG_NAME, 'input')
lista_input[0].send_keys('tomsmith')
lista_input[1].send_keys('SuperSecretPassword! ')
time.sleep(5)