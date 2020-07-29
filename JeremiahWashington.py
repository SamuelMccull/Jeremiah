import selenium
import sys
import time
import logIO
import Friends
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = logIO.login()
for x in range(10):
    Friends.addFriends(driver)
    time.sleep(3)
logIO.logout(driver)
# example            new = driver.page_source
