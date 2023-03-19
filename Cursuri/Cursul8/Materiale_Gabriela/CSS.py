'''
Cum sa gandim un sleector?
1.  #-> cautare dupa id
2. .-> cautare dupa clasa
3. daca preceam # sau . dupa numele unui tag, atunci sistemul va cauta elem. cu tag-ul repsectiv si id-ul / clasa respectiva
4. Putem sa cautam elemente cu un anumit tag cu filtrare de tipul atribut = valoare.
5. Putem sa cautam primul copil al unui element cu caracterul mai mare
6. Putem sa cautam orice copil al unui elem. daca separam tag-ul elementului de copilul sau prin spatiu.
7. Daca vrem sa cautam primul copil al unui element putem sa specificam "first-of-type"
8. Daca vrem sa cuatam ultimul copil al unui element putem sa specificam "last-of-type"
9. Daca vrem sa cautam un copil care nu este nici primul nici ultimul putem sa folosim "nth-of-type(specificand aici al catealea elem este)'
10. Daca vrem sa gasim un frate ulterior ne putem folosi de carcaterul +

De intrat pe CSS selectors W3Schooles.
'''






import time
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()
time.sleep(2)
chrome.maximize_window()
chrome.get('https://formy-project.herokuapp.com/form')

# chrome.find_element(By.CSS_SELECTOR, '#first-name').send_keys("Cosmin")
# #am facut cautare dupa ID
# chrome.find_element(By.CSS_SELECTOR, '#last-name').send_keys("Mircea")
# time.sleep(1)
# chrome.find_element(By.CSS_SELECTOR, '#last-name').clear()
# time.sleep(1)
# #cautare dupa atribut = valoare
# chrome.find_element(By.CSS_SELECTOR, 'input[placeholder="Enter last name"]').send_keys("Marian")
# time.sleep(1)
# # am facut cautare dupa clasa
# chrome.find_elements(By.CSS_SELECTOR, '.form-control')[2].send_keys('Tester')
#
# # Validare ca textul in pagina este cel din HTRMPL.
# test_label_class_name = chrome.find_element(By.CSS_SELECTOR, "strong > label[for='last-name']").text
# assert test_label_class_name == "Last name", f"Error, Expected - Last name -, Actual : {test_label_class_name}"

# chrome.find_element(By.CSS_SELECTOR, 'div.input-group>div:nth-of-type(2) > input').click()
# chrome.find_element(By.CSS_SELECTOR, 'div.input-group>div:last-of-type > input').click()
# highest_level_of_education = chrome.find_element(By.CSS_SELECTOR, 'div.input-group>div:first-of-type label').text
# assert highest_level_of_education == 'Highest level of education', f'Error, Except = Highest level of education - Actual: {highest_level_of_education}'
#
# college_education = chrome.find_element(By.CSS_SELECTOR, 'div.input-group>div:nth-of-type(3)').text
# assert college_education == 'College', f'Error: Expected: College, actual{college_education}'

chrome.find_element(By.CSS_SELECTOR, "div.form-group > div:nth-of-type(2) strong + input").send_keys('following sibblings')


