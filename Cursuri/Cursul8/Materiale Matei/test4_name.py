from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# initializam chrome
s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)
# maximizam fereastra
chrome.maximize_window()

#navigam catre un url
chrome.get('http://www.seleniumframework.com/Practiceform/')


#selector by name
# link_test = chrome.find_element(By.NAME, 'country')
# link_test.send_keys('Romania')

chrome.find_element(By.NAME, 'country').send_keys('Romania')

sleep(3)
chrome.quit()




