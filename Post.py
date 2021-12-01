from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import unittest
import time
import wget
import os
import pyautogui
from selenium.webdriver.chrome.service import Service


option1=Options()
option1.add_argument("--disable-notifications")
driver = webdriver.Chrome(executable_path=r"C:\Users\user\chromedriver.exe", chrome_options=option1)
driver.maximize_window()
driver.get("https://facebook.com/")
username="083811"
password="Axiata"

driver.find_element_by_id("email").send_keys(username)
driver.find_element_by_id("pass").send_keys(password)
login=driver.find_element_by_name("login")
login.click()
driver.implicitly_wait(3)
driver.get("https://www.facebook.com/marketplace/")


driver.get('https://www.facebook.com/marketplace/you/selling')

driver.get('https://www.facebook.com/marketplace/you/selling?state=DRAFT')
driver.implicitly_wait(10)
n=2
for i in range(1,n):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(60)
    simpan=driver.find_elements_by_tag_name('a')
    simpan=[a.get_attribute('href') for a in simpan ]
    simpan=[a for a in simpan if str(a).startswith("https://www.facebook.com/marketplace/edit/")]
    print(simpan)
    print(len(simpan))
    b=1
    for a in simpan:
        driver.get(a)
        driver.implicitly_wait(10)
        
        dharga="50000"
        harga=driver.find_element_by_xpath('//label[@aria-label="Harga"]')
        harga.click()
        harga.send_keys(Keys.BACKSPACE+Keys.BACKSPACE+Keys.BACKSPACE+Keys.BACKSPACE+Keys.BACKSPACE+Keys.BACKSPACE)
        time.sleep(2)
        harga.send_keys(dharga)
        

        dlokasi=['Sukoharjo','Kendal','Slawi','Temanggung','Wonogiri',
    'Wonosobo','Surakarta','Magelang','semarang',
    'Bangkalan','Nganjuk','Banyuwangi','Ngawi',
    'Kanigoro','Bojonegoro','Pamekasan','Bangil',
    'Gresik','Ponorogo','Jember','Kraksaan',
    'Jombang','Sampang','Ngasem','Sidoarjo',
    'Lamongan','Situbondo','Lumajang','Sumenep',
    'Caruban','Trenggalek','Magetan','Tuban',
    'Kepanjen','Tulungagung','Mojosari','Batu',
    'Blitar','Mojokerto','Kediri','Pasuruan',
    'Madiun','Probolinggo','Malang','Surabaya',
    'Soreang','Bandung','Ngamprah','Banjar',
    'Cikarang','Bekasi','Cibinong','Bogor',
    'Ciamis','Cimahi','Ciamis','Cimahi',
    'Tarogong','Depok','Indramayu','Sukabumi',
    'Karawang','Tasikmalaya','Kuningan','Singaparna',
    'Majalengka','Sumedang','Parigi','Palabuhanratu',
    'Purwakarta','Subang'
    ]


        lokasi=driver.find_element_by_xpath('//input[@aria-label="Masukkan kota"]')
        lokasi.click()
        lokasi.send_keys(Keys.BACKSPACE+dlokasi[b])
        time.sleep(2)
        dlok=driver.find_element_by_xpath ('//li[@aria-selected="false"][1]')
        dlok.click()

        lanjutkan=driver.find_element_by_xpath('//div[@aria-label="Selanjutnya"]')
        lanjutkan.click()
        terbitkan=driver.find_element_by_xpath('//div[@aria-label="Terbitkan"]')
        terbitkan.click()
        time.sleep(10)     
        driver.get('https://www.facebook.com/marketplace/you/selling?state=DRAFT')
        lanjut=driver.find_element_by_xpath('//span[text()="(BIG PROMO 50%) JAM TANGAN ANTI AIR BISA COD / BAYAR DI TEMPATT"]')
        lanj=(lanjut.text)
        b+=1
        if lanj=="(BIG PROMO 50%) JAM TANGAN ANTI AIR BISA COD / BAYAR DI TEMPATT":
            continue
        else:
            break
