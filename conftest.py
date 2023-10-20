import random
import string
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.create_account_page import CreateAccountPage
from pages.eco_friendly_page import EcoFriendlyPage
from pages.sale_page import SalePage
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--ignore-certificate-errors')
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-dev-shm-usage')


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome(chrome_options)
    #chrome_driver = webdriver.Chrome()
    # time.sleep(3)
    chrome_driver.implicitly_wait(7)
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


@pytest.fixture()
def fake_email(driver):
    return (random.choice(string.ascii_letters.lower())+'@'+random.choice(string.ascii_letters.lower()) +
            random.choice(string.ascii_letters.lower())+'.com')


# @pytest.fixture(scope="session")
@pytest.fixture()
def size_color(driver):
    driver.get('https://magento.softwaretestingboard.com/collections/eco-friendly.html')
    all_sizes = driver.find_elements(By.XPATH, "//*[@class = 'swatch-attribute size']")
    i = random.randint(0, len(all_sizes)-1)
    # if i == 0:
    #     i = 1
    name_of_goods = driver.find_elements(By.XPATH, "//a[@class='product-item-link']")
    name_of_selected = name_of_goods[i].text
    print('Name of good is ', name_of_selected)
    first_sizes = all_sizes[i]
    one_size = first_sizes.find_elements(By.CSS_SELECTOR, ".swatch-option")
    j = random.randint(0, len(one_size)-1)
    # if j == 0:
    #     j = 1
    # print("random number of size is ", j)
    size = one_size[j]
    size_text = size.get_attribute("option-label")
    print('and this size is = ', size_text)
    # self.driver.stop_client()
    all_colors = driver.find_elements(By.XPATH, "//*[@class = 'swatch-attribute color']")
    first_colors = all_colors[i]
    one_color = first_colors.find_elements(By.CSS_SELECTOR, ".swatch-option")
    # print('size of all colors is = ', len(all_colors))
    # print('size of one color is = ', len(one_color))
    k = random.randint(0, len(one_color)-1)
    # if k == 0:
    #     k = 1
    color_text = one_color[k].get_attribute("option-label")
    print('and this color is = ', color_text)
    randoms = (i, j, k)
    return randoms

