# pip install selenium
# pip install webdriver-manager

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

# navigam catre un url
chrome.get('https://formy-project.herokuapp.com/form')


#selector by ID
try:
    first_name = chrome.find_element(By.ID, 'first-name2')
    first_name.send_keys('Cosmin')
except Exception as e:
    print('ID-ul prenumelui introdus nu este corect')


print('Pagina s-a completat')
# chrome.find_element(By.ID, 'first-name').send_keys('TEST AUTOMATION')

sleep(100000)
# chrome.quit()
