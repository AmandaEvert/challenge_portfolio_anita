from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage


class EditMatchPlayer(BasePage):
    my_team_field_xpath = "//input[@name='myTeam']"
    enemy_team_field_xpath = "//input[@name='enemyTeam']"
    my_team_score_xpath = "//input[@name= 'myTeamScore']"
    enemy_team_score_xpath = "//input[@name='enemyTeamScore']"
    date_field_xpath = "//input[@name='date']"
    match_at_home_radiobutton_xpath = "//input[@name='matchAtHome' and contains(@value, 'true')]"
    match_out_home_radiobutton_xpath = "//input[@name='matchAtHome' and contains(@value, 'false')]"
    submit_button_xpath = "//*/form/div[3]/button[1]/span[1]"

    def clear_enemy_team_field(self):
        self.wait_for_element_to_be_clickable(self.enemy_team_field_xpath)
        enemy_team_field = self.driver.find_element(By.XPATH, self.enemy_team_field_xpath)
        enemy_team_field.send_keys(Keys.CONTROL + "a")
        enemy_team_field.send_keys(Keys.DELETE)

    def type_in_enemy_team_field(self, enemy_team_field):
        self.wait_for_element_to_be_clickable(self.submit_button_xpath)
        self.field_send_keys(self.enemy_team_field_xpath, enemy_team_field)

    def click_on_the_submit_button(self):
        self.wait_for_element_to_be_clickable(self.submit_button_xpath)
        self.click_on_the_element(self.submit_button_xpath)





