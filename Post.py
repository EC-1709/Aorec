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
driver = webdriver.Chrome(executable_path=r"C:\Users\user\chromedriver.exe", chrome_options=option1)
driver.maximize_window
driver.get("https://facebook.com/")
username="enjangcahyana259@gmail.com"
password="ARFan1308"

driver.find_element_by_id("email").send_keys(username)
driver.find_element_by_id("pass").send_keys(password)
login=driver.find_element_by_name("login")
login.click()
driver.implicitly_wait(3)
driver.get("https://www.facebook.com/marketplace/")

for i in range(33):
    driver.get('https://www.facebook.com/marketplace/you/selling')
    driver.get('https://www.facebook.com/marketplace/you/selling?state=DRAFT')
    simpan=driver.find_element_by_xpath('//a[@aria-label="Lanjutkan"][1]')
    simpan.click()

    dharga="50000"
    harga=driver.find_element_by_xpath('//label[@aria-label="Harga"]')
    harga.click()
    harga.send_keys(Keys.BACKSPACE+Keys.BACKSPACE+Keys.BACKSPACE+Keys.BACKSPACE+Keys.BACKSPACE+Keys.BACKSPACE)
    time.sleep(2)
    harga.send_keys(dharga)
    time.sleep(3)

    dlokasi=['Banjarnegara','Kudus','Purwokerto','Klaten',
'Batang	','Mungkid','Blora','Pati','Boyolali','Kajen',
'Brebes','Pemalang','Cilacap','Purbalingga','Demak','Purworejo',
'Kebumen','Rembang','Karanganyar','Ungaran','Jepara','Sragen',
'Purwodadi','Sukoharjo','Kendal','Slawi','Temanggung','Wonogiri',
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
    lokasi.send_keys(Keys.BACKSPACE+dlokasi[i])
    time.sleep(2)
    dlok=driver.find_element_by_xpath ('//li[@aria-selected="false"][1]')
    dlok.click()

    lanjutkan=driver.find_element_by_xpath('//div[@aria-label="Selanjutnya"]')
    lanjutkan.click()
    terbitkan=driver.find_element_by_xpath('//div[@aria-label="Terbitkan"]')
    terbitkan.click()
    time.sleep(10)
