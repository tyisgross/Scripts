from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time
import os
import shutil
import autoit
import bs4
import pandas as pd
import glob
import fnmatch
from bs4 import BeautifulSoup
os.chdir("C:/")
ClientList = pd.read_csv('C:/Python/Eroad.csv')
ClientUser = ClientList.UserName
ClientPass = ClientList.Password
ClientName = ClientList.CompanyName
ClientMF = ClientList.ClientMF
a = 0
username = "tyg"
password = "MotiveIsAwesome"
FuelTaxWizard = "http://itc-staging.glostone.com/FuelTaxWizard.aspx"
ITC = "http://itc-staging.glostone.com/"
Eroad = "https://my.eroad.com/login"
IFTA = "https://my.eroad.com/Portal/report/tax/ifta/fleetsummary"
logout = "https://my.eroad.com/logout"
Driver = webdriver.Chrome()
Driver.get(Eroad)
time.sleep(2)
Driver.execute_script("window.open('http://itc-staging.glostone.com/','ITCS');")
time.sleep(4)
#Driver handle 0 will be Eroad and 1 will be ITC
Driver.switch_to.window(Driver.window_handles[1])
Driver.find_element("id", "weblogin").send_keys(username)
Driver.find_element("id", "webpassword").send_keys(password)
time.sleep(2)
Driver.find_element(By.CLASS_NAME, "link3").click()
time.sleep(2)
Driver.get(FuelTaxWizard)
time.sleep(2)
Driver.find_element("id", "ctl00_ContentPlaceHolder1_xpnlPage_xtabPages_T1").click()
os.chdir("C:/")
global a
Driver.switch_to.window(Driver.window_handles[0])

def Eroad(download):
    global a
    if ClientName[a] == "Stop":
        print("Eroad is done")
        return
    else:
        Driver.switch_to.default_content()
        Driver.find_element("id", "username").send_keys(ClientUser[a])
        Driver.find_element("id", "password").send_keys(ClientPass[a])
        Driver.find_element(By.CLASS_NAME, "ant-btn.ant-btn-primary.ant-btn-lg").click()
        time.sleep(3)
        Driver.get(IFTA)
        time.sleep(3)
        try:
            Driver.find_element(By.ID, "pendo-close-guide-b702a9e7").click()
        except:
            pass
        iframe = Driver.find_element(By.ID, "depotIframe")
        Driver.switch_to.frame(iframe)
        select_element = Driver.find_element(By.NAME, "timespan")
        select = Select(select_element)
        select.select_by_value('monthly')
        time.sleep(.5)
        Driver.find_element("id", "previousLink").click()
        time.sleep(1)
        Driver.find_element(By.XPATH, "//*[text()='By Vehicle']").click()
        time.sleep(1)
        Driver.find_element(By.XPATH, "//*[text()='Show Details']").click()
        time.sleep(3)
        Driver.find_element(By.ID, "reportoptions").click()
        time.sleep(1)
        Driver.find_element(By.CLASS_NAME, "hideOnPermissionError").click()
        time.sleep(6)
        for milesfiles in glob.glob('C:/Users/tyg.GLOSTONETRUCKIN/Downloads/*.csv'):
         os.rename(milesfiles, ClientMF[a])
        Driver.switch_to.default_content()
        Driver.get(logout)
        print(ClientName[a] + ' is downloaded')
        time.sleep(2)
        Driver.switch_to.window(Driver.window_handles[1])
        ITC(True)



def ITC(imp):
    global a
    Driver.find_element("id", "ctl00_ContentPlaceHolder1_xcboClientListing_I").send_keys(Keys.CONTROL + "a")
    Driver.find_element("id", "ctl00_ContentPlaceHolder1_xcboClientListing_I").send_keys(ClientName[a])
    Driver.find_element("id", "ctl00_ContentPlaceHolder1_xcboClientListing_I").send_keys(Keys.ENTER)
    time.sleep(.5)
    Driver.find_element("id", "ctl00_ContentPlaceHolder1_xpnlPage_xtabPages_xcboMilesImportType_I").send_keys(Keys.CONTROL + "a")
    Driver.find_element("id", "ctl00_ContentPlaceHolder1_xpnlPage_xtabPages_xcboMilesImportType_I").send_keys("ERoad [.csv, Fleet Summary]")
    time.sleep(.5)
    Driver.find_element("id", "ctl00_ContentPlaceHolder1_xpnlPage_xtabPages_xcboMilesImportType_I").send_keys(Keys.ENTER)
    Driver.find_element("id", "ctl00_ContentPlaceHolder1_xpnlPage_xtabPages_xflUploadMiles_TextBox0_Input").send_keys(ClientMF[a])
    Driver.find_element("id", "ctl00_ContentPlaceHolder1_xpnlPage_xtabPages_xbtnImportMiles_CD").click()
    time.sleep(.5)
    print(ClientName[a] + ' is imported')
    a += 1
    Driver.switch_to.window(Driver.window_handles[0])
    Eroad(True)
    


Eroad(True)
