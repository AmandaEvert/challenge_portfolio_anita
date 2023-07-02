# Zadanie 1 #
## **Podzadanie 1: Konfiguracja oprogramowania.** ##
## **Podzadanie 2: Dlaczego zdecydowałem się wziąć udział w wyzwaniu Dare IT Challenge?** ##
Zdecydowałam się wziąć udział w wyzwaniu, ponieważ chciałabym sprawdzić czy nadaję się do automatycznego testowania oprogramowania. Jest to dla mnie coś zupełnie nowego (z wykształcenia jestem prawnikiem), więc będzie to dla mnie spore wyzwanie. Mam nadzieję, że ogarnę.  😊
## Wynik ##
9
# ZADANIE 2: selektory #
## scouts_panel_xpath ##
//*[@id="__next"]/form/div/div[1]/h5
//*[contains(@ class, "MuiTypography-root MuiTypography-h5")]
//*[text()="Scouts Panel"]
## login_xpath ##
//*[@id="login"]
//input[@type="text"]
//input[starts-with(@name,'login')]
## password_xpath ##
//*[@id="password"]
/html/body/div[1]/form/div/div[1]/div[2]/div/input
//input[@type="password"]
## please_provide_your_username_or_your_e-mail_xpath ##
//*[@id="__next"]/form/div/div[1]/div[3]/span
//*[contains(@class, "MuiTypography-root MuiTypography-caption")]
//span[text()="Please provide your username or your e-mail."]
## remind_password_xpath ##
//*[@id="__next"]/form/div/div[1]/a
//*[contains(@class, "MuiTypography-root MuiLink")]
//*[text()="Remind password"]
## language_xpath ##
//*[@id="__next"]/form/div/div[2]/div/div
//div[starts-with(@class,"MuiSelect-root MuiSelect-select")]
//div[@role="button" and contains(@class,'MuiSelect')]
## sign_in_xpath ##
//*[@id="__next"]/form/div/div[2]/button/span[1]
//span[starts-with(@class,'MuiButton-label')]
 //span[contains(@class,'MuiButton-label')] 
 
