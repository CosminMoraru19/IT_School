"""
Elementele dintr-un site web sunt identificabile print ointermediul unui tag:
Ex:
-id
-span
-a (ancora)
-td (table data)
-tr ( table row)
-ul (unordered list)
-ol (ordered list)
-li (list item)
-input
-h(h1,h2,h3....)
-div
-p (paragraph)


"""
import time

from selenium import webdriver
chrome = webdriver.Chrome()
time.sleep(2)
chrome.maximize_window()
chrome.get('https://the-internet.herokuapp.com')  # cu aceasta comanda se deschid site-uri
time.sleep(2)
chrome.quit()    #inchide toata intanta browserului
#chrome.close()   inchide un singur tab din isntanta broserului

























