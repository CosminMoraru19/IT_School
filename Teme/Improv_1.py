import unittest
from time import sleep
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class Test(unittest.TestCase):
    AB_ELEMENTS = (By.XPATH, '//*[@id="content"]/ul/li[1]/a')
    ADD_REMOVE_ELEMENTS = (By.XPATH, '//*[@id="content"]/ul/li[2]/a')
    BASIC_AUTENTIF = (By.XPATH,'//*[@id="content"]/ul/li[3]/a')
    BROKEN_IMAGE = (By.XPATH, '//*[@id="content"]/ul/li[4]/a')
    CHALLENGING_DOM = (By.XPATH, '//*[@id="content"]/ul/li[5]/a')
    CHECK_BOX = (By.XPATH, '//*[@id="content"]/ul/li[6]/a')
    CONTEXT_MENU = (By.XPATH, '//*[@id="content"]/ul/li[7]/a')
    DIGEST_AUTENTIF = (By.XPATH, '//*[@id="content"]/ul/li[8]/a')
    DISSAPEARING_ELEMENTS = (By.XPATH, '//*[@id="content"]/ul/li[9]/a')
    DRAG_DROP = (By.XPATH, '//*[@id="content"]/ul/li[10]/a')
    DROP_DOWN = (By.XPATH, '//*[@id="content"]/ul/li[11]/a')
    DYNAMIC_CONTENT = (By.XPATH,'//*[@id="content"]/ul/li[12]/a')
    DYNAMIC_CONTROL = (By.XPATH, '//*[@id="content"]/ul/li[13]/a')
    DYNAMIC_LOADING = (By.XPATH, '//*[@id="content"]/ul/li[14]/a')
    ENTRY_AD = (By.XPATH, '//*[@id="content"]/ul/li[15]/a')
    EXIT_INTENT = (By.XPATH, '//*[@id="content"]/ul/li[16]/a')
    FILE_DOWNLOAD = (By.XPATH, '//*[@id="content"]/ul/li[17]/a')
    FILE_UPLOAD = (By.XPATH, '//*[@id="content"]/ul/li[18]/a')
    FLOATING_MENU = (By.XPATH, '//*[@id="content"]/ul/li[19]/a')
    FORGET_PASSWORD = (By.XPATH, '//*[@id="content"]/ul/li[20]/a')
    FORM_AUTENTIF = (By.XPATH, '//*[@id="content"]/ul/li[21]/a')
    FRAMES = (By.XPATH, '//*[@id="content"]/ul/li[22]/a')
    GEOLOCATION = (By.XPATH, '//*[@id="content"]/ul/li[23]/a')
    HORIZONTAL_SLIDER = (By.XPATH, '//*[@id="content"]/ul/li[24]/a')
    HOVERS = (By.XPATH, '//*[@id="content"]/ul/li[25]/a')
    INFINITE_SCROLL = (By.XPATH, '//*[@id="content"]/ul/li[26]/a')
    INPUTS = (By.XPATH, '//*[@id="content"]/ul/li[27]/a')
    JQUERY_UI_MENU = (By.XPATH, '//*[@id="content"]/ul/li[28]/a')
    JAVASCRIPTALERT = (By.XPATH, '//*[@id="content"]/ul/li[29]/a')
    JAVASCRIPT_ONLOAD = (By.XPATH, '//*[@id="content"]/ul/li[30]/a')
    KEY_PROGRESS = (By.XPATH, '//*[@id="content"]/ul/li[31]/a')
    LARGE_DEEP_DOM = (By.XPATH, '//*[@id="content"]/ul/li[32]/a')
    MULTIPLE_WINDOWS = (By.XPATH, '//*[@id="content"]/ul/li[33]/a')
    NESTED_FRAMES = (By.XPATH, '//*[@id="content"]/ul/li[34]/a')
    NOTIFICATION_MESSAGE = (By.XPATH, '//*[@id="content"]/ul/li[35]/a')
    REDIRECT_LINK = (By.XPATH, '//*[@id="content"]/ul/li[36]/a')
    SECURE_FILE_DOWNLOAD = (By.XPATH, '//*[@id="content"]/ul/li[37]/a')
    SHADOW_DOM = (By.XPATH, '//*[@id="content"]/ul/li[38]/a')
    SHIFTING_CONTENT = (By.XPATH, '//*[@id="content"]/ul/li[39]/a')
    SLOW_RESOURCES = (By.XPATH, '//*[@id="content"]/ul/li[40]/a')
    SORTABLE_DATA_TABLES = (By.XPATH, '//*[@id="content"]/ul/li[41]/a')
    STATUS_CODES = (By.XPATH, '//*[@id="content"]/ul/li[42]/a')
    TYPOS = (By.XPATH, '//*[@id="content"]/ul/li[43]/a')
    WYSIWYG_EDITORS = (By.XPATH, '//*[@id="content"]/ul/li[44]/a')

    def setUp(self) -> None:
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.get('https://the-internet.herokuapp.com')

    def tearDown(self) -> None:
        sleep(2)
        self.chrome.quit()

    def test_ADTesting(self):
        self.chrome.find_element(*self.AB_ELEMENTS).click()

        sleep(2)
        self.chrome.back()
        sleep(2)

    def test_ADRemove(self):
        self.chrome.find_element(*self.ADD_REMOVE_ELEMENTS).click()
        self.chrome.find_element(By.XPATH, '//*[@id="content"]/div/button').click()
        self.chrome.find_element(By.XPATH, '//*[@id="content"]/div/button').click()
        self.chrome.find_element(By.XPATH, '//*[@id="content"]/div/button').click()
        self.chrome.find_element(By.XPATH, '//*[@id="content"]/div/button').click()
        self.chrome.find_element(By.CLASS_NAME, 'added-manually').click()
        sleep(1)
        self.chrome.find_element(By.CLASS_NAME, 'added-manually').click()
        sleep(1)
        self.chrome.find_element(By.CLASS_NAME, 'added-manually').click()
        self.chrome.find_element(By.CLASS_NAME, 'added-manually').click()
        sleep(2)
        self.chrome.back()
        sleep(2)
    def test_BasicAutentif(self):
        self.chrome.find_element(*self.BASIC_AUTENTIF).click()
        sleep(2)
        self.chrome.back()
        sleep(2)

    def test_Broken_image(self):
        self.chrome.find_element(*self.BROKEN_IMAGE).click()
        sleep(2)
        self.chrome.back()
        sleep(2)

    def test_Challenging_Dom(self):
        self.chrome.find_element(*self.CHALLENGING_DOM).click()
        sleep(2)
        self.chrome.back()
        sleep(2)

    def test_check_box(self):
        self.chrome.find_element(*self.CHECK_BOX).click()
        self.chrome.find_element(By.XPATH, '//*[@id="checkboxes"]/input[1]').click()
        sleep(1)
        self.chrome.find_element(By.XPATH, '//*[@id="checkboxes"]/input[1]').click()
        sleep(1)
        self.chrome.find_element(By.XPATH, '//*[@id="checkboxes"]/input[2]').click()
        sleep(1)
        self.chrome.find_element(By.XPATH, '//*[@id="checkboxes"]/input[2]').click()
        sleep(2)
        self.chrome.back()
        sleep(2)

    def test_context_menu(self):
        self.chrome.find_element(*self.CONTEXT_MENU).click()
        sleep(2)
        self.chrome.back()
        sleep(2)

    def test_digest_autentif(self):
        self.chrome.find_element(*self.DIGEST_AUTENTIF).click()
        sleep(2)
        self.chrome.back()
        sleep(2)

    def test_disapearing_elen(self):
        self.chrome.find_element(*self.DISSAPEARING_ELEMENTS).click()
        self.chrome.find_element(By.XPATH,'//*[@id="content"]/div/ul/li[2]/a').click()
        sleep(2)
        self.chrome.back()
        sleep(2)
        self.chrome.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[3]/a').click()
        sleep(2)
        self.chrome.back()
        sleep(2)
        self.chrome.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[4]/a').click()
        sleep(2)
        self.chrome.back()
        sleep(2)
        self.chrome.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[1]/a').click()
        sleep(2)

    def test_drag_drop(self):
        self.chrome.find_element(*self.DRAG_DROP).click()
        sleep(2)
        self.chrome.back()
        sleep(2)

    def test_dropdown(self):
        self.chrome.find_element(*self.DROP_DOWN).click()
        sleep(2)
        self.chrome.back()
        sleep(2)

    def test_dynamic_content(self):
        self.chrome.find_element(*self.DYNAMIC_CONTENT).click()
        sleep(2)
        self.chrome.back()
        sleep(2)

    def test_dynamic_controls(self):
        self.chrome.find_element(*self.DYNAMIC_CONTROL).click()
        sleep(2)
        self.chrome.back()
        sleep(2)

    def test_dynamic_loading(self):
        self.chrome.find_element(*self.DYNAMIC_LOADING).click()
        sleep(2)
        self.chrome.back()
        sleep(2)

    def test_entry_AD(self):
        self.chrome.find_element(*self.ENTRY_AD).click()
        sleep(2)
        self.chrome.back()
        sleep(2)

    def test_exit_intent(self):
        self.chrome.find_element(*self.EXIT_INTENT).click()
        sleep(2)
        self.chrome.back()
        sleep(2)

    def test_file_downlaod(self):
        self.chrome.find_element(*self.FILE_DOWNLOAD).click()
        sleep(2)
        self.chrome.back()
        sleep(2)

    def test_file_upload(self):
        self.chrome.find_element(*self.FILE_UPLOAD).click()
        sleep(2)
        self.chrome.back()
        sleep(2)

    def test_floating_menu(self):
        self.chrome.find_element(*self.FLOATING_MENU).click()
        sleep(2)
        self.chrome.back()
        sleep(2)

    def test_forget_pass(self):
        self.chrome.find_element(*self.FORGET_PASSWORD).click()
        sleep(2)
        self.chrome.back()
        sleep(2)

    def test_form_autentif(self):
        self.chrome.find_element(*self.FORM_AUTENTIF).click()
        sleep(2)
        self.chrome.back()
        sleep(2)

    def test_frame(self):
        self.chrome.find_element(*self.FRAMES).click()
        sleep(2)
        self.chrome.back()
        sleep(2)

    def test_geolocation(self):
        self.chrome.find_element(*self.GEOLOCATION).click()
        sleep(2)
        self.chrome.back()
        sleep(2)

    def test_horizontal_slider(self):
        self.chrome.find_element(*self.HORIZONTAL_SLIDER).click()
        sleep(2)
        self.chrome.back()
        sleep(2)

    def test_hovers(self):
        self.chrome.find_element(*self.HOVERS).click()
        sleep(2)
        self.chrome.back()
        sleep(2)

    def test_infinite_scroll(self):
        self.chrome.find_element(*self.INFINITE_SCROLL).click()
        sleep(2)
        self.chrome.back()
        sleep(2)

    def test_inputs(self):
        self.chrome.find_element(*self.INPUTS).click()
        sleep(2)
        self.chrome.back()
        sleep(2)

    def test_jquery_UI(self):
        self.chrome.find_element(*self.JQUERY_UI_MENU).click()
        sleep(2)
        self.chrome.back()
        sleep(2)

    def test_JV_alerts(self):
        self.chrome.find_element(*self.JAVASCRIPTALERT).click()
        sleep(2)
        self.chrome.back()
        sleep(2)

    def test_JV_onload_event(self):
        self.chrome.find_element(*self.JAVASCRIPT_ONLOAD).click()
        sleep(2)
        self.chrome.back()
        sleep(2)

    def test_key_presses(self):
        self.chrome.find_element(*self.KEY_PROGRESS).click()
        sleep(2)
        self.chrome.back()
        sleep(2)

    def test_large_deep_dom(self):
        self.chrome.find_element(*self.LARGE_DEEP_DOM).click()
        sleep(2)
        self.chrome.back()
        sleep(2)

    def test_multiple_window(self):
        self.chrome.find_element(*self.MULTIPLE_WINDOWS).click()
        sleep(2)
        self.chrome.back()
        sleep(2)

    def test_nested_frames(self):
        self.chrome.find_element(*self.NESTED_FRAMES).click()
        sleep(2)
        self.chrome.back()
        sleep(2)

    def test_notif_message(self):
        self.chrome.find_element(*self.NOTIFICATION_MESSAGE).click()
        sleep(2)
        self.chrome.back()
        sleep(2)

    def test_redirect_link(self):
        self.chrome.find_element(*self.REDIRECT_LINK).click()
        sleep(2)
        self.chrome.back()
        sleep(2)

    def test_secure_file_download(self):
        self.chrome.find_element(*self.SECURE_FILE_DOWNLOAD).click()
        sleep(2)
        self.chrome.back()
        sleep(2)

    def test_shadown_dom(self):
        self.chrome.find_element(*self.SHADOW_DOM).click()
        sleep(2)
        self.chrome.back()
        sleep(2)

    def test_shifting_content(self):
        self.chrome.find_element(*self.SHIFTING_CONTENT).click()
        sleep(2)
        self.chrome.back()
        sleep(2)

    def test_slow_resurse(self):
        self.chrome.find_element(*self.SLOW_RESOURCES).click()
        sleep(2)
        self.chrome.back()
        sleep(2)

    def test_sortable_data(self):
        self.chrome.find_element(*self.SORTABLE_DATA_TABLES).click()
        sleep(2)
        self.chrome.back()
        sleep(2)

    def test_status_codes(self):
        self.chrome.find_element(*self.STATUS_CODES).click()
        sleep(2)
        self.chrome.back()
        sleep(2)

    def test_WYSIWYG_Edistor(self):
        self.chrome.find_element(*self.WYSIWYG_EDITORS).click()
        sleep(2)
        self.chrome.back()
        sleep(2)