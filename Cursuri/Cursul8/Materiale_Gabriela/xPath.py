'''

//*[@id="last-name"] -- XPATH relativ care porneste de la un anumit element unic indentificabil pe pagina
/html/body/div/form/div/div[2]/input -- XPATH absolut care porneste de la inceputul paginii web



'''

import time

import selenium.webdriver.support.select
from selenium import webdriver
from selenium.webdriver.common.by import By


chrome = webdriver.Chrome()
time.sleep(2)
chrome.maximize_window()
chrome.get('https://formy-project.herokuapp.com/form')
# #1. Cautare dupa atribut= valoare pentru un tag specific
# chrome.find_element(By.XPATH, '//input[@placeholder="Enter first name"]').send_keys('Cosmin')
# time.sleep(2)
# #2. Cautare dupa atribut= valoare indiferent de tag
# chrome.find_element(By.XPATH, '//*[@placeholder="Enter first name"]').send_keys('CMArian')
# time.sleep(2)
# #3.  Cautare dupa copil prin navigare in jos
# # chrome.find_element(By.XPATH, "//div[@class='form-group']/div[3]/input]").send_keys("injiner")   #ceva nu merge la asta
# time.sleep(2)
# #//div[@class="input-group"]/div[2]/input
# #//*[@id="checkbox-1"]
# #//div[@class="input-group"]/following-sibling::div/div[2]/input
# chrome.find_element(By.XPATH, '//div[@class="input-group"]/div[2]/input').click()
# time.sleep(2)
# chrome.find_element(By.XPATH, '//*[@placeholder="Enter first name"]').clear()
# #4. Cautare cu or(compusa)-- Ambele codnitii sunt adevarate
# chrome.find_element(By.XPATH, '//input[@placeholder="Enter first name"]|/*[@placeholder="Enter last name"]').send_keys('Cautare cu or ')
#
# #5. Cautare cu or(compusa)-- doar a doua conditie este averata
#
# chrome.find_element(By.XPATH, '//input[@placeholder="Enter first names"] | /*[@placeholder="Enter last name"]').send_keys('Cautare cu or a doua oara') #ceva nu a mers
#
# #5. Cautare cu or(compusa)-- nicio conditie nu este adevara
# chrome.find_element(By.XPATH, '//input[@placeholder="Enter first names"] | /*[@placeholder="Enter last name"]').send_keys('Cautare cu or a doua oara') #ceva nu a mers

#6. Tratare drop down:

# years_of_experience = selenium.Select(chrome.find_element(By.XPATH,'//*[@id="select-menu"]'))
# time.sleep(2)
# years_of_experience.select_by_visible
# time.sleep(2)
"""
x y axis navigation
1. Navigare din parinte in copil se face cu caracterul / 
2. Navigare catre un urmas care nu este urmas direct se face cu caracterul //
3. Navigarea in sus catre parent se paote face cu "/parent::tag"
4. Putem sa navigam la urmatorul frate cu "/following-sibling::tag"
5. Putem sa navigam la frate anterios cu "/preceding-sibling::tag"
 
 //form/div/div/following-sibling::div[4]/preceding-sibling::div[3]
 //a[text()='Submit']
 //a[@role='button']
 
 
 Drop down:  
"""


time.sleep(5)