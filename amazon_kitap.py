from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest, time, re
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class Amazon(unittest.TestCase):
    @classmethod
    def setUp(cls):
        # Call Firefox browser
        cls.driver = webdriver.Firefox(executable_path="directory")
        cls.driver.implicitly_wait(30)
        #Load amazon.in site
        cls.driver.get("https://www.amazon.com.tr/")
        cls.driver.maximize_window()


    def test_amazon(self):

        # Çerezleri kabul ediyoruz
        self.driver.find_element(By.ID,'sp-cc-accept').click()
        self.driver.implicitly_wait(5)
        time.sleep(3)

        # In the search box, enter ' data catalog' and search'
        self.driver.find_element_by_xpath("//input[@id='twotabsearchtextbox']").send_keys("Şeker Portakalı")
        self.driver.find_element_by_xpath("//input[@id='twotabsearchtextbox']").submit()
                                      
        print("done")
        
        first_book_title = "Şeker Portakalı"


        
        # Çıkan ilk ürüne tıklıyorum
        time.sleep(3)
        self.driver.find_element_by_xpath("(//div[@class='sg-col-inner']//img[contains(@data-image-latency,'s-product-image')])[1]").click()

        #check for title
        time.sleep(3)
        title = self.driver.find_element_by_xpath('//*[@id="productTitle"]').text.strip()
        self.assertEqual(first_book_title,title)
        print("Title done")
    
        # check for author
        time.sleep(3)
        author = self.driver.find_element_by_xpath('//*[@id="bylineInfo"]/span[1]/a').text.strip()
        self.assertEqual(author,"Jose Mauro De Vasconcelos")
        print("Author done")
        
        # check for paperback price
        #time.sleep(2)
        ##paperback = self.driver.find_element_by_xpath('//*[@id="a-autoid-3-announce"]/span[2]/span').text.strip()
        #paperback = paperback[:6]
        #self.assertEqual(paperback,"29,00")
        #print("Paperback done", paperback)

        #print("Paperback = " , paperback)
        print("Title = ", title)
        print("Author = ", author)
        
        
    @classmethod    
    def tearDown(cls):
        #Close the browser
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()    
