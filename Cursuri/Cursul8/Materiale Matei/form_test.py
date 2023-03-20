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
sleep(2)
input_list = driver.find_elements(By.CLASS_NAME, 'form-control')
input_list[1].send_keys('Oltean')
sleep(2)
my_input = driver.find_element(By.XPATH, f'//input[@placeholder="Enter your job title"]')
my_input.send_keys('Injiner')
sleep(2)
my_button = driver.find_element(By.XPATH, f'//input[@id="radio-button-2"]')
my_button.click()
sleep(2)
my_checkbox = driver.find_element(By.XPATH, f'//input[@id="checkbox-1"]')
my_checkbox.click()
sleep(2)
my_dropdown_select1 = driver.find_element(By.XPATH, f'//*[@id="select-menu"]')
my_dropdown_select1.click()
sleep(1)
my_dropdown_select2 = driver.find_element(By.XPATH, f'//*[@id="select-menu"]/option[4]')
my_dropdown_select2.click()
sleep(2)
date_picker = driver.find_element(By.XPATH, f'//*[@id="datepicker"]')
date_picker.click()
sleep(2)
date_select = driver.find_element(By.XPATH, f'//table//td[@data-date="1678492800000"]')
date_select.click()
sleep(2)
submit_button = driver.find_element(By.XPATH, '//a[contains(text(), "Sub")]')
submit_button.click()


driver.get('https://formy-project.herokuapp.com/thanks')
check_sub_message = driver.find_element(By.XPATH, f'//*[@role="alert"]')
check_sub_message.screenshot('submessage2.png')


sleep(3)

driver.quit()
