from selenium.webdriver.common.by import By

page_title = (By.CSS_SELECTOR, '.page-title-wrapper')
sorter = (By.ID, 'sorter')
greeting = (By.TAG_NAME, 'body')
prod_item = (By.CLASS_NAME, 'product-item-link')
sort_list = (By.XPATH, "//a[@title='List']")
prices = (By.XPATH, "//span/span[@class='price']")
sizes = (By.XPATH, "//*[@class = 'swatch-attribute size']")
good_name = (By.XPATH, "//a[@class='product-item-link']")
size = (By.CSS_SELECTOR, ".swatch-option")
colors = (By.XPATH, "//*[@class = 'swatch-attribute color']")
color = (By.CSS_SELECTOR, ".swatch-option")
add_to_cart = (By.XPATH, "//span[text()='Add to Cart']")
cart_counter = (By.XPATH, "//span[@class='counter-number' and contains(text(), '1')]")
loader = (By.XPATH,  "//img[@class='product-image-photo swatch-option-loading']")
cart_opened = (By.XPATH, '//div[@class="ui-dialog ui-widget ui-widget-content ui-corner-all ui-front '
                         'mage-dropdown-dialog" and @style="display: block;"]')
cart_closed = (By.XPATH, '//div[@class="ui-dialog ui-widget ui-widget-content ui-corner-all ui-front '
                         'mage-dropdown-dialog" and @style="display: none;"]')
cart = (By.XPATH, "//*[@class='action showcart']")
size_visible = (By.XPATH, "//*[@data-role='content' and @aria-hidden='false']//*[text()='Size']")
cart_detailed = (By.CSS_SELECTOR, "span[role='tab']")
prod_detailed = (By.XPATH, "//dl[normalize-space()]/dd")