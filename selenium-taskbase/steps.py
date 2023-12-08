import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from datetime import datetime

def login(browser,url_to_open):
    browser.get(url_to_open)
    username_input = browser.find_element(By.ID, 'txtUserName')
    password_input = browser.find_element(By.ID, 'txtPassword')
    login_button = browser.find_element(By.ID, 'btnLogin')

    username = 'shubham_joshi@neovasolutions.in'
    password = 'MH12hy6196'

    username_input.send_keys(username)
    password_input.send_keys(password)

    login_button.click()
    time.sleep(3)


def select_date(browser):
    today_date = datetime.now().strftime('%d-%b-%Y')
    text_field = browser.find_element(By.ID, 'ctl00_ContentPlaceHolder1_txtEntryDate')
    text_field.clear()  # Clear existing text
    text_field.send_keys(today_date) 


def select_project(browser):
    dropdown = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.ID, 'ctl00_ContentPlaceHolder1_ddProjects'))
    )
    dropdown.click()
    non_billable_option = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//option[text()="NON-BILLABLE"]'))
    )
    non_billable_option.click()
    


def select_phase(browser):
    dropdown = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.ID, 'ctl00_ContentPlaceHolder1_ddPhase'))
    )
    dropdown.click()
    self_learning_for_project = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//option[text()="Self Learning_For the Project"]'))
    )
    self_learning_for_project.click()


def select_time(browser):
    dropdown = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.ID, 'ctl00_ContentPlaceHolder1_ddEntryHours'))
    )
    dropdown.click()
    time_select = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//option[text()="8"]'))
    )
    time_select.click()


def write_description(browser,data):
    textarea = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, 'ctl00_ContentPlaceHolder1_txtDescription'))
    )
    text_to_input = data
    textarea.send_keys(text_to_input)


def add_data(browser):
    element_to_click = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.ID, 'ctl00_ContentPlaceHolder1_btnAddTimesheetEntry'))
    )
    element_to_click.click()