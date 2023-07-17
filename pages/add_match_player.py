from pages.base_page import BasePage


class AddMatchPlayer(BasePage):
    my_team_field_xpath = "//input[@name='myTeam']"
    enemy_team_field_xpath = "//input[@name='enemyTeam']"
    my_team_score_xpath = "//input[@name= 'myTeamScore']"
    enemy_team_score_xpath = "//input[@name='enemyTeamScore']"
    date_field_xpath = "//input[@name='date']"
    match_at_home_radiobutton_xpath = "//input[@name='matchAtHome' and contains(@value, 'true')]"
    match_out_home_radiobutton_xpath = "//input[@name='matchAtHome' and contains(@value, 'false')]"
    submit_button_xpath = "//*/form/div[3]/button[1]/span[1]"

    def type_in_enemy_team_field(self, enemy_team_field):
        self.wait_for_element_to_be_clickable(self.submit_button_xpath)
        self.field_send_keys(self.enemy_team_field_xpath, enemy_team_field)

    def click_on_the_submit_button(self):
        self.wait_for_element_to_be_clickable(self.submit_button_xpath)
        self.click_on_the_element(self.submit_button_xpath)

    def type_in_my_team_field(self, my_team_field):
        self.field_send_keys(self.my_team_field_xpath, my_team_field)

    def type_in_my_team_score(self, my_team_score):
        self.field_send_keys(self.enemy_team_score_xpath, my_team_score)

    def type_in_enemy_team_score(self, enemy_team_score):
        self.field_send_keys(self.enemy_team_score_xpath, enemy_team_score)

    def type_in_date(self, date):
        self.field_send_keys(self.date_field_xpath, date)

    def click_on_the_match_at_home_radiobutton(self):
        self.click_on_the_element(self.match_at_home_radiobutton_xpath)
