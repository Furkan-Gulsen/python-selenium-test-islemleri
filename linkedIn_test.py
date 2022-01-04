# Gerekli olan kütüphanelerin içeri aktarılması
import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random


class LinkedIn(unittest.TestCase):
	# hesap bilgilerini içeren degiskenler
	email = ""
	password = ""

	# paylaşılacak post içeriği
	postText = "Birim Test "

	def setUp(self):
		# ChromeDriver'ın bağlanması
		self.service = Service('directory/chromedriver')
		self.driver = webdriver.Chrome(service=self.service)
		# Tarayıcı büyütülmüş pencerede yüklenmesi
		self.driver.maximize_window()
		# Sunucunun yüklenmesi için belirli bir süre bekliyorum
		self.driver.implicitly_wait(10) 


	def test_add_item_to_cart(self):
		# Web sayfasının ChromeDrive ile açılması
		self.driver.get("https://www.linkedin.com")
		# Doğru URL'ye sahip sitenin yüklenip yüklenmediğini test etme
		self.assertLessEqual(self.driver.title, "Log In or Sign Up")

		email_elem = self.driver.find_element(By.ID, 'session_key')
		# Email input alanı erişilebilir mi kontrol et
		self.assertTrue(email_elem.is_enabled())
		# Email input alanını doldurma
		email_elem.send_keys(self.email)

		
		password_elem = self.driver.find_element(By.ID, 'session_password')
		# Password input alanı erişilebilir mi kontrol et
		self.assertTrue(password_elem.is_enabled())
		# Şifre input alanını doldurma
		password_elem.send_keys(self.password)

		login_button = self.driver.find_element(By.CSS_SELECTOR, '.sign-in-form__submit-button')
		# Giriş butonu görünür mü ve tıklanılabilir mi kontrol et
		self.assertTrue(login_button.is_displayed())
		self.assertTrue(login_button.is_enabled())
		# Giriş butonuna tıklanılır
		login_button.click()


		home_page = self.driver.find_element(By.ID,"voyager-feed")
		# ana sayfa açıldı mı kontrol et
		self.assertTrue(home_page.is_displayed())


		add_post_button = self.driver.find_element(By.CSS_SELECTOR,'.artdeco-button.artdeco-button--muted.artdeco-button--4.artdeco-button--tertiary.ember-view.share-box-feed-entry__trigger')
		# Gönderi paylaşma butonu görünür mü ve tıklanılabilir mi kontrol et
		self.assertTrue(add_post_button.is_displayed())
		self.assertTrue(add_post_button.is_enabled())
		add_post_button.click();

		# post paylaşma
		time.sleep(2)
		self.postText = self.postText + str(random.randint(0,100000))
		post_text_area = self.driver.find_element(By.CSS_SELECTOR,".ql-editor.ql-blank")
		# editör alanı erişilebilir mi kontrol et
		self.assertTrue(post_text_area.is_enabled())
		# post yazısını editöre yazma işlemi
		post_text_area.send_keys(self.postText)

		time.sleep(2)
		post_send_button = self.driver.find_element(By.CSS_SELECTOR,'.share-actions__primary-action.artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view')
		# Gönderi paylaşma butonu görünür mü ve tıklanılabilir mi kontrol et
		self.assertTrue(post_send_button.is_displayed())
		self.assertTrue(post_send_button.is_enabled())
		post_send_button.click();

		# post paylaşımını kontrol etme
		time.sleep(2)
		post_content_div = self.driver.find_element(By.CSS_SELECTOR,'.break-words>span')
		self.assertTrue(post_content_div.is_displayed())
		self.assertEqual(self.postText, post_content_div.text)
		time.sleep(3)
		
		
	def tearDown(self):
		# çıkış yapıyorum
		self.driver.quit()

if __name__ == "__main__":
    unittest.main()
