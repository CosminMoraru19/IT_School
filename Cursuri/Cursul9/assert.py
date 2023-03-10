from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)
chrome.maximize_window()

chrome.get('https://formy-project.herokuapp.com/')
chrome.find_element(By.LINK_TEXT, 'Autocomplete').click()
sleep(4)
actual = chrome.current_url
# expected = 'https://formy-project.herokuapp.com/buttons'
expected = 'https://formy-project.herokuapp.com/autocomplete'
sleep(1)
assert actual == expected, f'Url invalid: expected {expected}, found {actual}'
print('Test Passed')


