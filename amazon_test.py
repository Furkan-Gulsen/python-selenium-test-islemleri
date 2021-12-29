
# Gerekli olan kütüphanelerin içeri aktarılması
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class AddItemToCart(unittest.TestCase):
    # Ziyaret edeceği sitenin URL'si
    base_url = "https://www.amazon.in"

    # Aranacak ürün
    search_term = "WD My Passport 4TB"

    def setUp(self):
        # Chrome'u kullanmak için sürücüyü bağlıyorum 
        self.service = Service('directory/chromedriver')
        self.driver = webdriver.Chrome(service=self.service)
        # Tarayıcı büyütülmüş pencerede yüklenmelidir
        self.driver.maximize_window()
        # Sunucunun yüklenmesi için belirli bir süre bekliyorum
        self.driver.implicitly_wait(10)  # 10 saniye kadar


    def test_add_item_to_cart(self):
        # Belirlediğim URL sitesine gidiyorum
        self.driver.get(self.base_url)
        # Arama input alanını seçiyorum
        searchTextBox = self.driver.find_element(By.ID, "twotabsearchtextbox")
        # Arama input alanını temizliyorum
        searchTextBox.clear()
        # Belirlediğim arama metninin arama input alanına yazıyorum
        searchTextBox.send_keys(self.search_term)
        # Aramaya başlıyorum
        searchTextBox.send_keys(Keys.RETURN)
        # Çıkan ilk ürüne tıklıyorum
        self.driver.find_element(By.XPATH,
            "(//div[@class='sg-col-inner']//img[contains(@data-image-latency,'s-product-image')])[2]").click()
        # Aranan ürün yeni bir sekmede açıldığı için o sekemeye geçiş yapıyorum
        self.driver.switch_to.window(self.driver.window_handles[1])
        # ürünün üzerinde ki sepete ekle butonuna basarak sepete ekliyorum
        self.driver.find_element(By.ID, "add-to-cart-button").click()
        # ürünün sepete başarıyla eklendiğini doğruluyorum
        self.assertTrue(self.driver.find_element(By.ID,
            "attach-added-to-cart-message").is_enabled())


    def tearDown(self):
        # çıkış yapıyorum
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()