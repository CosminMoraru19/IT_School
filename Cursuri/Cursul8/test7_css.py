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


# selector by CSS SELECTOR - ID
chrome.find_element(By.CSS_SELECTOR, 'input#first-name').send_keys('test1')

# selector by CSS Class - only first one if multiple matches
chrome.find_element(By.CSS_SELECTOR, 'input.form-control').send_keys('test2')

# selector by CSS atribut-valoare
chrome.find_element(By.CSS_SELECTOR, 'input[placeholder="Enter last name"]').send_keys('test3')

# selector by CSS atribut-valoare partiala + parinte -> copil
chrome.find_element(By.CSS_SELECTOR, 'div input[placeholder*="last name"]').send_keys('test4')


sleep(52415)
chrome.quit()




