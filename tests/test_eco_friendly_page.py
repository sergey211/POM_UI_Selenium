from selenium.webdriver.support.select import Select


def test_eco_friendly_title(eco_friendly_page):
    eco_friendly_page.open()
    assert eco_friendly_page.page_title_text == 'Eco Friendly'


def test_sort_by_price(eco_friendly_page):
    eco_friendly_page.open()
    eco_friendly_page.sort_by_price()


def test_put_in_cart_orange_pants(eco_friendly_page):
    eco_friendly_page.open()
    eco_friendly_page.buy_orange_pants()
    assert eco_friendly_page.check_size_of_good_to_buy() == eco_friendly_page.check_size_of_good_in_cart()
    assert eco_friendly_page.check_color_of_good_to_buy() == eco_friendly_page.check_color_of_good_in_cart()

