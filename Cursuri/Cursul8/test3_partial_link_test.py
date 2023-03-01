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


#selector by partial_link_test
# try:
partial_link_test = chrome.find_element(By.PARTIAL_LINK_TEXT, 'and disabled')
partial_link_test.click()
# except Exception as e:
#     print(f'Nu am gasit elementul cautat')
# print('Am ajuns aici')
sleep(3)
chrome.quit()




