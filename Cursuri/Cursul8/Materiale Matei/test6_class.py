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
chrome.get('https://formy-project.herokuapp.com/form')


#selector by CLASS_NAME cand e unul singur , e ok daca avem Clasa unica
# chrome.find_element(By.CLASS_NAME, 'form-control').send_keys('Matei')

#daca gasim mai multe, le punem intr-o lista
input_list = chrome.find_elements(By.CLASS_NAME, 'form-control')
#print(input_list)
input_list[0].send_keys('TEST ALADIN')

sleep(3)
chrome.quit()




