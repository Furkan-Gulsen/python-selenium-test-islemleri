import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time


email = "hilal.coskun20@gmail.com"
password =123456789321
#aranacak ürün
product = "pembe lilyum çiçek buketi"



class Buy:
    s = Service('directory/chromedriver.exe')
    browser = webdriver.Chrome(service=s)
    browser.maximize_window()
    url = 'https://www.ciceksepeti.com'
    browser.get(url)

    def sign(self):
        self.browser.get("https://www.ciceksepeti.com/uye-girisi")
        time.sleep(1)
        userName = self.browser.find_element_by_name("Email")
        userName.send_keys(email)
        time.sleep(2)
        userPassword = self.browser.find_element_by_id("Password")
        userPassword.send_keys(password)
        time.sleep(2)
        userPassword.send_keys(Keys.ENTER)
        time.sleep(1)

    def addFavorites(self):
        self.browser.find_element_by_class_name("icon-favorite").click()
        time.sleep(1)
        self.browser.find_element_by_class_name("user-menu__icon--favorite").click()
        time.sleep(3)
        self.browser.close()


    def searchProduct(self):
        search = self.browser.find_element_by_class_name("product-search__input")
        search.send_keys(product)
        self.browser.find_element_by_class_name("icon-search-444").click()
        time.sleep(2)
        self.browser.find_element_by_xpath("/html/body/main/div/div[4]/div[4]/div/div/a/div[1]/img").click()
        time.sleep(2)

    def addToCart(self):
        self.browser.find_element_by_class_name("js-emoji-characters").click()
        time.sleep(1)
        self.browser.find_element_by_class_name("js-region-self-service").click()
        time.sleep(2)
        self.browser.find_element_by_xpath("//*[@id='productDetailSend']/div/div/div[2]/div[2]/div[4]/div[5]/div[1]/div[1]/span[1]").click()
        time.sleep(2)
        self.browser.find_element_by_xpath("//*[@id='productDetailSend']/div/div/div[2]/div[2]/div[4]/div[13]/div/div/div/div[1]/input").click()
        time.sleep(2)
        self.browser.find_element_by_xpath("//*[@id='productDetailSend']/div/div/div[2]/div[2]/div[4]/div[13]/div/div/div/div[2]/div/div[1]/p").click()
        time.sleep(2)
        self.browser.find_element_by_class_name("js-add-to-cart").click()
        time.sleep(2)
        self.browser.find_element_by_class_name("order-back-button").click()
        time.sleep(3)
        self.browser.find_element_by_class_name("user-menu__icon--cart").click()
        time.sleep(3)
        self.browser.close()


if __name__ == '__main__':
    Buy = Buy()
    Buy.sign()
    Buy.searchProduct()
    Buy.addToCart()
    """  
    Buy.addFavorites()
    """












