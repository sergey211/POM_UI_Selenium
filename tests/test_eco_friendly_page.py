from selenium.webdriver.support.select import Select

# from conftest import ijk


def test_eco_friendly_title(eco_friendly_page):
    eco_friendly_page.open()
    assert eco_friendly_page.page_title_text == 'Eco Friendly'


def test_sort_by_price(eco_friendly_page):
    eco_friendly_page.open()
    eco_friendly_page.sort_by_price()


def test_put_in_cart_random_good(eco_friendly_page, size_color):
    eco_friendly_page.open()
    eco_friendly_page.put_good_in_cart(size_color)
    assert eco_friendly_page.check_size_of_good_to_buy(size_color) == eco_friendly_page.check_size_of_good_in_cart()
    assert eco_friendly_page.check_color_of_good_to_buy(size_color) == eco_friendly_page.check_color_of_good_in_cart()

