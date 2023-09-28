import time

from selenium.webdriver.common.by import By
from pages.create_account_page import CreateAccountPage


def test_incorrect_data(driver, create_account_page):
    create_account_page.open()
    create_account_page.fill_create_form(f_name='', l_name='', email='w@g.t', passw='123', c_passw='1234')
    assert create_account_page.error_f_name == 'This is a required field.'
    assert create_account_page.error_l_name == 'This is a required field.'
    assert create_account_page.error_email == 'Please enter a valid email address (Ex: johndoe@domain.com).'
    assert create_account_page.error_passw == ('Minimum length of this field must be equal or '
                                               'greater than 8 symbols. Leading and trailing spaces will be ignored.')
    assert create_account_page.error_c_passw == 'Please enter the same value again.'
