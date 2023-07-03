from pages.base_page import BasePage


class Dashboard(BasePage)
main_page_button_xpath = "//div[@class='MuiListItemText-root jss91 jss105']//child::span"
players_button_xpath = "//div[@class='MuiListItemText-root jss91 jss106']//child::span"
language_button_xpath = "//span[text()='Polski']"
sign_out_button_xpath = "//span[text()='Sign out']"
scouts_panel-xpath = "//h6[starts-with(@class,'MuiTypography-root jss16')"
image_futbol_xpath ="//div[@title='Logo Scouts Panel' and contains(@style,'image')]"
text_under_image_xpath = "//p[starts-with(@class,'MuiTypography-root ')]"
dev_team_button_xpath = "//a[contains(@class,'MuiButtonBase-root')]"
add_player_button_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[2]/div/div/a/button/span[1]"
activity_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/h2"
last created player_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/a[1]/button/span[1]"
last created match_xpath ="//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/a[3]/button/span[1]"
last updated match_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/a[4]/button/span[1]"
last updated report_xpath ="//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/a[5]/button/span[1]"
pass