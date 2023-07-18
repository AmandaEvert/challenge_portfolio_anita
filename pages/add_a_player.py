from pages.base_page import BasePage
import time


class AddPlayer(BasePage):
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

    def type_in_email(self, email):
        self.field_send_keys(self.email_field_xpath, email)

    def type_in_name(self, name):
        self.field_send_keys(self.name_field_xpath, name)

    def type_in_surname(self, surname):
        self.field_send_keys(self.surname_field_xpath, surname)

    def type_in_main_position(self, main_position):
        self.field_send_keys(self.main_position_field_xpath, main_position)

    def type_in_age(self, age):
        self.field_send_keys(self.age_field_xpath, age)

    def click_on_the_submit_button(self):
        self.click_on_the_element(self.submit_button_xpath)

    def title_of_page(self):
        time.sleep(4)
        assert self.get_page_title(self.add_a_player_url) == self.expected_title

    def click_on_leg_dropdown(self):
        self.wait_for_element_to_be_clickable(self.leg_dropdown_xpath)
        self.click_on_the_element(self.leg_dropdown_xpath)

    def click_on_left_leg_dropdown(self):
        self.wait_for_element_to_be_clickable(self.left_leg_dropdown_xpath)
        self.click_on_the_element(self.left_leg_dropdown_xpath)

    def select_leg(self, leg):
        self.click_on_the_element(self.leg_dropdown_xpath)
        time.sleep(1)
        if leg == "Right leg":
            self.click_on_the_element(self.right_leg_dropdown_xpath)
        else:
            self.click_on_the_element(self.left_leg_dropdown_xpath)


