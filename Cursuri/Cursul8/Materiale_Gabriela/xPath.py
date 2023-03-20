'''

//*[@id="last-name"] -- XPATH relativ care porneste de la un anumit element unic indentificabil pe pagina
/html/body/div/form/div/div[2]/input -- XPATH absolut care porneste de la inceputul paginii web



'''

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()
time.sleep(2)
chrome.maximize_window()
chrome.get('https://formy-project.herokuapp.com/form')
#1. Cautare dupa atribut= valoare pentru un tag specific
chrome.find_element(By.XPATH, '//input[@placeholder="Enter first name"]').send_keys('Cosmin')
time.sleep(2)
#2. Cautare dupa atribut= valoare indiferent de tag
chrome.find_element(By.XPATH, '//*[@placeholder="Enter first name"]').send_keys('CMArian')
time.sleep(2)
#3.  Cautare dupa copil prin navigare in jos
# chrome.find_element(By.XPATH, "//div[@class='form-group']/div[3]/input]").send_keys("injiner")   #ceva nu merge la asta
time.sleep(2)
#//div[@class="input-group"]/div[2]/input
#//*[@id="checkbox-1"]
#//div[@class="input-group"]/following-sibling::div/div[2]/input
chrome.find_element(By.XPATH, '//div[@class="input-group"]/div[2]/input').click()
time.sleep(2)
chrome.find_element(By.XPATH, '//*[@placeholder="Enter first name"]').clear()



time.sleep(5)