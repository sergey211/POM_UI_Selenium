import time
from pages.locators import create_acc_page_locs as loc
from pages.base_page import BasePage


class CreateAccountPage(BasePage):
    page_url = '/customer/account/create/'

    def fill_create_form(self, f_name, l_name, email, passw, c_passw):
        self.find(loc.firstname).send_keys(f_name)
        self.find(loc.lastname).send_keys(l_name)
        self.find(loc.e_mail).send_keys(email)
        self.find(loc.password).send_keys(passw)
        self.find(loc.c_password).send_keys(c_passw)
        time.sleep(1)
        self.find(loc.submit_button).click()

    @property
    def error_f_name(self):
        return self.find(loc.f_name_err).text

    @property
    def error_l_name(self):
        return self.find(loc.l_name_err).text

    @property
    def error_email(self):
        return self.find(loc.email_err).text

    @property
    def error_passw(self):
        return self.find(loc.passw_err).text

    @property
    def error_c_passw(self):
        return self.find(loc.c_passw_err).text


