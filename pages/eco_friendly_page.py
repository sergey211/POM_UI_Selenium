from pages.base_page import BasePage
from pages.locators import eco_friendly_page_locs as loc


class EcoFriendlyPage(BasePage):
    page_url = '/collections/eco-friendly.html'

    @property
    def page_title_text(self):
        return self.driver.find_element(*loc.page_title).text
