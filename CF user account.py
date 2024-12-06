from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os
import autoit
import bs4
import pandas as pd
from bs4 import BeautifulSoup
Driver = webdriver.Chrome()
time.sleep(1)
CF = "http://itc.glostone.com/"
CFuser = "https://cleanscreen.cleanfleet.org/AdminUserEdit.aspx?ID=-1"
time.sleep(.25)
Driver.get(CF)
time.sleep(3)
username = "tyg"
password = "53*4d3f*b8"
fname = "joe"
lname = "haul"
email = "joeh@glostone.com"
newus = "joeh"
newpw = "Password123!"
Driver.find_element("id", "weblogin").send_keys(username)
Driver.find_element("id", "webpassword").send_keys(password)
time.sleep(2)
Driver.find_element(By.CLASS_NAME, "link3").click()
time.sleep(2)
Driver.get(ITCuser)
time.sleep(2)
Driver.find_element("id", "ctl00_ContentPlaceHolder1_xpnlPage_xgrd_header0_hyperlinkAddNew").click()
time.sleep(2)
Driver.find_element("id", "xtabPages_xtxtLogin_I").send_keys(Keys.CONTROL + "a")
Driver.find_element("id", "xtabPages_xtxtLogin_I").send_keys(newus)
Driver.find_element("id", "xtabPages_xtxtFirstName_I").send_keys(Keys.CONTROL + "a")
Driver.find_element("id", "xtabPages_xtxtFirstName_I").send_keys(fname)
Driver.find_element("id", "xtabPages_xtxtLastName_I").send_keys(lname)
Driver.find_element("id", "xtabPages_xcboRoleID_I").send_keys(Keys.CONTROL + "a")
Driver.find_element("id", "xtabPages_xcboRoleID_I").send_keys("Licensing Specialist")
Driver.find_element("id", "xtabPages_xchkAccountManager_S_D").click()
Driver.find_element("id", "xtabPages_xchkActive_S_D").click()
Driver.find_element("id", "xtabPages_xtxtEmail_I").send_keys(Keys.CONTROL + "a")
Driver.find_element("id", "xtabPages_xtxtEmail_I").send_keys(email)
Driver.find_element("id", "xtabPages_xcboDocuwareTray_I").send_keys(Keys.CONTROL + "a") 
Driver.find_element("id", "xtabPages_xcboDocuwareTray_I").send_keys(newus + "Working Tray")
Driver.find_element(By.XPATH, "//*[text()='Save']").click()