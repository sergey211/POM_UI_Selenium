def test_eco_friendly_title(eco_friendly_page):
    eco_friendly_page.open()
    assert eco_friendly_page.page_title_text == 'Eco Friendly'
