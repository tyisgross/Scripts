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
os.chdir("C:/")
username = "tyg"
password = "MotiveIsAwesome"
FuelTaxWizard = "http://itc-staging.glostone.com/FuelTaxWizard.aspx"
ITC = "http://itc-staging.glostone.com/"
ClientList = pd.read_csv('C:/Python/March.csv')
ClientUser = ClientList.UserName
ClientPass = ClientList.Password
ClientName = ClientList.CompanyName
ClientMiles = ClientList.Miles
ClientFuel = ClientList.Fuel
a = 0
Driver = webdriver.Chrome()
time.sleep(.5)
IFTA = "https://app.gomotive.com/en-US/#/reports/ifta-trips-rearch/vehicle;start_date=2024-03-01;end_date=2024-03-31;report_id=2411;report_type=normal"
GoMotive = "https://account.gomotive.com/log-in?referer_url=https%3A%2Fgomotive.com%2F"
Fuel = "https://app.gomotive.com/en-US/#/reports/ifta-fuel/vehicle;start_date=2024-03-01;end_date=2024-03-31;report_id=27;report_type=normal" 
motivelogout = "https://app.gomotive.com/en-US/#/logout"
Driver.get(GoMotive)
time.sleep(4)
Driver.execute_script("window.open('http://itc-staging.glostone.com/','ITCS');")
time.sleep(4)
#Driver handle 0 will be GoMotive and 1 will be ITC
Driver.switch_to.window(Driver.window_handles[1])
Driver.find_element("id", "weblogin").send_keys(username)
Driver.find_element("id", "webpassword").send_keys(password)
time.sleep(2)
Driver.find_element(By.CLASS_NAME, "link3").click()
time.sleep(2)
Driver.get(FuelTaxWizard)
time.sleep(2)
Driver.find_element("id", "ctl00_ContentPlaceHolder1_xpnlPage_xtabPages_T1").click()
Driver.switch_to.window(Driver.window_handles[0])

def MotiveLogin(login):
    global a
    try:
        Driver.get(IFTA)
        time.sleep(2)
        Driver.find_element("id", "user_email").send_keys(ClientUser[a])
        Driver.find_element("id", "user_password").send_keys(ClientPass[a])
        Driver.find_element("id", "sign-in-button").click()
        time.sleep(10)
        try:
            Driver.find_element("id", "pendo-close-guide-77063459").click()
        except: 
            pass
        MilesOrder(True)
    except: 
        print(ClientName[a] + ' login failed')

def MilesOrder(order):
    global a
    try:
        Driver.find_element(By.CLASS_NAME, "phx-button.dropdown-trigger.phx-button-secondary-default-standard.phx-has-suffix.phx-button-md.phx-content-empty").click()
        time.sleep(1)
        Driver.find_element(By.XPATH, "//*[text()='Export as CSV']").click()
        time.sleep(10)
        print(ClientName[a] + ' miles download succeeded')
        MilesImp(True)
    except:
        print(ClientName[a] + ' miles download failed')
        return

def MilesImp(Glob):
    global a
    time.sleep(5)
    try:
        for milesfiles in glob.glob('C:/Users/tyg.GLOSTONETRUCKIN/Downloads/*.csv'):
            os.rename(milesfiles, ClientMiles[a])
        Driver.switch_to.window(Driver.window_handles[1])
        Driver.find_element("id", "ctl00_ContentPlaceHolder1_xcboClientListing_I").send_keys(Keys.CONTROL + "a")
        Driver.find_element("id", "ctl00_ContentPlaceHolder1_xcboClientListing_I").send_keys(ClientName[a])
        Driver.find_element("id", "ctl00_ContentPlaceHolder1_xpnlPage_xtabPages_ASPxLabel2").click()
        Driver.find_element("id", "ctl00_ContentPlaceHolder1_xpnlPage_xtabPages_xflUploadMiles_TextBox0_Input").send_keys(ClientMiles[a])
        Driver.find_element("id", "ctl00_ContentPlaceHolder1_xpnlPage_xtabPages_xbtnImportMiles_CD").click()
        time.sleep(5)
        print(ClientName[a] + ' miles import succeeded')
        FuelOrder(True)
    except: 
        print(ClientName[a] + ' miles import failed')
        return


def FuelOrder(order):
    try:
        Driver.switch_to.window(Driver.window_handles[0])
        Driver.get(Fuel)
        time.sleep(5)
        Driver.find_element(By.CLASS_NAME, "phx-button.dropdown-trigger.phx-button-secondary-default-standard.phx-has-suffix.phx-button-md.phx-content-empty").click()
        time.sleep(1)
        Driver.find_element(By.XPATH, "//*[text()='Export as CSV']").click()
        time.sleep(10)
        Driver.get(motivelogout)
        time.sleep(1)
        print(ClientName[a] + ' fuel order succeeded')
        FuelImp(True)
    except:
        print(ClientName[a] + ' fuel order failed')
        return

def FuelImp(Glob):
    global a
    time.sleep(5)
    try:
        for milesfiles in glob.glob('C:/Users/tyg.GLOSTONETRUCKIN/Downloads/*.csv'):
            os.rename(milesfiles, ClientFuel[a])
        Driver.switch_to.window(Driver.window_handles[1])
        Driver.find_element("id", "ctl00_ContentPlaceHolder1_xpnlPage_xtabPages_T2").click()
        Driver.find_element("id", "ctl00_ContentPlaceHolder1_xpnlPage_xtabPages_xflUploadFuel_TextBox0_Input").send_keys(ClientFuel[a])
        Driver.find_element("id", "ctl00_ContentPlaceHolder1_xpnlPage_xtabPages_xbtnImportFuel").click()
        time.sleep(2)
        Driver.find_element("id", "ctl00_ContentPlaceHolder1_xpnlPage_xtabPages_T1").click()
        print(ClientName[a] + ' fuel import succeeded')
        a += 1
        Driver.switch_to.window(Driver.window_handles[0])
        MotiveLogin(True)
    except:
        print(ClientName[a] + ' fuel import failed')
        return



MotiveLogin(True)
