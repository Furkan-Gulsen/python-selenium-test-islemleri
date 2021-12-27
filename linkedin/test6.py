#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import time
from random import randint
import datetime as dt
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver import ChromeOptions, Chrome
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException

delay = 10
# browser ı parametre olarak alıyoruz
def choose_driver():
    # webdriver chrome ise
    opts = ChromeOptions()
    opts.add_experimental_option("detach", True)
    driver = webdriver.Chrome(executable_path="/Users/furkangulsen/projects/chromedriver")
    return driver 



def login(driver):

    username = "dogushankaya.itu@gmail.com"
    password = "trendyolcase"

    driver.get("https://www.trendyol.com/")
    time.sleep(7)
    

    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    WebDriverWait(driver,delay).until(EC.element_to_be_clickable((By.CLASS_NAME,"modal-close"))).click()
    time.sleep(3)
    WebDriverWait(driver,delay).until(EC.element_to_be_clickable((By.CLASS_NAME,"login-register-button-container"))).click()
    WebDriverWait(driver,delay).until(EC.element_to_be_clickable((By.ID,"email"))).send_keys(username)
    WebDriverWait(driver,delay).until(EC.element_to_be_clickable((By.ID,"password"))).send_keys(password)
    driver.find_element_by_id('loginSubmit').click()

# tablara tıklıyor ve fotoları kontrol ediyor
def tabs_click(driver):
    item = "item"
    big_butik_loaded = "bigBoutiqueImage lazy-load-trigger loaded"
    other_loaded = "littleBoutiqueImage lazy-load-trigger loaded"
    # tabların id leri item1-2-3 diye gidiyor. id lere göre tablarda geziyor range(1,11)
    for i in range(1,11):
        time.sleep(3)
        WebDriverWait(driver,delay).until(EC.element_to_be_clickable((By.ID,item+str(i)))).click()
        time.sleep(5)

        # büyük butiklerin kaç tane olduğunu buluyor
        large_butik = driver.find_elements_by_css_selector('.butik.large.col-lg-12.col-md-12.col-xs-12')
        large_butik_len = len(large_butik)
        print(" büyük butik sayısı: ",large_butik_len)
        webdriver.ActionChains(driver).send_keys(Keys.SPACE).perform()
        webdriver.ActionChains(driver).send_keys(Keys.SPACE).perform()

        # büyük butik fotoları kontrol
        for k in range(1,large_butik_len + 1):
            big_element = driver.find_element_by_xpath('//*[@id="dynamic-boutiques"]/div/div/div['+str(k)+']/div[1]/a/img')
            time.sleep(0.1)
            print("{}   {}".format(k,big_element.get_attribute('class')))
            if k%3 == 0:
                webdriver.ActionChains(driver).send_keys(Keys.SPACE).perform()
            if big_element.get_attribute('class') != big_butik_loaded:
                time.sleep(0.2)

                big_butik_name = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[1]/div/div/div['+str(k)+']/div[1]/a')
                    #dosya = open("butik_gorsel_hata.txt",'a')
                with open('butik_gorsel_hata.txt','a',encoding='utf-8') as dosya:
                    dosya.write("tarih : {} Butik Adı: {}  \n".format(dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),big_butik_name.get_attribute('title')))


        # diğer butiklerin kaç tane olduğunu buluyor
        other_butik = driver.find_elements_by_css_selector('.col-lg-4.col-md-4.col-xs-4.butik.small.left')
        other_butik_len = len(other_butik)
        print("other butik sayısı : ",other_butik_len)

        webdriver.ActionChains(driver).send_keys(Keys.SPACE).perform()
        webdriver.ActionChains(driver).send_keys(Keys.SPACE).perform()
        webdriver.ActionChains(driver).send_keys(Keys.SPACE).perform()
        # diğer butiklerin fotoları kontrol
        for j in range(1,other_butik_len + 1):
            other_element = driver.find_element_by_xpath('//*[@id="container"]/div[3]/div[2]/div/div['+str(j)+']/div[1]/a/img')
            #time.sleep(0.2)
            print("{}   {}".format(j,other_element.get_attribute('class')))
            if j%6==0:
                webdriver.ActionChains(driver).send_keys(Keys.SPACE).perform()
            if other_element.get_attribute('class') != other_loaded :

                time.sleep(0.2)
                other_butik_name = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[2]/div/div['+str(j)+']/div[1]/a')

                with open('butik_gorsel_hata.txt','a',encoding='utf-8') as dosya:
                    dosya.write("tarih : {} Butik Adı: {}  \n".format(dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),other_butik_name.get_attribute('title')))

def click_random_boutique(driver):
    time.sleep(2)
    # rastgele bir sekmeye gidiyor
    i = randint(1,10)
    item = "item"
    # sekmekeye gidiyor
    WebDriverWait(driver,delay).until(EC.element_to_be_clickable((By.ID,item+str(i)))).click()
    # butiğe gidiyor
    butik = driver.find_elements_by_css_selector('.col-lg-4.col-md-4.col-xs-4.butik.small.left')
    i = randint(1,len(butik))
    print(len(butik), i)
    driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[2]/div/div['+str(i)+']').click()
    for i in range(20):
        webdriver.ActionChains(driver).send_keys(Keys.END).perform()
        time.sleep(1)

    element_list = driver.find_elements_by_class_name('product-box')

    j = randint(1,len(element_list))
    element = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/div/div/div[3]/div['+str(j)+']')


    # eşyanın tüknip tükenmediğinin kontrolü
    while(element.get_attribute('class') != "available"):
        j = randint(1,len(element_list))
        print("j: {}   element len: {} ".format(j,len(element_list)))
        try:
            element = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/div/div/div[3]/div['+str(j)+']/div/a/div[4]/div')
        except NoSuchElementException:
            j = randint(1,len(element_list))
            element = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/div/div/div[3]/div['+str(j)+']/div/a/div[4]/div')


    driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/div/div/div[3]/div['+str(j)+']').click()

    # gelen butikte beden seçme varsa beden seçip sepeye ekliyor. yoksa direkt olarak sepete ekliyor
    try:
        driver.find_element_by_id('basketForm').click()
        driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/form/div[1]/div[3]/div/ul/div/div[1]/li[2]').click()
        driver.find_element_by_id('addToBasketButton').click()
    except ( NoSuchElementException, ElementNotInteractableException) :
        webdriver.ActionChains(driver).send_keys(Keys.F5).perform()
        WebDriverWait(driver,delay).until(EC.element_to_be_clickable((By.ID,'addToBasketButton'))).click()



browser = choose_driver()
login(browser)
tabs_click(browser)
click_random_boutique(browser)