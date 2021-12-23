# Gerekli olan kütüphanelerin içeri aktarılması
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

"""
Birim(Unit) Test
- [] LinkedIn sayfasına giriş
- [] Email input alanına kullanıcı emaili yazılır
- [] Şifre input alanına kullanıcı şifresi yazılır
- [] Giriş butonuna basıldığında kullanıcının hesabı açılır
"""

class LinkedInWebTesting(unittest.TestCase):
	# ziyaret edilecek URL'yi saklamak için değişken
	base_url = "https://www.linkedin.com"

	# hesap bilgilerini içeren degiskenler
	email = "testprojesi1@gmail.com"
	password = "beykent1997"

	def setUp(self):
		# ChromeDriver'ın bağlanması
		self.driver = webdriver.Chrome("/Users/furkangulsen/projects/chromedriver")
		# Tarayıcı büyütülmüş pencerede yüklenmesi
		self.driver.maximize_window()
        # Browserın yüklenmesi için belirli bir süre beklemelidir
		self.driver.implicitly_wait(10) 
		

	def test_load_home_page(self):
		 # Web sayfasının ChromeDrive ile açılması
		self.driver.get(self.base_url)
		# Doğru URL'ye sahip sitenin yüklenip yüklenmediğini test etme
		self.assertTrue("Log In or Sign Up" == self.driver.title)
		time.sleep(1)
		
	def fill_email_input(self):
		# Email input alanını doldurma
		email_elem = self.driver.find_element_by_id('session_key')
		email_elem.send_keys(self.email)

	def fill_password_input(self):
		# Şifre input alanını doldurma
		password_elem = self.driver.find_element_by_id('session_password')
		password_elem.send_keys(self.password)



	def tearDown(self):
		self.driver.close()


if __name__ == '__main__':
    unittest.main()
    
# Giriş butonuna tıklanılır


# girişin başarılı olduğunu kontrol etmek için
# unittest.TestCase.assertTrue(browser.find_element_by_id("main").is_enabled())

