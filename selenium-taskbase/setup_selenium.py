import selenium.webdriver as webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import WebDriverException


def setup():
    try:
        gecko_driver_path = 'geckodriver'
        firefox_service = Service(gecko_driver_path)
        firefox_options = Options()
        firefox_options.headless = True
        browser = webdriver.Firefox(service=firefox_service,options=firefox_options)
        return browser
    except WebDriverException as e:
        print(f"WebDriverException: {e}")