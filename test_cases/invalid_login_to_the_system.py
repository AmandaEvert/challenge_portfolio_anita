import os
import unittest
from selenium import webdriver
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from selenium.webdriver.chrome.service import Service
from pages.login_page import LoginPage



class TestInvalidLoginPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_invalid_login_to_the_system(self):
        user_login = LoginPage(self.driver)
        user_login.type_in_email('user09@getnada.com')
        user_login.type_in_password('Test4321')
        user_login.click_on_the_sign_in_button()
        user_login.error_info_visible()
        self.driver.save_screenshot("C:\Users\Anita\Documents\GitHub\Challenge_portfolio_anita\test_cases\Screenshots\invalid_login_to_the_system\TC1.png")


    @classmethod
    def tearDown(self):
        self.driver.quit()