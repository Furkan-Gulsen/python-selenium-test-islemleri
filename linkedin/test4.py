# bnk
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class AddItemToCart(unittest.TestCase): 
    # declare variable to store the URL to be visited
    base_url = "https://www.amazon.in"

    # declare variable to store search term
    search_term = "WD My Passport 4TB"

    # --- Pre - Condition ---
    def setUp(self):
        # declare and initialize driver variable
        self.driver = webdriver.Chrome(
            executable_path="/Users/furkangulsen/projects/chromedriver")
        # browser should be loaded in maximized window
        self.driver.maximize_window()
        # driver should wait implicitly for a given duration, for the element under consideration to load.
        # to enforce this setting we will use builtin implicitly_wait() function of our 'driver' object.
        self.driver.implicitly_wait(10)  # 10 is in seconds

    # --- Steps ---
    def test_add_item_to_cart(self):
        # to load a given URL in browser window
        self.driver.get(self.base_url)
        # to enter search term, we need to locate the search textbox
        searchTextBox = self.driver.find_element_by_id("twotabsearchtextbox")
        # to clear any text in the search textbox
        searchTextBox.clear()
        # to enter the search term in the search textbox via send_keys() function
        searchTextBox.send_keys(self.search_term)
        # to search for the entered search term
        searchTextBox.send_keys(Keys.RETURN)
        # to click on the first search result's link
        self.driver.find_element_by_xpath(
            "(//div[@class='sg-col-inner']//img[contains(@data-image-latency,'s-product-image')])[2]").click()
        # since the clicked product opens in a new tab, we need to switch to that tab.
        # to do so we will use window_handles()
        self.driver.switch_to.window(self.driver.window_handles[1])
        # to add the product to cart by clicking the add to cart button
        self.driver.find_element_by_id("add-to-cart-button").click()
        # to verify that sub cart page has loaded
        self.assertTrue(self.driver.find_element_by_id(
            "hlb-subcart").is_enabled())
        # to verify that the product was added to the cart successfully
        self.assertTrue(self.driver.find_element_by_id(
            "hlb-ptc-btn-native").is_displayed())

    # --- post - condition ---
    def tearDown(self):
        # to close the browser
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()