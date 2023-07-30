from pages.base_page import BasePage

class LoginPageChangeLanguage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//span[starts-with(@class,'MuiButton-label')]"
    login_url = "https://dareit.futbolkolektyw.pl/login"
    expected_title = "Scouts panel - sign in"
    header_of_box_xpath = "//*/div/div[1]/h5"
    expected_header_of_the_box = 'Scouts Panel'
    error_message_xpath = "//*/div/div[1]/div[3]/span"
    expected_error_message = "Identifier or password invalid."
    language_dropdown_button_xpath = "//div[starts-with(@class,'MuiSelect-root MuiSelect')]"
    language_english_dropdown_xpath = "//li[contains(@data-value, 'en')]"
    language_polish_dropdown_xpath = "//li[contains(@data-value, 'pl')]"

    def select_language(self, language):
        self.click_on_the_element(self.language_dropdown_button_xpath)
        self.wait_for_visibility_of_element(self.language_english_dropdown_xpath)
        if language == "english":
            self.wait_for_element_to_be_clickable(self.language_english_dropdown_xpath)
            self.click_on_the_element(self.language_english_dropdown_xpath)
        else:
            self.wait_for_element_to_be_clickable(self.language_polish_dropdown_xpath)
            self.click_on_the_element(self.language_polish_dropdown_xpath)
            self.wait_for_element_to_be_clickable(self.language_dropdown_button_xpath)




