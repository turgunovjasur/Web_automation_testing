from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pytest


@pytest.fixture(params=["chrome", "mozillafirefox"], scope="class")
def invoke_driver(request):
    global web_driver
    if request.param == "chrome":
        web_driver = webdriver.Chrome(service=Service(
            executable_path='C:\\Users\\User\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe'),
                                      options=webdriver.ChromeOptions())
        # web_driver = webdriver.Chrome(ChromeDriverManager().install())
    web_driver.maximize_window()
    web_driver.get("https://qase.io/")
    request.cls.driver = web_driver
    web_driver.implicitly_wait(10)
    yield
    web_driver.quit()

