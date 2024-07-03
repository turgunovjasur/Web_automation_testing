from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

service = Service(executable_path='C:\\Users\\User\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
options = webdriver.ChromeOptions()
web_driver = webdriver.Chrome(service=service, options=options)
web_driver.maximize_window()
web_driver.get("https://it-market.uz/")
web_driver.implicitly_wait(10)   # qidirish so'rovlari uchun kutilayotgan vaqt

"""Sign up testing"""
email = "tjasur224@gmail.com"
# element = web_driver.find_element(By.XPATH, "//div/h1[contains(text(), 'Oʻzbekiston IT-bozoridagi')]")

try:
    element = WebDriverWait(web_driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div/h1/ya-tr-span[contains(text(), 'Ваш проводник')]"))
    )
    assert "Ваш проводник" in element.text, "Sahifa ochilmadi!"
    print("Test muvaffaqiyatli o'tdi: Oʻzbekiston IT-bozoridagi xabari topildi.")
except:
    print("Xatolik: Sahifa ochilmadi yoki 'Oʻzbekiston IT-bozoridagi' xabari topilmadi.")

web_driver.close()
