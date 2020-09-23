from xpaths import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import os
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(executable_path='./gontijo/chromedriver/chromedriver')

url = 'https://teamshift.crossknowledge.com/'
driver.get(url)
time.sleep(1)
#Elements Xpaths
xpath_log_in_button = '/html/body/main/header/nav/div[2]/div/div/button'
email_input = '//*[@id="login-form__login"]'
next_btn = '//*[@id="js-modal-login-member"]/div/div/div[3]/button[2]'
password_input = '//*[@id="login-form__password"]'
login_btn = '//*[@id="js-modal-login-member"]/div/div/div[3]/button[2]'

#Actions to perform
print("Clicking on Login Button")
driver.find_element_by_xpath(xpath_log_in_button).click()
print("Success!")
time.sleep(5)
print("passing credentials - email")
driver.find_element_by_xpath(email_input).send_keys("tiagoluiz@samerica.com")
print("Success!")
time.sleep(5)
print("Clicking Next Button")
driver.find_element_by_xpath(next_btn).click()
print("Success!")
print("passing credentials - password")
time.sleep(5)
driver.find_element_by_xpath(password_input).send_keys("WLS2020qa")
print("Success!")
print("clicking on Login Button")
driver.find_element_by_xpath(login_btn).click()
print("success!")

