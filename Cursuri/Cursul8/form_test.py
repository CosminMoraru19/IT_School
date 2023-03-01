from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.maximize_window()

driver.get('https://formy-project.herokuapp.com/form')


first_name = driver.find_element(By.ID, 'first-name')
first_name.send_keys('Matei')



sleep(10)
driver.quit()