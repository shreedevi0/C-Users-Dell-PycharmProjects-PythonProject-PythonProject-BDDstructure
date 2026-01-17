from behave import *
from selenium import webdriver
import time
from datetime import datetime

@given('Navigate to Time')
def navigate_to_time(context):
    context.browser.find_element_by_xpath("//span[normalize-space()='Dashboard']").click()
    context.browser.save_screenshot(r"C:\Users\Dell\PycharmProjects\PythonProject\PythonProject\BDDstructure\Screenshot\Time.png")
    time.sleep(3)

@when('User click on Attendance and select the My Records')
def click_attendance(context):
    context.browser.find_element_by_xpath("//span[normalize-space()='Leave']").click()
    context.browser.save_screenshot(r"C:\Users\Dell\PycharmProjects\PythonProject\PythonProject\BDDstructure\Screenshot\Myrecords.png")
    time.sleep(3)

@then('Record page should display')
def record_page(context):
    context.browser.save_screenshot(r'C:\Users\Dell\PycharmProjects\PythonProject\PythonProject\BDDstructure\Screenshot\record.png')
    time.sleep(2)

