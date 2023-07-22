from pages.base_page import BasePage


class Dashboard(BasePage):
    expected_title = "Scouts panel"
    dashboard_url = "https://scouts-test.futbolkolektyw.pl/"
    main_page_button_xpath = "//div[@class='MuiListItemText-root jss91 jss105']//child::span"
    players_button_xpath = "//div[@class='MuiListItemText-root jss91 jss106']//child::span"
    language_button_xpath = "//*//div/ul[2]/div[1]"
    sign_out_button_xpath = "//span[text()='Sign out']"
    scouts_panel_xpath = "//h6[starts-with(@class,'MuiTypography-root jss16')"
    image_futbol_xpath = "//div[@title='Logo Scouts Panel' and contains(@style,'image')]"
    text_under_image_xpath = "//p[starts-with(@class,'MuiTypography-root ')]"
    dev_team_button_xpath = "//a[contains(@class,'MuiButtonBase-root')]"
    add_player_button_xpath = "//*/div[2]/div/div/a/button/span[1]"
    activity_label_xpath = "//*/div[3]/div[3]/div/div/h2"
    last_created_player_button_xpath = "//*/div[3]/div/div/a[1]/button/span[1]"
    last_created_match_button_xpath = "//*/div/a[3]/button/span[1]"
    last_updated_match_button_xpath = "//*/div/div/a[4]/button/span[1]"
    last_updated_report_button_xpath = "//*/div/div/a[5]/button/span[1]"

    def click_on_the_add_a_player_button(self):
        self.click_on_the_element(self.add_player_button_xpath)

    def title_of_page(self):
        self.wait_for_element_to_be_clickable(self.add_player_button_xpath)
        assert self.get_page_title(self.dashboard_url) == self.expected_title

    def click_on_the_last_created_match_button(self):
        self.click_on_the_element(self.last_created_match_button_xpath)

    def click_on_the_sign_out_button(self):
        self.wait_for_element_to_be_clickable(self.sign_out_button_xpath)
        self.click_on_the_element(self.sign_out_button_xpath)

    def click_on_the_last_created_player_button(self):
        self.wait_for_element_to_be_clickable(self.last_created_player_button_xpath)
        self.click_on_the_element(self.last_created_player_button_xpath)