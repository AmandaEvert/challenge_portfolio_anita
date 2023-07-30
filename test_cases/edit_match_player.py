import os
import unittest
import time
from selenium import webdriver
from pages.dashboard import Dashboard
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from selenium.webdriver.chrome.service import Service
from pages.login_page import LoginPage
from pages.edit_match_player import EditMatchPlayer


class TestEditMatchPlayer(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://dareit.futbolkolektyw.pl/')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_edit_match_player(self):
        user_login = LoginPage(self.driver)
        user_login.type_in_email('user09@getnada.com') #enter "user09@getnada.com" in the email field
        user_login.type_in_password('Test-1234') #enter "Test-1234" in the password field
        user_login.click_on_the_sign_in_button() #click on the sign in button
        dashboard_page = Dashboard(self.driver)
        dashboard_page.click_on_the_last_created_match_button()
        edit_match_player_page = EditMatchPlayer(self.driver)
        edit_match_player_page.clear_enemy_team_field()
        edit_match_player_page.type_in_enemy_team_field('Soki')
        edit_match_player_page.click_on_the_submit_button()
        edit_match_player_page.click_on_the_main_page_button()
        time.sleep(5)

    @classmethod
    def tearDown(self):
        self.driver.quit()



