from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# initializam chrome
s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)
chrome.maximize_window()
#intram pe pagina unde vrem sa facem testul
# chrome.get('https://formy-project.herokuapp.com')

#selector pe baza link_text
# try:
#     Accesare_butoane = chrome.find_element(By.LINK_TEXT, 'Buttons').click()
# except Exception as e:
#     print('Ceva nu a fucntionat Link_txt Buttons')
# sleep(2)
# chrome.back()
# try:
#     Accesare_formular = chrome.find_element(By.LINK_TEXT, 'Autocomplete').click()
# except Exception as e:
#     print('Ceva nu a fucntionat Link_txt Autocomplete')
# sleep(1)
#
# #selector by ID link
# try:
#     Adresa = chrome.find_element(By.ID, 'autocomplete')
#     Adresa.send_keys('Calea 13 Septembrie')
# except Exception as e:
#     print('Ceva nu a fucntionat ID Atucomplete')
#
#
# # try:
# #     Click_ok = chrome.find_element(By.PARTIAL_LINK_TEXT, 'OK').click()             De intrebat mai departe
# # except Exception as e:
# #     print('Ceva nu a functionat class DismissButton')
#
# sleep(1)
# try:
#     Numarul = chrome.find_element(By.ID, 'street_number')
#     Numarul.send_keys('nr 45')
# except Exception as e:
#     print('Ceva nu a fucntionat ID street number')
# sleep(1)
# # selector by class
# try:
#     Scare = chrome.find_elements(By.CLASS_NAME, 'form-control')
#     Scare[2].send_keys('Scare 2')
# except Exception as e:
#     print('Ceva nu a functionat class form control')
# sleep(1)
# try:
#     Oras = chrome.find_elements(By.CLASS_NAME, 'form-control')
#     Oras[3].send_keys('Bucuresti')
# except Exception as e:
#     print('Ceva nu a functionat class form control')
#
#
# sleep(1)
#
# # selector by tag
# try:
#     Judet = chrome.find_elements(By.TAG_NAME, 'input')
#     Judet[4].send_keys('Judetul Ilfov')
# except Exception as e:
#     print('Ceva nu a functionat la tag judet')
# sleep(1)
#
# try:
#     Cod_Postal = chrome.find_elements(By.TAG_NAME, 'input')
#     Cod_Postal[5].send_keys('107600')
# except Exception as e:
#     print('Ceva nu a functionat la tag cod postal')
# sleep(1)
#
# try:
#     Tara = chrome.find_elements(By.TAG_NAME, 'input')
#     Tara[6].send_keys('Romania')
# except Exception as e:
#     print('Ceva nu a functionat la tag tara')
# sleep(2)
# chrome.back()


chrome.get('https://www.techlistic.com/p/selenium-practice-form.html')

#Selector by partial link text

try:
    Click_cookies = chrome.find_element(By.ID, 'ez-accept-all').click()
except Exception as e:
    print('Ceva nu a functionat class accept de cookies')

# try:
#     close_ad = chrome.find_element(By.ID, 'ad_position_box').click()
#     # close_ad[0].click()
# except Exception as e:
#     print('Ceva nu a functionat class form control')




sleep(100000)
chrome.quit()

