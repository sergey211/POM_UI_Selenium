import random
import time

import allure
from allure_commons.types import AttachmentType
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from pages.locators import eco_friendly_page_locs as loc


class EcoFriendlyPage(BasePage):
    page_url = '/collections/eco-friendly.html'

    # i = None
    # j = None
    # k = None

    @property
    def page_title_text(self):
        return self.driver.find_element(*loc.page_title).text

    def close_modal(self):
        agree_button = self.driver.find_elements(*loc.agree_button)
        time.sleep(3)
        if len(agree_button) > 0:
            agree_button[0].click()
            print("window closed")

    def sort_by_price(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.text_to_be_present_in_element(loc.greeting, "Default welcome msg!"))
        select = Select(self.driver.find_element(*loc.sorter))
        first_link = self.driver.find_element(*loc.prod_item)
        select.select_by_visible_text('Price')
        sort_list = self.driver.find_elements(*loc.sort_list)
        print('length=', len(sort_list))
        sort_list[0].click()
        wait.until(EC.staleness_of(first_link))
        prices = self.driver.find_elements(*loc.prices)
        self.driver.execute_script("document.body.style.zoom='40%'")
        # self.driver.find_element(By.TAG_NAME, 'body').screenshot('c:/big_scr.png')
        allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        for x in range(0, len(prices) - 1):
            price_one = int(prices[x].text[1:3])
            price_two = int(prices[x + 1].text[1:3])
            print(price_one, '<=', price_two)
            assert price_one <= price_two, (f'Sort by ascending price Error: Price number {x + 1} = {price_one}'
                                            f'  is bigger then price number {x + 2} = {price_two}')

    def put_good_in_cart(self, size_color):
        i = size_color[0]
        j = size_color[1]
        k = size_color[2]
        all_sizes = self.driver.find_elements(*loc.sizes)
        first_sizes = all_sizes[i]
        # name_of_goods = self.driver.find_elements(*loc.good_name)
        # name_of_selected = name_of_goods[i].text
        one_size = first_sizes.find_elements(*loc.size)
        size = one_size[j]
        # size_text = size.get_attribute("option-label")
        all_colors = self.driver.find_elements(*loc.colors)
        first_colors = all_colors[i]
        one_color = first_colors.find_elements(*loc.color)
        color = one_color[k]
        # color_text = color.get_attribute("option-label")
        size.click()
        color.click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(loc.loader))
        # "product-image-photo"
        # pics = self.driver.find_elements(By.XPATH, "//img[@class='product-image-photo']")
        # wait.until(EC.ele element_to_be_clickable(pics[i]))
        self.driver.find_elements(*loc.add_to_cart)[i].click()
        wait.until(EC.element_to_be_clickable(loc.cart_counter))

    def check_color_of_good_to_buy(self, size_color):
        i = size_color[0]
        k = size_color[2]
        all_colors = self.driver.find_elements(*loc.colors)
        first_colors = all_colors[i]
        one_color = first_colors.find_elements(*loc.color)
        color = one_color[k]
        color_text = color.get_attribute("option-label")

        return color_text

    def check_size_of_good_to_buy(self, size_color):
        i = size_color[0]
        j = size_color[1]
        all_sizes = self.driver.find_elements(*loc.sizes)
        first_sizes = all_sizes[i]
        # name_of_goods = self.driver.find_elements(*loc.good_name)
        # name_of_selected = name_of_goods[i].text
        one_size = first_sizes.find_elements(*loc.size)
        size = one_size[j]
        size_text = size.get_attribute("option-label")
        return size_text

    def check_color_of_good_in_cart(self):
        self.driver.execute_script("window.scrollTo(0, 0)")
        cart_closed = self.driver.find_elements(*loc.cart_closed)
        if len(cart_closed) > 0:
            self.driver.find_element(loc.cart).click()
        size_visible = self.driver.find_elements(*loc.size_visible)
        if len(size_visible) == 0:
            self.driver.find_element(loc.cart_detailed).click()
        prod_details = self.driver.find_elements(*loc.prod_detailed)
        color_in_cart = prod_details[1].text
        print('color in cart = ', color_in_cart)
        return color_in_cart

    def check_size_of_good_in_cart(self):
        self.driver.execute_script("window.scrollTo(0, 0)")
        cart_closed = self.driver.find_elements(*loc.cart_closed)
        if len(cart_closed) > 0:
            cart = self.driver.find_element(*loc.cart)
            cart.click()
        size_visible = self.driver.find_elements(*loc.size_visible)
        if len(size_visible) == 0:
            self.driver.find_element(*loc.cart_detailed).click()
        prod_details = self.driver.find_elements(*loc.prod_detailed)
        size_in_cart = prod_details[0].text
        print('size in cart = ', size_in_cart)
        return size_in_cart
