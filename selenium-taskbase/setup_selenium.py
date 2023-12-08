import selenium.webdriver as webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options


def setup():
    gecko_driver_path = './selenium-taskbase/geckodriver'
    firefox_service = Service(gecko_driver_path)
    firefox_options = Options()
    firefox_options.headless = True
    browser = webdriver.Firefox(service=firefox_service,options=firefox_options)
    return browser