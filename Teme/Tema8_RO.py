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
chrome.get('https://formy-project.herokuapp.com')

#accesarea pe baza class-ului

link_text = chrome.find_elements(By.LINK_TEXT, 'Autocomplete')
link_text.click()




sleep(100000)
chrome.quit()

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
chrome.get('https://formy-project.herokuapp.com/')


# selector by link_text
link_test = chrome.find_element(By.LINK_TEXT, 'Autocomplete')
link_test.click()

# chrome.find_element(By.LINK_TEXT, 'Autocomplete').click()

sleep(3)
chrome.quit()
