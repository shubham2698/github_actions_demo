from setup_selenium import setup
from steps import login,select_project,select_phase,select_time,write_description,add_data
from get_data import get_data

url_to_open = 'http://114.143.149.14:4356//TaskbaseAWS-2.0/NeovaTaskBase/LoginPage.aspx'
file_path = 'selenium-taskbase/data.csv'
browser = setup()

try:
    
    login(browser,url_to_open)
    select_project(browser)    
    select_phase(browser)
    select_time(browser)
    write_description(browser,get_data(file_path))
    add_data(browser)

finally:
    browser.quit()
