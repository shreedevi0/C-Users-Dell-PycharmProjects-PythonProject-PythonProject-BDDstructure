from behave import *
from selenium import webdriver
import time
from datetime import datetime

@given('Launch the Browser')
def launch_browser(context):
    context.browser = webdriver.Chrome(executable_path=r"D:\chromedriver.exe")
    context.browser.maximize_window()
    time.sleep(2)

@when('Open the Website')
def open_website(context):
    context.browser.get('https://opensource-demo.orangehrmlive.com')
    time.sleep(2)

@when('Login with valid username "{username}" and Password "{password}"')
def login(context, username, password):
    context.browser.find_element_by_xpath("//input[@placeholder='Username']").send_keys(username)
    context.browser.find_element_by_xpath("//input[@placeholder='Password']").send_keys(password)
    context.browser.find_element_by_xpath("//button[normalize-space()='Login']").click()
    time.sleep(3)

@when('Navigate to PIM page')
def navigate(context):
    context.browser.find_element_by_xpath("//span[normalize-space()='PIM']").click()
    context.browser.save_screenshot(r'C:\Users\Dell\PycharmProjects\PythonProject\PythonProject\BDDstructure\Screenshot\PIM.png')
    time.sleep(2)

@then('click on Add Employee')
def navigate(context):
    context.browser.find_element_by_xpath("//body").click()
    time.sleep(2)







