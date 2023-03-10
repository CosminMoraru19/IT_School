# pip install selenium
# pip install webdriver-manager

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)
chrome.maximize_window()
chrome.get('https://formy-project.herokuapp.com/form')
start_time = time.time()
try:
    chrome.find_element(By.ID, 'first-name').send_keys('ELON')
    chrome.find_element(By.ID, 'last-name').send_keys('MUSK')
    job_title = WebDriverWait(chrome, 8).until(EC.presence_of_element_located((By.ID, "job-title3")))
    job_title.send_keys('INJINER_TEST')
except Exception as e:
    end_time = time.time()
    elapsed = end_time - start_time
    print(elapsed)
    print(e)

# sleep(5)
# chrome.quit()
