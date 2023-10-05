from selenium.webdriver.common.by import By

firstname = (By.ID, 'firstname')
lastname = (By.ID, 'lastname')
e_mail = (By.ID, 'email_address')
password = (By.ID, 'password')
c_password = (By.ID, 'password-confirmation')
submit_button = (By.XPATH, "//*[@title='Create an Account']")
f_name_err = (By.ID, 'firstname-error')
l_name_err = (By.ID, 'lastname-error')
email_err = (By.ID, 'email_address-error')
passw_err = (By.ID, 'password-error')
c_passw_err = (By.ID, 'password-confirmation-error')
reg_info_mes = (By.XPATH, "//*[starts-with(@data-bind,'html: $parent')]")
menu_btn = (By.XPATH, "//button[@class='action switch']")
logout_btn = (By.XPATH,
              ("//li[@class='customer-welcome active']/div/ul[@class='header links']/li[@class="
               "'authorization-link']/a[contains(text(),'Sign Out')]"))
