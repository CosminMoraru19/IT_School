import time
from selenium import webdriver
from selenium.webdriver.common.by import By

"""
link text = textul care este pusul peste un link.
link-urile pe un site sunt definite prin intermediul unei ancore(tag-ul a)
un element de tip ancora are urmatoarele componeten:
1. tag-ul de inceput (a)
2. link-ul catre care se face navigarea ( href = 'valoare')
3. textul care este afisat peste lin (linktext)
4. tag-ul de sfarsit (/a)

<a href="/checkboxes">Checkboxes</a>
<a href="/login">Form Authentication</a>

"""
chrome = webdriver.Chrome()
time.sleep(2)
chrome.maximize_window()
chrome.get('https://the-internet.herokuapp.com')
chrome.find_element(By.LINK_TEXT, 'Checkboxes').click()
time.sleep(1)
chrome.back()
time.sleep(1)
chrome.find_element(By.LINK_TEXT, 'Form Authentication').click()
chrome.quit()

