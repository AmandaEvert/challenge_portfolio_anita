import os
import unittest
from selenium import webdriver
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from selenium.webdriver.chrome.service import Service
from pages.login_page import LoginPage
from pages.add_a_player import AddPlayer
from pages.dashboard import Dashboard
from PIL import Image



class TestAddPlayer(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/login')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_add_a_player(self):
        user_login = LoginPage(self.driver)
        user_login.type_in_email('user09@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_the_sign_in_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.click_on_the_add_a_player_button()
        add_a_player_page = AddPlayer(self.driver)
        add_a_player_page.type_in_email("anna@gmail.com")
        add_a_player_page.type_in_name("Anna")
        add_a_player_page.type_in_surname("Kolorowa")
        add_a_player_page.type_in_age("10.12.2000")
        add_a_player_page.type_in_main_position("555")
        add_a_player_page.click_on_leg_dropdown()
        add_a_player_page.click_on_left_leg_dropdown()
        add_a_player_page.click_on_the_submit_button()
        add_a_player_page.click_on_the_main_page_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.verify_last_added_player()
        self.driver.save_screenshot(r"C:\Users\Anita\Documents\GitHub\Challenge_portfolio_anita\test_cases\Screenshots\add_a_player\TC2.png")
        img = Image.open(r"C:\Users\Anita\Documents\GitHub\Challenge_portfolio_anita\test_cases\Screenshots\add_a_player\TC2.png")
        img.show()


    @classmethod
    def tearDown(self):
        self.driver.quit()
