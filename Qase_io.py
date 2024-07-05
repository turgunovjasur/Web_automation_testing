from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def setup_driver():
    service = Service(executable_path='C:\\Users\\User\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
    options = webdriver.ChromeOptions()
    web_driver = webdriver.Chrome(service=service, options=options)
    web_driver.maximize_window()
    web_driver.get("https://qase.io/")
    web_driver.implicitly_wait(10)
    return web_driver


def check_main_page(driver):
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div/h1[contains(text(), 'All-in-one')]")))
    assert "All-in-one" in element.text, "Sahifa ochilmadi!"


def click_start_free_button(driver):
    login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div/a[text()='Start for free']")))
    login_button.click()


def registration_form(driver, email, password, password_confirmation):
    email_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div/input[@placeholder='Work email']")))
    email_input.clear()
    email_input.send_keys(email)

    password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div/input[@placeholder='Password']")))
    password_input.clear()
    password_input.send_keys(password)

    password_confirmation_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div/input[@placeholder='Password confirmation']")))
    password_confirmation_input.clear()
    password_confirmation_input.send_keys(password_confirmation)


def click_sign_up_button(driver):
    sign_up_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button/span[contains(text(), 'Sign up with email')]")))
    sign_up_button.click()


def check_congratulations_page(driver):
    congratulations = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div/h1[contains(text(), 'Congratulations!')]")))
    assert "Congratulations!" in congratulations.text, "'Congratulations' Sahifasi ochilmadi!"


def check_email_on_page(driver, email):
    email_see = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div/span[@data-qase-test='email']")))
    assert email in email_see.text, "Email xato!"


def main():
    email = "tjasur22445354@gmail.com"
    password = '01062001Jasur@'
    password_confirmation = '01062001Jasur@'

    driver = setup_driver()
    try:
        check_main_page(driver)
        click_start_free_button(driver)
        registration_form(driver, email, password, password_confirmation)
        click_sign_up_button(driver)
        check_congratulations_page(driver)
        check_email_on_page(driver, email)
        print("Barcha testlar muvaffaqiyatli o'tdi!")
    except AssertionError as e:
        print(f"Test xatosi: {e}")
    except Exception as e:
        print(f"Kutilmagan xatolik: {e}")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()