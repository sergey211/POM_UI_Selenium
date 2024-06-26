import time

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from pages.locators import eco_friendly_page_locs as loc


class BasePage:
    base_url = 'https://magento.softwaretestingboard.com'
    page_url = None

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open(self):
        if self.page_url:
            self.driver.get(f'{self.base_url}{self.page_url}')
        agree_button = self.driver.find_elements(*loc.agree_button)
        time.sleep(3)
        if len(agree_button) > 0:
            agree_button[0].click()
            print("window closed")
        else:
            raise NotImplementedError('This page cannot be opened by url')




    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_all(self, locator):
        return self.driver.find_elements(*locator)

    @staticmethod
    def find_in_elt(locator, elt: WebElement):
        return elt.find_element(*locator)

    @staticmethod
    def find_all_in_elt(locator, elt: WebElement):
        return elt.find_elements(*locator)

    def scroll_page(self, pixel=None):
        if pixel:
            self.driver.execute_script(f'window.scrollTo(0,{pixel});')
        else:
            self.driver.execute_script(f'window.scrollTo(0,document.body.scrollHeight);')
