from pages.base_page import BasePage


class AddaMatchForm (BasePage):
    my_team_field_xpath = "//input[@name='myTeam']"
    enemy_team_field_xpath = "//input[@name='enemyTeam']"
    my_team_score_xpath = "//input[@name= 'myTeamScore']"
    enemy_team_score_xpath = "//input[@name='enemyTeamScore']"
    date_field_xpath = "//input[@name='date']"
    match_at_home_radiobutton_xpath = "//input[@name='matchAtHome' and contains(@value, 'true')]"
    match_out_home_radiobutton_xpath = "//input[@name='matchAtHome' and contains(@value, 'false')]"
    t_shirt_color_field_xpath = "//input[@name='tshirt']"
    league_field_xpath = "//input[@name='league']"
    time_played_field_xpath = "//input[starts-with(@name,'timePlayed')] "
    number_field_xpath = "//input[starts-with(@name,'number')] "
    web_match_field_xpath = "//input[@name='webMatch']"
    general_field_xpath = "//input[@name='general']"
    rating_field_xpath = "//input[@name='rating']"
    submit_button_xpath = "//button[@type='submit']//child::span[1]"
    clear_button_xpath = "//span[@class='MuiButton-label' and text()='Clear']"
    pass