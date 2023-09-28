from pages.base_page import BasePage
from pages.locators import sale_page_locs as loc


class SalePage(BasePage):
    page_url = '/sale.html'

    @property
    def page_title_text(self):
        return self.driver.find_element(*loc.page_title).text
