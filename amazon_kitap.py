from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest, time, re
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class Amazon(unittest.TestCase):
    @classmethod
    def setUp(cls):
        
        # Firefox tarayıcısı için gerekli geckodriver aranıyor
        cls.driver = webdriver.Firefox(executable_path="/Users\Yunus\Desktop\Test dersi/geckodriver")
        cls.driver.implicitly_wait(30)
        # Amazon sayfasının url'si tanımlanıyor
        cls.driver.get("https://www.amazon.com.tr/")
        # Tarayıcı tam ekran olacak şekilde büyütülüyor
        cls.driver.maximize_window()


    def test_amazon(self):

        first_book_title = "Şeker Portakalı"

        # Çerezleri kabul ediyoruz
        self.driver.find_element(By.ID,'sp-cc-accept').click()
        self.driver.implicitly_wait(5)
        time.sleep(3)
        
        input_alan = self.driver.find_element(By.XPATH,"//input[@id='twotabsearchtextbox']")
        # Arama input alanı erişilebilir mi kontrol et
        self.assertTrue(input_alan.is_enabled())
        # Arama kutusuna tıkla ve 'Kitap İsmi' gir
        self.driver.find_element(By.XPATH,"//input[@id='twotabsearchtextbox']").send_keys(first_book_title)
        # Aramayı başlat
        self.driver.find_element(By.XPATH,"//input[@id='twotabsearchtextbox']").submit()
                                      
        print("done")
        
        


        
        # Çıkan ilk ürüne tıklıyorum
        time.sleep(3)
        self.driver.find_element(By.XPATH,"(//div[@class='sg-col-inner']//img[contains(@data-image-latency,'s-product-image')])[1]").click()

        # Ürünün başlığı kontrol
        time.sleep(3)
        title = self.driver.find_element(By.XPATH,'//*[@id="productTitle"]').text.strip()
        self.assertEqual(first_book_title,title)
        print("Title done")
    
        # Ürünün yazarı kontrol
        time.sleep(3)
        author = self.driver.find_element(By.XPATH,'//*[@id="bylineInfo"]/span[1]/a').text.strip()
        self.assertEqual(author,"Jose Mauro De Vasconcelos")
        print("Author done")

        # Ürünün dili kontrol
        time.sleep(3)
        language = self.driver.find_element(By.XPATH, '//*[@id="detailBullets_feature_div"]/ul/li[2]/span/span[2]').text.strip()
        
        self.assertEqual(language,"Türkçe")
        print("Language done")
        
        # Ürünün sayfa sayısı kontrol
        time.sleep(3)
        pages = self.driver.find_element(By.XPATH,'//*[@id="detailBullets_feature_div"]/ul/li[3]/span/span[2]').text.strip()
        pages = pages[:3]
        self.assertEqual(pages,"184")
        print("Pages done")

        print("Pages = " , pages)
        print("Title = ", title)
        print("Author = ", author)
        print("Language = ", language)
        
        
    @classmethod    
    def tearDown(cls):
        # Tarayıcı Kapatılıyor
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()    
