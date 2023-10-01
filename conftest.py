import time

import pytest
from selenium import webdriver
from pages.create_account_page import CreateAccountPage
from pages.eco_friendly_page import EcoFriendlyPage
from pages.sale_page import SalePage
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-dev-shm-usage')


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome(chrome_options)
    # chrome_driver = webdriver.Chrome()
    # time.sleep(3)
    chrome_driver.implicitly_wait(5)
    return chrome_driver


@pytest.fixture()
def create_account_page(driver):
    return CreateAccountPage(driver)


@pytest.fixture()
def eco_friendly_page(driver):
    return EcoFriendlyPage(driver)


@pytest.fixture()
def sale_page(driver):
    return SalePage(driver)

