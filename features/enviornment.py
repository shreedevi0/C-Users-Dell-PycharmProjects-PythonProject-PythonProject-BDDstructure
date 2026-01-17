from selenium import webdriver
import time

def after_scenario(context):
    context.browser.find_element_by_xpath("//span[@class='oxd-userdropdown-tab']").click()
    time.sleep(2)
    context.browser.find_element_by_xpath("//a[normalize-space()='Logout']").click()
    time.sleep(2)