import time
from selenium.webdriver.common.by import By
import selenium.webdriver as webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import WebDriverException
import pytest

@pytest.fixture(scope="module")
def browser():
    try:
        
        firefox_options = Options()
        firefox_options.headless = True
        browser = webdriver.Firefox(service=Service(r'/var/lib/jenkins/workspace/TestAutomation/selenium-taskbase/geckodriver'),options=firefox_options)
        return browser
    except WebDriverException as e:
        print(f"WebDriverException: {e}")

@pytest.fixture(scope="module")
def url_to_open():
    return 'http://114.143.149.14:4356//TaskbaseAWS-2.0/NeovaTaskBase/LoginPage.aspx'


def test_login(browser,url_to_open):
    try:
        browser.get(url_to_open)
        username_input = browser.find_element(By.ID, 'txtUserName')
        password_input = browser.find_element(By.ID, 'txtPassword')
        login_button = browser.find_element(By.ID, 'btnLogin')

        username = "shubham_joshi@neovasolutions.in"
        password = "MH12hy6196"

        username_input.send_keys(username)
        password_input.send_keys(password)

        login_button.click()
        time.sleep(3)
        print(browser.title)
        assert "Neova Task Base" in browser.title
    finally:
        browser.quit()

