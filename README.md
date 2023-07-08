# Zadanie 1 #
## **Podzadanie 1: Konfiguracja oprogramowania.** ##
## **Podzadanie 2: Dlaczego zdecydowałem się wziąć udział w wyzwaniu Dare IT Challenge?** ##
Zdecydowałam się wziąć udział w wyzwaniu, ponieważ chciałabym sprawdzić czy nadaję się do automatycznego testowania oprogramowania. Jest to dla mnie coś zupełnie nowego (z wykształcenia jestem prawnikiem), więc będzie to dla mnie spore wyzwanie. Mam nadzieję, że ogarnę.  😊
## Wynik ##
9
# ZADANIE 2: selektory #
## scouts_panel_xpath ##
1. //*[@id="__next"]/form/div/div[1]/h5
2. //*[contains(@ class, "MuiTypography-root MuiTypography-h5")]
3. //*[text()="Scouts Panel"]
## login_xpath ##
1. //*[@id="login"]
2. //input[@type="text"]
3. //input[starts-with(@name,'login')]
## password_xpath ##
1. //*[@id="password"]
2. /html/body/div[1]/form/div/div[1]/div[2]/div/input
3. //input[@type="password"]
## please_provide_your_username_xpath ##
1. //*[@id="__next"]/form/div/div[1]/div[3]/span
2. //*[contains(@class, "MuiTypography-root MuiTypography-caption")]
3. //span[text()="Please provide your username or your e-mail."]
## remind_password_xpath ##
1. //*[@id="__next"]/form/div/div[1]/a
2. //*[contains(@class, "MuiTypography-root MuiLink")]
3. //*[text()="Remind password"]
## language_xpath ##
1. //*[@id="__next"]/form/div/div[2]/div/div
2. //div[starts-with(@class,"MuiSelect-root MuiSelect-select")]
3. //div[@role="button" and contains(@class,'MuiSelect')]
## sign_in_xpath ##
1. //*[@id="__next"]/form/div/div[2]/button/span[1]
2. //span[starts-with(@class,'MuiButton-label')]
3. //span[contains(@class,'MuiButton-label')] 
## language_select_button_xpath ##
//div[@role='button' and contains(@class,'MuiSelect')]
## language_select_english_xpath ##
//li[@role='option' and contains(@data-value,'en')]
## language_select_polski_xpath ##
//li[@role='option' and contains(@data-value,'pl')]
## login_label_xpath ##
 //label[@for='login' and contains(@class,'MuiFormLabel-root')]
## password_label_xpath ##
//label[@for='password' and contains(@class,'MuiFormLabel-root')]
