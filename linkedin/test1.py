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

# ziyaret edilecek URL'yi saklamak için değişken


# ChromeDriver'ın bağlanması
driver = webdriver.Chrome("/Users/furkangulsen/projects/chromedriver")
# Tarayıcı büyütülmüş pencerede yüklenmesi
driver.maximize_window()
# Browserın yüklenmesi için belirli bir süre beklemelidir
driver.implicitly_wait(5) 
# Web sayfasının ChromeDrive ile açılması
driver.get("https://www.linkedin.com")
print("Title: ", driver.title)
# Doğru URL'ye sahip sitenin yüklenip yüklenmediğini test etme
time.sleep(3)


def login():
	# hesap bilgilerini içeren degiskenler
	email = "testprojesi1@gmail.com"
	password = "beykent1997"

	# Email input alanını doldurma
	email_elem = driver.find_element_by_id('session_key')
	email_elem.send_keys(email)

	# Şifre input alanını doldurma
	password_elem = driver.find_element_by_id('session_password')
	password_elem.send_keys(password)

	# Giriş butonuna tıklanılır
	login_button = driver.find_element_by_css_selector('.sign-in-form__submit-button')
	login_button.click()


	add_post_button = driver.find_element_by_css_selector('.artdeco-button.artdeco-button--muted.artdeco-button--4.artdeco-button--tertiary.ember-view.share-box-feed-entry__trigger')
	add_post_button.click();

	time.sleep(1)
	post_text_area = driver.find_element_by_css_selector(".ql-editor.ql-blank")
	post_text_area.send_keys("Birim Test Denemesi2")

	time.sleep(2)
	post_send_button = driver.find_element_by_css_selector('.share-actions__primary-action.artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view')
	post_send_button.click();

login()
time.sleep(1)


# girişin başarılı olduğunu kontrol etmek için
# unittest.TestCase.assertTrue(browser.find_element_by_id("main").is_enabled())
