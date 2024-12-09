### edit this stuff first
newuseracct = "diannad"
newuserfn = "dianna"
newuserln = "dilling"
###
### variables set first
newuseremail = newuseracct + "@cleanfleet.org"
newuserpw = "Cleanfleet2024!"
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
DWpassword = "AHHHHHHHHHHHHHH"
dwuserpass = "OOOOOOOOOOOOO"
NetworkID = "glostonetruckin\\" + newuseracct
##LMS stuff
LMSus = "tyg@glostone.com"
LMSpw = "ADASDASDASDASDASDASDASDASDASD*A"
LMS = "https://learning.cleanfleet.org/wp-admin/users.php"
LMScourse = "https://learning.cleanfleet.org/wp-admin/post.php?post=453&action=edit&currentTab=sfwd-courses-settings"
## Safeguard stuff
SFG = "https://safeguard.gradientway.com"
sfguser = "tyg"
sfgpw = "AAAAAAAAAASSSSSSSSSSSDDDDDDDDDDDDD"
## launch chrome
Driver = webdriver.Chrome()


#add user to lms and add the onboarding project
#tested and finalized
def LMSuser(remove):
    Driver.get(LMS)
    Driver.find_element("id", "user_login").send_keys(LMSus)
    Driver.find_element("id", "user_pass").send_keys(LMSpw)
    Driver.find_element("id", "wp-submit").click()
    time.sleep(2)
    Driver.find_element("id", "user-search-input").send_keys(newuserfn)
    Driver.find_element("id", "search-submit").click()
    ActionChains(Driver).move_to_element(Driver.find_element(By.CLASS_NAME, "username.column-username.has-row-actions.column-primary")).perform()
    Driver.find_element(By.CLASS_NAME, "submitdelete").click()
    time.sleep(1)
    Driver.find_element("id", "submit").click()
    try:
     Driver.find_element("id", "delete_option1").click()
     Driver.find_element("id", "reassign_user").click()
     Driver.find_element("id", "reassign_user").send_keys("CY")
     Driver.find_element("id", "reassign_user").send_keys(Keys.ENTER)
     Driver.find_element("id", "submit").click()
    except:
     pass
    return
	
#remove DW
#Tested and finalized
def DWuser(remove):
    Driver.get(DW)
    time.sleep(15)
    Driver.find_element("id", "Username").send_keys(DWadmin)
    Driver.find_element("id", "Password").send_keys(DWpassword)
    Driver.find_element("id", "loginBtn").click()
    time.sleep(3)
    Driver.find_element(By.CLASS_NAME, "ui-icon.icon-auto.dw-icon-user-management").click()
    time.sleep(2)
    iframe = Driver.find_element(By.CLASS_NAME, "plugin-frame")
    Driver.switch_to.frame(iframe)
    #end of navigation to user management
    Driver.find_element(By.CLASS_NAME, "gray-border").send_keys(newuseracct)
    time.sleep(1)
    Driver.find_element(By.CLASS_NAME, "disabled-table-row").click()
    ActionChains(Driver).move_to_element(Driver.find_element(By.CLASS_NAME, "ui-icon.icon-auto.button.bordered.dw-icon-delete.m-r-15")).perform()
    Driver.find_element(By.CLASS_NAME, "ui-icon.icon-auto.button.bordered.dw-icon-delete.m-r-15").click()
    time.sleep(1)
    Driver.find_element(By.CLASS_NAME, "toastr-confirm-btn.toastr-confirm-ok.main.ui-button.ui-widget.ui-state-default.ui-corner-all.ui-button-text-only").click()

## Safeguard decomm is not an easy process at this time.
#def Safeguard(remove):
#    Driver.get(SFG)
#    time.sleep(1)
#    Driver.find_element("id", "ASPxPopupControl1_pnlLogin_xtxtUserName_I").send_keys(sfguser)
 #   Driver.find_element("id", "ASPxPopupControl1_pnlLogin_xtxtPassword_I").send_keys(sfgpw)
  #  Driver.find_element("id", "ASPxPopupControl1_pnlLogin_xcmdLogin").click()
   # time.sleep(5)
    
