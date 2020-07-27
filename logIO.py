import selenium
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class logIO:
    def login():
        #opens facebook website
        driver = webdriver.Chrome()
        driver.get("https://www.facebook.com")
        
        old = driver.page_source

        #enters details
        userName = "jeremiahwashington0@outlook.com"
        password = "Outlook365"

        element = driver.find_element_by_id("email")
        element.send_keys(userName)

        element = driver.find_element_by_id("pass")
        element.send_keys(password)
    
        element.send_keys(Keys.RETURN)
        
        new = driver.page_source
        while(new == old):
            time.sleep(2)
            new = driver.page_source
        return driver

    def logout(driver):
        element = driver.find_element_by_id("logout")
        element.click()
