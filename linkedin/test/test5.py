
# Gerekli olan kütüphanelerin içeri aktarılması
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class AddItemToCart(unittest.TestCase):
    # Ziyaret edeceği sitenin URL'si
    base_url = "https://www.amazon.in"

    # Aranacak ürün
    search_term = "WD My Passport 4TB"

    def setUp(self):
        # Chrome'u kullanmak için sürücüyü bağlıyorum 
        self.driver = webdriver.Chrome(
            executable_path="/Users/furkangulsen/projects/chromedriver")
        # Tarayıcı büyütülmüş pencerede yüklenmelidir
        self.driver.maximize_window()
        # Sunucunun yüklenmesi için belirli bir süre bekliyorum
        self.driver.implicitly_wait(10)  # 10 saniye kadar


    def test_add_item_to_cart(self):
        # Belirlediğim URL sitesine gidiyorum
        self.driver.get(self.base_url)
        # Arama input alanını seçiyorum
        searchTextBox = self.driver.find_element_by_id("twotabsearchtextbox")
        # Arama input alanını temizliyorum
        searchTextBox.clear()
        # Belirlediğim arama metninin arama input alanına yazıyorum
        searchTextBox.send_keys(self.search_term)
        # Aramaya başlıyorum
        searchTextBox.send_keys(Keys.RETURN)
        # Çıkan ilk ürüne tıklıyorum
        self.driver.find_element_by_xpath(
            "(//div[@class='sg-col-inner']//img[contains(@data-image-latency,'s-product-image')])[2]").click()
        # Aranan ürün yeni bir sekmede açıldığı için o sekemeye geçiş yapıyorum
        self.driver.switch_to.window(self.driver.window_handles[1])
        # ürünün üzerinde ki sepete ekle butonuna basarak sepete ekliyorum
        self.driver.find_element_by_id("add-to-cart-button").click()
        self.assertTrue(self.driver.find_element_by_id(
            "hlb-subcart").is_enabled())
        # ürünün sepete başarıyla eklendiğini doğruluyorum
        self.assertTrue(self.driver.find_element_by_id(
            "hlb-ptc-btn-native").is_displayed())

    def tearDown(self):
        # çıkış yapıyorum
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()