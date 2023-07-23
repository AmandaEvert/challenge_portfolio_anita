from pages.base_page import BasePage
import time


class AddPlayerChange(BasePage):
    email_field_xpath = "//*[@name='email']"
    name_field_xpath = "//*[@name='name']"
    surname_field_xpath = "//*[@name='surname']"
    age_field_xpath = "//*[@name='age']"
    submit_button_xpath = "//*/div[3]/button[1]/span[1]"
    add_a_player_button_xpath = "//*/div[2]/div/div/a/button/span[1]"
    main_position_field_xpath = "//*[@name='mainPosition']"
    add_a_player_url = "https://scouts-test.futbolkolektyw.pl/en/players/add"
    expected_title = "Add player"
    leg_dropdown_xpath = "//*[@id='mui-component-select-leg']"
    left_leg_dropdown_xpath = "//*[@data-value='left']"
    right_leg_dropdown_xpath = "//li[contains(@data-value, 'right')]"


    def select_leg(self, leg):
        self.click_on_the_element(self.leg_dropdown_xpath)
        self.wait_for_element_to_be_clickable(self.right_leg_dropdown_xpath)
        if leg == "Right leg":
            self.click_on_the_element(self.right_leg_dropdown_xpath)
        else:
            self.wait_for_visibility_of_element(self.left_leg_dropdown_xpath)
            self.click_on_the_element(self.left_leg_dropdown_xpath)
            self.wait_for_element_to_be_clickable(self.left_leg_dropdown_xpath)



