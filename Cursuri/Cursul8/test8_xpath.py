# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
#
# # initializam chrome
# s = Service(ChromeDriverManager().install())
# chrome = webdriver.Chrome(service=s)
# # maximizam fereastra
# chrome.maximize_window()
#
# # navigam catre un url
# chrome.get('https://formy-project.herokuapp.com/form')
# selector by XPATH - atribut=valoare
# chrome.find_element(By.XPATH, '//input[@id="first-name"]').send_keys('M')
# selector by XPATH - folosind wildcard
# chrome.find_element(By.XPATH, '//*[@id="first-name"]').send_keys('Mat')
# selector by XPATH - navigare in jos trecand prin fiecare elemet
# chrome.find_element(By.XPATH, '//div/div/input[@id="first-name"]').send_keys('Matei')
# selector by XPATH - navigare in jos skip tags pana la elementul dorit
# chrome.find_element(By.XPATH, '//div//input[@id="first-name"]').send_keys('Matei CORVIN')
# selector by XPATH - luam elementul dorit din lista
# chrome.find_element(By.XPATH, '(//input[@class="form-control"])[2]').send_keys('Matei CORVIN')
# chrome.get('https://jules.app/search/all')
# chrome.find_element(By.XPATH, '//*[@role="presentation"]').click()
# xpath  search by text
# chrome.get('https://formy-project.herokuapp.com/form')
# chrome.find_element(By.XPATH, '//a[text()="Submit"]').click()
# xpath search by partial text
# chrome.get('https://formy-project.herokuapp.com/form')
# chrome.find_element(By.XPATH, '//a[contains(text(), "Sub")]').click()
# def formy_input_by_placeholder(placeholder_text, input_value):
#     my_input = chrome.find_element(By.XPATH, f'//input[@placeholder="{placeholder_text}"]')
#     my_input.clear()
#     my_input.send_keys(input_value)
#
#
# formy_input_by_placeholder('Enter first name', 'Aladin')
# formy_input_by_placeholder('Enter last name', 'SALAM')
# formy_input_by_placeholder('Enter your job title', 'QA AUTOMATION')

# def label_formy(label, input_value):
#     chrome.get('https://formy-project.herokuapp.com/form')
#     my_input = chrome.find_element(By.XPATH, f'//label[text()="{label}"]/parent::strong/parent::div//input')
#     my_input.clear()
#     my_input.send_keys(input_value)
#
#
# label_formy('Job title', 'INIJINER')
# label_formy('First name', 'Florin')
# label_formy('Last name', 'SALAM')
#
# sleep(5)
# chrome.quit()




