def test_sale_page_title(sale_page):
    sale_page.open()
    assert sale_page.page_title_text == 'Sale'
    sale_page.driver.close()
