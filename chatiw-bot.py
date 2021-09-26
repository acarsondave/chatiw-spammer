from selenium import webdriver
import random
from bs4 import BeautifulSoup
import sys
import datetime
import os
import threading
import smtplib, ssl
import pandas
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import StaleElementReferenceException
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(executable_path="chromedriver", options=options)
driver.maximize_window()
driver.get("https://www.chatiw.com")
print("Please login and press the Enter key to continue")
input(": ")
time.sleep(5)
message = input("Enter the message to send: ")

chats = driver.find_elements_by_class_name("list-group-item-action")
print(len(chats))
x = 0

try:
    try:
        print("- Starting spammer -")
        for i in chats:
            x+=1
            print(x)
            try:
                i.click()
                time.sleep(1)
                box = driver.find_element_by_css_selector("#app > div > div.col-lg-8.col-md-7.col-xl-8 > div.h-100 > div > div.p-2.row.no-gutters.rounded-0.card-footer.bg-chatiw-orange > div.col-xl-10.col-lg-9.col-md-7.col-9.position-relative > input")
                box.send_keys(message)
                box.send_keys(Keys.ENTER)
            except ElementClickInterceptedException:
                print("None account")
                pass
    except StaleElementReferenceException:
        print("- Finished the line... -")
except NoSuchElementException:
    if "ban" in driver.current_url:
        print("Banned from the server\n- Switching proxies -")
        
