import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest, time, re
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

email = "hilal.coskun20@gmail.com"
#password =
#aranacak ürün
product = "pembe lilyum çiçek buketi"




class CicekSepeti(unittest.TestCase):

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


    def searchProduct(self):
        search = self.browser.find_element(By.CLASS_NAME,"product-search__input")
        search.send_keys(product)
        self.browser.find_element(By.CLASS_NAME, "icon-search-444").click()
        time.sleep(2)
        self.browser.find_element(By.XPATH, "/html/body/main/div/div[4]/div[4]/div/div/a/div[1]/img").click()
        name = self.browser.find_element(By.XPATH, "//*[@id='productDetailSend']/div/div/div[2]/div[2]/div[2]/div/div[1]/h1/span").text.strip()
        self.assertEqual("Pembe Lilyum Çiçek Buketi", name)
        print("success")
        time.sleep(2)

    def addToCart(self):
        self.browser.find_element(By.CLASS_NAME, "js-emoji-characters").click()
        time.sleep(1)
        self.browser.find_element(By.CLASS_NAME, "js-region-self-service").click()
        time.sleep(2)
        self.browser.find_element(By.XPATH, "//*[@id='productDetailSend']/div/div/div[2]/div[2]/div[4]/div[5]/div[2]/div[1]/span[1]").click()
        time.sleep(2)
        self.browser.find_element(By.XPATH, "//*[@id='productDetailSend']/div/div/div[2]/div[2]/div[4]/div[13]/div/div/div/div[1]/input").click()
        time.sleep(2)
        self.browser.find_element(By.XPATH, "//*[@id='productDetailSend']/div/div/div[2]/div[2]/div[4]/div[13]/div/div/div/div[2]/div/div[1]/p").click()
        time.sleep(2)

        self.browser.find_element(By.CLASS_NAME, "js-add-to-cart").click()
        time.sleep(2)

    def returnAddToCart(self):
        self.browser.back()
        self.browser.find_element(By.CLASS_NAME, "js-emoji-characters").click()
        time.sleep(1)
        self.browser.find_element(By.CLASS_NAME, "js-region-self-service").click()
        time.sleep(2)
        productPrice = self.browser.find_element(By.CLASS_NAME, "js-price-integer").text
        print("price: ", productPrice)

        #ürün fiyatı string den int türüne çevrilir
        intPrice = int(productPrice)

        #sepete eklenecek aynı iki ürünün toplam fiyatı
        tekliurunikiuruncarpimi = intPrice*2

        print("sepete eklenecek aynı iki ürünün toplam fiyatı", tekliurunikiuruncarpimi)

        #sepete eklencek iki ürünün toplam fiyatının string e çevrilir
        stringtekliurunikiuruncarpimi = str(tekliurunikiuruncarpimi)

        self.browser.find_element(By.XPATH, "//*[@id='productDetailSend']/div/div/div[2]/div[2]/div[4]/div[5]/div[2]/div[1]/span[1]").click()
        time.sleep(2)
        self.browser.find_element(By.XPATH, "//*[@id='productDetailSend']/div/div/div[2]/div[2]/div[4]/div[13]/div/div/div/div[1]/input").click()
        time.sleep(2)
        self.browser.find_element(By.XPATH, "//*[@id='productDetailSend']/div/div/div[2]/div[2]/div[4]/div[13]/div/div/div/div[2]/div/div[1]/p").click()
        time.sleep(2)
        self.browser.find_element(By.CLASS_NAME, "js-add-to-cart").click()
        time.sleep(3)
        self.browser.find_element(By.CLASS_NAME, "agree-button").click()
        time.sleep(2)

        #sepetteki toplam fiyat
        totalPrice = self.browser.find_element(By.CLASS_NAME, "grand-total-integer").text
        print("total price", totalPrice)
        #sepetteki toplam fiyatın string e çevrilir
        strtotalPrice = str(totalPrice)

        time.sleep(2)
        self.assertEqual(stringtekliurunikiuruncarpimi, strtotalPrice)
        print("price successed")





if __name__ == '__main__':
    CicekSepeti = CicekSepeti()
    CicekSepeti.sign()
    CicekSepeti.searchProduct()
    CicekSepeti.addToCart()
    CicekSepeti.returnAddToCart()


