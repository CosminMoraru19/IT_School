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
try:
    last_name = chrome.find_element(By.ID, 'last-name')
    last_name.send_keys('Moraru')
except Exception as e:
    print('ID-ul numelui introdus nu este corect')

try:
    job_title = chrome.find_element(By.ID, 'job-title')
    job_title.send_keys('Inginer')
except Exception as e:
    print('ID-ul job-ului introdus nu este corect')

try:
    scoala = chrome.find_element(By.ID, 'radio-button-1').click()

except Exception as e:
    print('ID-ul introdus nu este corect')

try:
    sex = chrome.find_element(By.ID, 'checkbox-1').click()

except Exception as e:
    print('ID-ul introdus nu este corect')

try:
    Ani_experienta = chrome.find_element(By.ID, 'select-menu').click()

except Exception as e:
    print('ID-ul introdus nu este corect')

try:
    Data = chrome.find_element(By.ID, 'select-menu').click()

except Exception as e:
    print('ID-ul introdus nu este corect')




print('Pagina s-a completat')
# chrome.find_element(By.ID, 'first-name').send_keys('TEST AUTOMATION')

sleep(100000)
# chrome.quit()