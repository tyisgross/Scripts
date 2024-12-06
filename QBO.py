from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os
import shutil
import autoit
import bs4
import pandas as pd
import glob
import fnmatch
from bs4 import BeautifulSoup
qblogin = "https://accounts.intuit.com/app/sign-in"
qbusermgt = "https://app.qbo.intuit.com/app/usermgt"
qbuser = "qbservice@cleanfleet.org"
qbpass = "CleanScreen23!!"
userfname = "Christine"
userlname = "Penuel"
usermail = "Christinep@glostone.com"
Driver = webdriver.Chrome()
Driver.get(qbusermgt)
time.sleep(3)
Driver.find_element("id", "iux-identifier-first-international-email-user-id-input").send_keys(qbuser)
Driver.find_element(By.CLASS_NAME, "IdentifierFirstUnknownSubmitButton__StyledLockIcon-sc-1ec9o89-0.dAsOuU").click()
time.sleep(2)
Driver.find_element("id","iux-password-confirmation-password").send_keys(qbpass)
Driver.find_element(By.XPATH, "//*[text()='Continue']").click()
time.sleep(5)
#Driver.find_element(By.XPATH, "//*[text()='CleanFleet']").click()
Driver.find_element(By.XPATH, "//*[text()='Glostone Trucking Solutions Inc']").click()
time.sleep(1)
time.sleep(1)
time.sleep(1)
time.sleep(1)
time.sleep(1)
time.sleep(1)
time.sleep(1)
Driver.find_element(By.XPATH, "//*[text()='Add user']").click()
time.sleep(1)
time.sleep(1)
time.sleep(1)
time.sleep(1)
time.sleep(1)
Driver.find_element("id", "idc-text-input-First name").send_keys(userfname)
Driver.find_element("id", "idc-text-input-Last name").send_keys(userlname)
Driver.find_element("id", "idc-text-input-Email").send_keys(usermail)
Driver.find_element(By.CLASS_NAME, "TextField-TFLabelWrapper-6a31d78").send_keys("Standard limited customers and vendors")
Driver.find_element("id", "idsDropdownTypeahead1-item-0").click()
time.sleep(1)
time.sleep(1)
time.sleep(1)
Driver.find_element(By.XPATH, "//*[text()='Send invitation']").click()
