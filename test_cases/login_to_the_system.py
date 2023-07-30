import os
import unittest
from selenium import webdriver
from pages.dashboard import Dashboard
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from selenium.webdriver.chrome.service import Service
from pages.login_page import LoginPage
import time


class TestLoginPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://dareit.futbolkolektyw.pl/login')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_login_to_the_system(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page() #check if the title of the opened page is correct
        user_login.verify_header()
        user_login.type_in_email('user09@getnada.com') #enter "user09@getnada.com" in the email field
        user_login.type_in_password('Test-1234') #enter "Test-1234" in the password field
        user_login.click_on_the_sign_in_button() #click on the sign-in button
        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_page() #check if the title of the opened page is correct
        time.sleep(5)

    @classmethod
    def tearDown(self):
        self.driver.quit()
