from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from datetime import date


# initializam chrome
s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)
chrome.maximize_window()

# how to get rid of an ad
chrome.get('https://www.techlistic.com/p/selenium-practice-form.html')

# Selector by partial link text

try:
    Click_cookies = chrome.find_element(By.ID, 'ez-accept-all').click()

except Exception as e:
    print('Ceva nu a functionat class accept de cookies')


action = ActionChains(chrome)
action.move_by_offset(10, 10). click().perform()
action.move_by_offset(10, 10). click().perform()
action.move_by_offset(10, 10). click().perform()
action.move_by_offset(10, 10). click().perform()

sleep(20)
try:
    Click_AD1 = chrome.find_element(By.ID, 'ezmob-footer-close').click()

except Exception as e:
    print('Ceva nu a functionat la click ad1')

try:
    Click_AD2 = chrome.find_element(By.ID, 'cookieChoiceDismiss').click()

except Exception as e:
    print('Ceva nu a functionat la click ad2')

sleep(2)

try:
    First_name = chrome.find_element(By.NAME, 'firstname').send_keys('Moraru')

except Exception as e:
    print('Ceva nu a functionat la Last Name')

try:
    Last_name = chrome.find_element(By.NAME, 'lastname').send_keys('Moraru')

except Exception as e:
    print('Ceva nu a functionat la Last Name')

try:
    Sex = chrome.find_element(By.ID , 'sex-0').click()

except Exception as e:
    print('Ceva nu a functionat la sex')

try:
    Exp1 = chrome.find_element(By.ID , 'exp-0').click()

except Exception as e:
    print('Ceva nu a functionat la exp1')

try:
    Exp2 = chrome.find_element(By.ID , 'exp-1').click()

except Exception as e:
    print('Ceva nu a functionat la exp2')

try:
    Exp5 = chrome.find_element(By.ID , 'exp-5').click()

except Exception as e:
    print('Ceva nu a functionat la exp5')

try:

    Data = chrome.find_element(By.ID , 'datepicker').send_keys(date.today())

except Exception as e:
    print('Ceva nu a functionat la data')

try:

    Profesion = chrome.find_element(By.ID , 'profession-1').click()

except Exception as e:
    print('Ceva nu a functionat la profesion')

try:

    Profesion = chrome.find_element(By.ID , 'profession-1').click()

except Exception as e:
    print('Ceva nu a functionat la profesion')

try:

    Automation_tool = chrome.find_element(By.ID , 'tool-0').click()

except Exception as e:
    print('Ceva nu a functionat la automation tool')

try:

    Continente = chrome.find_element(By.XPATH , f'//*[@id="continents"]/option[4]').click()

except Exception as e:
    print('Ceva nu a functionat la automation continente')

try:

    Selenium_comand = chrome.find_element(By.XPATH , f'//*[@id="selenium_commands"]/option[4]').click()

except Exception as e:
    print('Ceva nu a functionat la selenium comand')


sleep(10000)
chrome.quit()