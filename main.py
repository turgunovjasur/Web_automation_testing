from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

service = Service(executable_path='C:\\Users\\User\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
options = webdriver.ChromeOptions()
web_driver = webdriver.Chrome(service=service, options=options)
web_driver.maximize_window()
web_driver.get("https://qase.io/")
web_driver.implicitly_wait(5)   # qidirish so'rovlari uchun kutilayotgan vaqt

"""Sign up testing"""
email = "tjazdsfdefdsfg656@gmail.com"
element = web_driver.find_element(By.XPATH, "//div/h1")
assert "All-in-one" in element.text, "Page did not open"
web_driver.find_element(By.XPATH, "//p/following-sibling::div/a[text()='Start for free']").click()
web_driver.find_element(By.XPATH, "//input[@name='email']").send_keys(email)
web_driver.find_element(By.XPATH, "//input[@name='password']").send_keys('0656256fgFJKKLgd#@')
web_driver.find_element(By.XPATH, "//input[@name='passwordConfirmation']").send_keys('0656256fgFJKKLgd#@')
# web_driver.find_element(By.XPATH, "//input[@name='emailPromoConfirmation']").click()
web_driver.find_element(By.XPATH, "//*[text()='Sign up with email']").click()
congratulation_label = web_driver.find_element(By.XPATH, "//div/h1")
email_container = web_driver.find_element(By.XPATH, "//div/span")
assert "Congratulations!" in congratulation_label.text, "Sign up failed!!!"
assert email in email_container.text, "Email does not appear!!!"

web_driver.close()
