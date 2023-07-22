import os
import unittest
from selenium import webdriver
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from selenium.webdriver.chrome.service import Service
from pages.login_page import LoginPage
from pages.add_a_player import AddPlayer
from pages.dashboard import Dashboard
import time


class TestAddPlayer(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/login')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_add_a_player_change_leg(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page() #check if the title of the opened page is correct
        user_login.type_in_email('user09@getnada.com') #enter "user09@getnada.com" in the email field
        user_login.type_in_password('Test-1234') #enter "Test-1234" in the password field
        user_login.click_on_the_sign_in_button() #click on the sign-in button
        dashboard_page = Dashboard(self.driver)
        dashboard_page.click_on_the_add_a_player_button()
        add_a_player_page = AddPlayer(self.driver)
        add_a_player_page.select_leg("Right leg")
        time.sleep(3)
        add_a_player_page.select_leg("Left leg")
        time.sleep(3)

    @classmethod
    def tearDown(self):
        self.driver.quit()
