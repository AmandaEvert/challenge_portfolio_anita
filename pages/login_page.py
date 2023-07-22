import time
from pages.base_page import BasePage

class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//span[starts-with(@class,'MuiButton-label')]"
    login_url = "https://scouts-test.futbolkolektyw.pl/en"
    expected_title = "Scouts panel - sign in"
    header_of_box_xpath = "//*/div/div[1]/h5"
    expected_header_of_the_box = 'Scouts Panel'
    error_message_xpath = "//*/div/div[1]/div[3]/span"
    expected_error_message = "Identifier or password invalid."
    language_dropdown_button_xpath = "//div[starts-with(@class,'MuiSelect-root MuiSelect')]"
    language_english_dropdown_xpath = "//li[contains(@data-value, 'en')]"
    language_polish_dropdown_xpath = "//li[contains(@data-value, 'pl')]"

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def click_on_the_sign_in_button(self):
        self.wait_for_element_to_be_clickable(self.sign_in_button_xpath)
        self.click_on_the_element(self.sign_in_button_xpath)

    def title_of_page(self):
        self.wait_for_element_to_be_clickable(self.sign_in_button_xpath)
        assert self.get_page_title(self.login_url) == self.expected_title

    def error_info_visible(self):
        self.assert_element_text(self.driver, self.error_message_xpath, self.expected_error_message)

    def verify_header(self):
        self.assert_element_text(self.driver, self.header_of_box_xpath, self.expected_header_of_the_box)

    def select_language(self, language):
        self.click_on_the_element(self.language_dropdown_button_xpath)
        time.sleep(1)
        if language == "english":
            self.click_on_the_element(self.language_english_dropdown_xpath)
        else:
            self.click_on_the_element(self.language_polish_dropdown_xpath)




