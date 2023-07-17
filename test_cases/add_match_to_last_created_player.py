import os
import unittest
from selenium import webdriver

from pages.dashboard import Dashboard
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from selenium.webdriver.chrome.service import Service
from pages.login_page import LoginPage
from pages.edit_player import EditPlayer
from pages.add_match_player import AddMatchPlayer



class TestAddMatchPlayer(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/login')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_add_match_to_last_created_player(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page() #check if the title of the opened page is correct
        user_login.type_in_email('user09@getnada.com') #enter "user09@getnada.com" in the email field
        user_login.type_in_password('Test-1234') #enter "Test-1234" in the password field
        user_login.click_on_the_sign_in_button() #click on the sign in button
        dashboard_page = Dashboard(self.driver)
        dashboard_page.click_on_the_last_created_player_button()
        edit_player_page = EditPlayer(self.driver)
        edit_player_page.click_on_the_matches_button()
        edit_player_page.click_on_the_add_match_button_xpath()
        add_match_player = AddMatchPlayer(self.driver)
        add_match_player.type_in_my_team_field('Loki')
        add_match_player.type_in_enemy_team_field("Asgard")
        add_match_player.type_in_my_team_score('5')
        add_match_player.type_in_enemy_team_score('4')
        add_match_player.type_in_date('10.10.2022')
        add_match_player.click_on_the_match_at_home_radiobutton()
        add_match_player.click_on_the_submit_button()

    @classmethod
    def tearDown(self):
            self.driver.quit()
