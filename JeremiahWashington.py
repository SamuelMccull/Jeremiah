import selenium
import sys
import time
from logIO import logIO
from Friends import Friends
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = logIO.login()
Friends.addFriends(driver)
logIO.logout(driver)
# example            new = driver.page_source
