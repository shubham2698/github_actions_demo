from setup_selenium import setup
from steps import login,select_project,select_phase,select_time,write_description,add_data
from get_data import get_data

import selenium.webdriver as webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import WebDriverException

url_to_open = 'http://114.143.149.14:4356//TaskbaseAWS-2.0/NeovaTaskBase/LoginPage.aspx'
file_path = './data.csv'

gecko_driver_path = 'geckodriver'
firefox_service = Service(gecko_driver_path)
firefox_options = Options()
firefox_options.headless = True
browser = webdriver.Firefox(service=firefox_service,options=firefox_options)

try:
    
    login(browser,url_to_open)
    select_project(browser)    
    select_phase(browser)
    select_time(browser)
    write_description(browser,get_data(file_path))
    add_data(browser)

finally:
    browser.quit()
