import time
from pages.locators import create_acc_page_locs as loc

class CreateAccountPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get('https://magento.softwaretestingboard.com/customer/account/create/')

    def fill_create_form(self, f_name, l_name, email, passw, c_passw):
        self.driver.find_element(*loc.firstname).send_keys(f_name)
        self.driver.find_element(*loc.lastname).send_keys(l_name)
        self.driver.find_element(*loc.e_mail).send_keys(email)
        self.driver.find_element(*loc.password).send_keys(passw)
        self.driver.find_element(*loc.c_password).send_keys(c_passw)
        time.sleep(1)
        self.driver.find_element(*loc.submit_button).click()

    @property
    def error_f_name(self):
        return self.driver.find_element(*loc.f_name_err).text

    @property
    def error_l_name(self):
        return self.driver.find_element(*loc.l_name_err).text

    @property
    def error_email(self):
        return self.driver.find_element(*loc.email_err).text

    @property
    def error_passw(self):
        return self.driver.find_element(*loc.passw_err).text

    @property
    def error_c_passw(self):
        return self.driver.find_element(*loc.c_passw_err).text


