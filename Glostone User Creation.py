### edit this stuff first
newuseremail = "shellya@glostone.com"
newuseracct = "shellya"
newuserfn = "shelly"
newuserln = "abbs"
###
### variables set first
newuserpw = "Glostone2024!"
newinbox = newuseracct + "'s inbox"
###
###
### Import dependent modules
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.keys import locate_with
from selenium.webdriver.support.ui import Select
import time
import os
import shutil
import autoit
import bs4
import pandas as pd
import glob
import fnmatch
from bs4 import BeautifulSoup
##
DW = "https://docuware.gradientway.com/DocuWare/Settings"
DWadmin = "dwadmin"
DWpassword = "NINERS13303"
dwuserpass = "12345678"
NetworkID = "glostonetruckin\\" + newuseracct
##LMS stuff
LMSus = "tyg@glostone.com"
LMSpw = "PVATCRYaFjLANWnh7pj0uH*A"
LMS = "https://learning.cleanfleet.org/wp-admin/user-new.php"
LMScourse = "https://learning.cleanfleet.org/wp-admin/post.php?post=453&action=edit&currentTab=sfwd-courses-settings"
## launch chrome
Driver = webdriver.Chrome()

#add user to lms and add the onboarding project
def LMSuser(create):
	Driver.get(LMS)
	Driver.find_element("id", "user_login").send_keys(LMSus)
	Driver.find_element("id", "user_pass").send_keys(LMSpw)
	Driver.find_element("id", "wp-submit").click()
	Driver.find_element("id", "user_login").send_keys(newuseracct)
	Driver.find_element("id", "email").send_keys(newuseremail)
	Driver.find_element("id", "first_name").send_keys(newuserfn)
	Driver.find_element("id", "last_name").send_keys(newuserln)
	Driver.find_element("id", "createusersub").click()
	Driver.get(LMScourse)
	Driver.find_element("id", "learndash-binary-selector-search-learndash_course_users-453-left").send_keys(newuserfn)
	Driver.find_element("id", "learndash-binary-selector-search-learndash_course_users-453-left").send_keys(Keys.ENTER)
	Driver.find_element(By.XPATH, "//*[text()='" + newuserfn + " " + newuserln + " " + "(" + newuseracct + ")" "']").click()
	Usertable = Driver.find_element("id", "learndash_course_users-453")
	Usertable.find_element(By.CLASS_NAME, "learndash-binary-selector-button-add").click()
	
#Add DW
def DWuser(create):
	Driver.get(DW)
	Driver.find_element("id", "Username").send_keys(DWadmin)
	Driver.find_element("id", "Password").send_keys(DWpassword)
	Driver.find_element("id", "loginBtn").click()
	Driver.find_element(By.CLASS_NAME, "ui-icon.icon-auto.dw-icon-user-management")
	iframe = Driver.find_element(By.CLASS_NAME, "plugin-frame")
	Driver.switch_to.frame(iframe)
	Driver.find_element(By.CLASS_NAME, "btn.btn-primary").click()
	Driver.find_element(By.XPATH, "//*[text()='New unnamed user']").click()
	Driver.find_element(By.CLASS_NAME, "form-control").send_keys(newuseracct)
	Driver.find_element("id", "firstNameInput").send_keys(newuserfn)
	Driver.find_element("id", "lastNameInput").send_keys(newuserln)
	Driver.find_element("id", "emailInput").send_keys(newuseremail)
	Driver.find_element(By.XPATH, "//*[text()='Set password now']").click()
	Driver.find_element(By.CLASS_NAME, "form-control.password-font").send_keys("12345678")
	confirmpw = Driver.find_element(By.CLASS_NAME, "col-xs-3.has-error")
	confirmpw.find_element(By.CLASS_NAME, "form-control.password-font").send_keys("12345678")
	Driver.find_element(By.CLASS_NAME, "checkbox-container").click()
	Driver.find_element("id", "basketNameInput").send_keys(Keys.CONTROL + "a")
	Driver.find_element("id", "basketNameInput").send_keys(newinbox)
	filecabinet = Driver.find_element(By.TAG_NAME, "COMBOBOX")
	filecabinetselect = filecabinet.find_element(By.TAG_NAME, "SELECT")
	filecabinetselect.send_keys("FuelTax")
	