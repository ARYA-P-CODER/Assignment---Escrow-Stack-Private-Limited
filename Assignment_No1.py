from selenium.webdriver.chrome.webdriver import WebDriver
from time import sleep

driver = WebDriver()
driver.implicitly_wait(15)
driver.maximize_window()
driver.get("https://www.amazon.in/")

parent_handle = driver.current_window_handle

search_textfeild = driver.find_element("id","twotabsearchtextbox")
search_textfeild.send_keys("Wrist Watches")

search_icon = driver.find_element("id","nav-search-submit-button")
search_icon.click()

leather_checkbox = driver.find_element("xpath","//span[text()='Leather']")
leather_checkbox.click()

fastrack_checkbox = driver.find_element("xpath","//span[text()='Brands']/../..//span[text()='Fastrack']")
fastrack_checkbox.click()

second_page_link = driver.find_element("css selector", "a[aria-label='Go to page 2']")
second_page_link.click()

first_product_img = driver.find_element("xpath", "//span[@data-component-id='5']/div[1]/div[2]//img")
first_product_img.click()

all_handles = driver.window_handles
for handle in all_handles:
    if handle != parent_handle:
        child_handle = handle

driver.switch_to.window(child_handle)

add_to_cart_btn = driver.find_element("id", "add-to-cart-button")
add_to_cart_btn.click()
