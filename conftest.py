import time

import pytest
from selenium import webdriver
from pages.create_account_page import CreateAccountPage
from pages.eco_friendly_page import EcoFriendlyPage
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)


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

