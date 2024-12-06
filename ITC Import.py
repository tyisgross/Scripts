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
ClientList = pd.read_csv('C:/Python/December.csv')
ClientUser = ClientList.UserName
ClientPass = ClientList.Password
ClientName = ClientList.CompanyName
ClientMiles = ClientList.Miles
ClientFuel = ClientList.Fuel
a = 0
Driver = webdriver.Chrome()
time.sleep(1)
ITC = "http://itc-staging.glostone.com/"
time.sleep(.25)
Driver.get(ITC)
time.sleep(3)
username = "tyg"
password = "MotiveIsAwesome"
Driver.find_element("id", "weblogin").send_keys(username)
Driver.find_element("id", "webpassword").send_keys(password)
time.sleep(2)
Driver.find_element(By.CLASS_NAME, "link3").click()
time.sleep(2)
FuelTaxWizard = "http://itc-staging.glostone.com/FuelTaxWizard.aspx"
Driver.get(FuelTaxWizard)
time.sleep(2)
os.chdir("C:/")
Driver.find_element("id", "ctl00_ContentPlaceHolder1_xpnlPage_xtabPages_T1").click()
def MilesImport(run):
    global a
    if ClientName[a] == "Sierra Mountain Express, Inc" or "SMT":
        Driver.find_element("id", "ctl00_ContentPlaceHolder1_xcboClientListing_I").send_keys(ClientName[a])
        Driver.find_element("id", "ctl00_ContentPlaceHolder1_xpnlPage_xtabPages_xflUploadMiles_TextBox0_Input").send_keys(ClientMiles[a])
        Driver.find_element("id", "ctl00_ContentPlaceHolder1_xpnlPage_xtabPages_xbtnImportMiles_CD").click()
        print("Loading of Sierra Mountain Express is complete")
        input("hit enter to continue: ")
        Driver.find_element("id", "ctl00_ContentPlaceHolder1_xcboClientListing_I").send_keys(Keys.CONTROL + "a")
        Driver.find_element("id", "ctl00_ContentPlaceHolder1_xcboClientListing_I").send_keys(Keys.DELETE)
        a += 1
        MilesImport(True)
    else:
        Driver.find_element("id", "ctl00_ContentPlaceHolder1_xcboClientListing_I").send_keys(Keys.CONTROL + "a")
        Driver.find_element("id", "ctl00_ContentPlaceHolder1_xcboClientListing_I").send_keys(ClientName[a])
        Driver.find_element("id", "ctl00_ContentPlaceHolder1_xpnlPage_xtabPages_ASPxLabel2").click()
        Driver.find_element("id", "ctl00_ContentPlaceHolder1_xpnlPage_xtabPages_xflUploadMiles_TextBox0_Input").send_keys(ClientMiles[a])
        Driver.find_element("id", "ctl00_ContentPlaceHolder1_xpnlPage_xtabPages_xbtnImportMiles_CD").click()
        time.sleep(2)
        Driver.find_element("id", "ctl00_ContentPlaceHolder1_xpnlPage_xtabPages_T2").click()
        Driver.find_element("id", "ctl00_ContentPlaceHolder1_xpnlPage_xtabPages_xflUploadFuel_TextBox0_Input").send_keys(ClientFuel[a])
        Driver.find_element("id", "ctl00_ContentPlaceHolder1_xpnlPage_xtabPages_xbtnImportFuel").click()
        time.sleep(2)
        Driver.find_element("id", "ctl00_ContentPlaceHolder1_xpnlPage_xtabPages_T1").click()
        a += 1
        MilesImport(True)

MilesImport(True)


# e9*4203*91 is old password