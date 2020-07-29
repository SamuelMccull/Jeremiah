import selenium
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# This automatically gets the right webdriver without needing to do wonky install stuff
from webdriver_manager.chrome import ChromeDriverManager


def login():
    option = Options()
    option.add_argument("--disable-infobars")
    option.add_argument("start-maximized")
    option.add_argument("--disable-extensions")

    # Pass the argument 1 to allow and 2 to block
    option.add_experimental_option("prefs", { 
        "profile.default_content_setting_values.notifications": 1 
    })

    #opens facebook website
    driver = webdriver.Chrome(chrome_options=option, executable_path=ChromeDriverManager().install())
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
        print("Page has changed :)")
    return driver

def logout(driver):
    element = driver.find_element_by_id("logout")
    element.click()
