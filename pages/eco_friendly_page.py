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

    @property
    def page_title_text(self):
        return self.driver.find_element(*loc.page_title).text

    def sort_by_price(self):
        time.sleep(3)  # КАК ИЗБАВИТЬСЯ ОТ ЭТОГО ОЖИДАНИЯ?? ВСЕ МЕТОДЫ СНИЗУ НЕ ПОМОГАЮТ - PRICE меняется на POSITION
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.driver.find_element(By.XPATH, "//div[contains(text(),'Climate')]")))
        wait.until(EC.element_to_be_clickable(self.driver.find_element(By.ID, 'sorter')))
        wait.until(lambda driver: self.driver.execute_script('return document.readyState') == 'complete')
        select = Select(self.driver.find_element(By.ID, 'sorter'))
        # price_sel = self.driver.find_elements(By.XPATH, "//select/option[@value='price']")
        # wait.until(EC.element_located_to_be_selected(price_sel[0]))
        # wait.until(EC.element_to_be_clickable(price_sel[0]))
        # price_sel[0].click()
        select.select_by_visible_text('Price')

        # price_sel[0].click()
        # wait.until(EC.element_located_to_be_selected())
        # select.select_by_visible_text('Price')
        time.sleep(5)  # c этим ожиданием разберемся после первого
        sort_list = self.driver.find_elements(By.XPATH, "//a[@title='List']")
        print('length=', len(sort_list))
        sort_list[0].click()
        prices = self.driver.find_elements(By.XPATH, "//span/span[@class='price']")

        self.driver.execute_script("document.body.style.zoom='40%'")
        self.driver.find_element(By.TAG_NAME, 'body').screenshot('c:/big_scr.png')
        allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        for x in range(0, len(prices) - 1):
            price_one = int(prices[x].text[1:3])
            price_two = int(prices[x + 1].text[1:3])
            print(price_one, '<=', price_two)
            assert price_one <= price_two, (f'Sort by ascending price Error: Price number {x + 1} = {price_one}'
                                            f'  is bigger then price number {x + 2} = {price_two}')

    def buy_orange_pants(self):
        size = self.driver.find_element(By.XPATH, "//div[@id='option-label-size-143-item-177']")
        color = self.driver.find_element(By.XPATH,
                                         "//div[@class='swatch-opt-802']//div[@id='option-label-color-93-item-56']")
        # size_text = size.get_attribute("option-label")
        # color_text = color.get_attribute("option-label")
        size.click()
        color.click()
        self.driver.find_element(By.XPATH,
                                 "//li[10]//div[1]//div[1]//div[3]//div[1]//div[1]//form[1]//button[1]//span[1]"
                                 ).click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='counter-number' and contains(text(), '1')]")))

    def check_color_of_good_to_buy(self):
        color = self.driver.find_element(By.XPATH,
                                         "//div[@class='swatch-opt-802']//div[@id='option-label-color-93-item-56']")
        action = ActionChains(self.driver)
        action.move_to_element(color)
        color_text = color.get_attribute("option-label")
        return color_text

    def check_size_of_good_to_buy(self):
        size = self.driver.find_element(By.XPATH, "//div[@id='option-label-size-143-item-177']")
        action = ActionChains(self.driver)
        action.move_to_element(size)
        size_text = size.get_attribute("option-label")
        return size_text

    def check_color_of_good_in_cart(self):
        self.driver.execute_script("window.scrollTo(0, 0)")
        self.driver.find_element(By.CSS_SELECTOR, ".action.showcart").click()
        prod_details = self.driver.find_elements(By.XPATH, "//dl[normalize-space()]/dd")
        color_in_cart = prod_details[1].text
        if color_in_cart == '':
            print("Color not displayed")
            try:
                self.driver.find_element(By.CSS_SELECTOR, "span[role='tab']").click()
            except:
                print("Cart is closed")
                self.driver.find_element(By.CSS_SELECTOR, ".action.showcart").click()
                prod_details = self.driver.find_elements(By.XPATH, "//dl[normalize-space()]/dd")
                color_in_cart = prod_details[1].text
            prod_details = self.driver.find_elements(By.XPATH, "//dl[normalize-space()]/dd")
            color_in_cart = prod_details[1].text
        return color_in_cart

    def check_size_of_good_in_cart(self):
        self.driver.execute_script("window.scrollTo(0, 0)")
        self.driver.find_element(By.CSS_SELECTOR, ".action.showcart").click()
        # time.sleep(0)
        prod_details = self.driver.find_elements(By.XPATH, "//dl[normalize-space()]/dd")
        size_in_cart = prod_details[0].text
        if size_in_cart == '':
            print("Size not displayed")
            try:
                self.driver.find_element(By.CSS_SELECTOR, "span[role='tab']").click()
            except:
                print("Cart is closed")
                self.driver.find_element(By.CSS_SELECTOR, ".action.showcart").click()
                # time.sleep(0)
                prod_details = self.driver.find_elements(By.XPATH, "//dl[normalize-space()]/dd")
                size_in_cart = prod_details[0].text
            # time.sleep(0)
            prod_details = self.driver.find_elements(By.XPATH, "//dl[normalize-space()]/dd")
            size_in_cart = prod_details[0].text
        return size_in_cart
