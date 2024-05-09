import time


def test_incorrect_data(create_account_page):
    create_account_page.open()
    create_account_page.fill_create_form(f_name='', l_name='', email='w@g.t', passw='123', c_passw='1234')
    assert create_account_page.error_f_name == 'This is a required field.'
    assert create_account_page.error_l_name == 'This is a required field.'
    assert create_account_page.error_email == 'Please enter a valid email address (Ex: johndoe@domain.com).'
    assert create_account_page.error_passw == ('Minimum length of this field must be equal or '
                                               'greater than 8 symbols. Leading and trailing spaces will be ignored.')
    assert create_account_page.error_c_passw == 'Please enter the same value again.'


def test_correct_data(create_account_page, fake_email):
    create_account_page.open()
    create_account_page.fill_create_form(f_name='Greg', l_name='Gromov', email=fake_email, passw='!QYUqw749',
                                         c_passw='!QYUqw749')
    assert create_account_page.reg_info == 'Thank you for registering with Main Website Store.'
    create_account_page.driver.close()

def test_registered_email(create_account_page, fake_email):
    create_account_page.open()
    create_account_page.fill_create_form(f_name='Greg', l_name='Gromov', email=fake_email, passw='!QYUqw749',
                                         c_passw='!QYUqw749')
    create_account_page.logout()
    create_account_page.open()
    create_account_page.fill_create_form('Greg', 'Gromov', fake_email, '!QYUqw749', '!QYUqw749')
    time.sleep(1)
    assert create_account_page.reg_info == ('There is already an account with this email address. '
                                            'If you are sure that it is your email address, click here to get your '
                                            'password and access your account.')
    create_account_page.driver.close()