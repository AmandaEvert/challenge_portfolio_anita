from pages.base_page import BasePage

class EditPlayer(BasePage):
    matches_button_xpath = "//*/ul[2]/div[2]/div[2]/span"
    add_match_button_xpath = "//*/main/a/button/span[1]"

    def click_on_the_matches_button(self):
        self.wait_for_element_to_be_clickable(self.matches_button_xpath)
        self.click_on_the_element(self.matches_button_xpath)

    def click_on_the_add_match_button_xpath(self):
        self.wait_for_element_to_be_clickable(self.add_match_button_xpath)
        self.click_on_the_element(self.add_match_button_xpath)
