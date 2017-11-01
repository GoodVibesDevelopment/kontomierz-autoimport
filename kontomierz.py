# This Python file uses the following encoding: utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

fp = webdriver.FirefoxProfile('profile.default')
browser = webdriver.Firefox(fp, executable_path='./geckodriver')

#LOGIN
browser.get("https://kontomierz.pl/k4/login")
email = browser.find_element_by_id("email")
email.send_keys("LOGIN_HERE")
password = browser.find_element_by_id("password")
password.send_keys("PASSWORD_HERE")
browser.find_element_by_xpath("//button[@type='submit']").click()
time.sleep(2)
#>LOGIN

#IMPORT
element = browser.find_elements(By.CLASS_NAME, "green")
element[0].click()

time.sleep(5)
element = browser.find_elements(By.CLASS_NAME, "green")
element[0].click()
time.sleep(60)
#>IMPORT

browser.quit()
