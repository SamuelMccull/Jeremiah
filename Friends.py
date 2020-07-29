import selenium
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def addFriends(driver):
    driver.get("https://www.facebook.com/?sk=ff")
    time.sleep(4)

    element = driver.find_element_by_xpath('//*[@id="u_0_11"]/button[1]')
    element.click()
