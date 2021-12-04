from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import unittest
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
import pyautogui


option1=Options()
option1.add_argument("--disable-notifications")
driver = webdriver.Chrome(executable_path=r"C:\Users\user\Belajar\chromedriver.exe", chrome_options=option1)
driver.maximize_window
driver.get("https://facebook.com/")
username="email"
password="kata sandi"

driver.implicitly_wait(7)
driver.find_element_by_id("email").send_keys(username)
driver.find_element_by_id("pass").send_keys(password)
login=driver.find_element_by_name("login")
login.click()
driver.get("https://www.facebook.com/marketplace/?ref=app_tab")



for i in range(1):
    driver.get("https://www.facebook.com/marketplace/create")

    driver.get("https://www.facebook.com/marketplace/create/item")

    foto=driver.find_element_by_xpath('//div[@class="oajrlxb2 gs1a9yip g5ia77u1 mtkw9kbi tlpljxtp qensuy8j ppp5ayq2 goun2846 ccm00jje s44p3ltw mk2mc5f4 rt8b4zig n8ej3o3l agehan2d sk4xxmp2 rq0escxv nhd2j8a9 j83agx80 mg4g778l btwxx1t3 pfnyh3mw p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x tgvbjcpo hpfvmrgz jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso l9j0dhe7 i1ao9s8h esuyzwwr f1sip0of du4w35lb lzcic4wl n00je7tq arfg74bv qs9ysxi8 k77z8yql abiwlrkh p8dawk7l buofh1pr"]')
    foto.click()
    time.sleep(5)
    pyautogui.write(r'C:\Users\user\Desktop\jam\anyar\"2.jpg" "3.jpg" "WhatsApp Image 2021-10-20 at 09.43.53.jpeg"')
    pyautogui.press("enter")
    time.sleep(10)
    judul="(BIG PROMO 50%) JAM TANGAN ANTI AIR BISA COD / BAYAR DI TEMPAT"
    harga="100000"
    k1="* Tampilan: Analog "
    k6="* Movement: Quartz "
    k2="* Dial Shape: Round"
    k3="* Material: Silicone"
    k4="* Case Diameter: 45mm"
    k5="* Case Thickness: 8mm"
    k7="* Band length: 20mm (include case)"
    k8="* Band Width: 15mm"
    k9="gfdgdhfh"

        
    driver.find_element_by_xpath('//label[@aria-label="Judul"]').send_keys(judul)
    driver.find_element_by_xpath('//label[@aria-label="Harga"]').send_keys(harga)

    kategori=driver.find_element_by_xpath('//label[@aria-label="Kategori"]')
    kategori.click()
    perhiasan=driver.find_element_by_xpath('//*[text()="Perhiasan & Aksesori"]')
    perhiasan.click()

    kondisi=driver.find_element_by_xpath('//label[@aria-label="Kondisi"]')
    kondisi.click()
    baru=kondisi=driver.find_element_by_xpath('//div[@class="oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 j83agx80 p7hjln8o kvgmc6g5 opuu4ng7 oygrvhab kj2yoqh6 pybr56ya dflh9lhu f10w8fjw scb9dxdr i1ao9s8h esuyzwwr f1sip0of lzcic4wl n00je7tq arfg74bv qs9ysxi8 k77z8yql l9j0dhe7 abiwlrkh p8dawk7l bp9cbjyn dwo3fsh8 btwxx1t3 pfnyh3mw du4w35lb"]')
    baru.click()


    driver.find_element_by_xpath('//label[@aria-label="Keterangan"]').send_keys(k1+Keys.ENTER+k6+Keys.ENTER+k2+Keys.ENTER+k3+Keys.ENTER+k4+Keys.ENTER+ k5 +Keys.ENTER+k7+Keys.ENTER+k8+Keys.ENTER+k9+Keys.ENTER)




    simpan=driver.find_element_by_xpath('//*[text()="Simpan Draf"]')
    simpan.click()
    time.sleep(10)
