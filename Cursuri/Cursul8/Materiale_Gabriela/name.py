import time
from selenium import webdriver
from selenium.webdriver.common.by import By

"""

"""
chrome = webdriver.Chrome()
time.sleep(2)
chrome.maximize_window()
chrome.get('http://www.seleniumframework.com/Practiceform/')
chrome.find_element(By.NAME, 'name').send_keys('Cosmin')
time.sleep(1)
lista_emails = chrome.find_elements(By.NAME, 'email')
lista_emails[1].send_keys('cosminmoraru@gmail.com')
time.sleep(1)
chrome.find_element(By.NAME, 'telephone').send_keys('0731267630')
time.sleep(1)
chrome.find_element(By.NAME, 'country').send_keys('Romania')
time.sleep(1)
chrome.find_element(By.NAME, 'company').send_keys('Kellogggs')
time.sleep(1)
chrome.find_element(By.NAME, 'message').send_keys('Mesaj formulat agwersesrtttttttttttttttttttttttttttttttttttttt')
time.sleep(1)
chrome.find_element(By.LINK_TEXT, 'Submit').click()
time.sleep(20)

