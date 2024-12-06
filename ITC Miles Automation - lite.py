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
ClientList = pd.read_csv('AugustMiles.csv')
ClientUser = ClientList.UserName
ClientPass = ClientList.Password
ClientName = ClientList.CompanyName
ClientFile = ClientList.CSV
ClientImport = ClientList.Import
ClientDownload = ClientList.Download
ClientOutcome = ClientList.Outcome
a = 49
Driver = webdriver.Chrome()
time.sleep(.5)
GoMotive = "https://account.gomotive.com/log-in?referer_url=https%3A%2Fgomotive.com%2F"
IFTA = "https://app.gomotive.com/en-US/#/reports/ifta-trips/vehicle;start_date=2023-07-01;end_date=2023-07-31;report_id=26;report_type=normal"
FuelTax = ""
motivelogout = "https://app.gomotive.com/en-US/#/logout"
time.sleep(3)
def ITC_Miles_lite(login):
    global a
    time.sleep(12)
    Driver.get(GoMotive)
    time.sleep(3)
    Driver.find_element("id", "user_email").send_keys(ClientUser[a])
    Driver.find_element("id", "user_password").send_keys(ClientPass[a])
    Driver.find_element("id", "sign-in-button").click()
    time.sleep(3)
    if a < 112 :
        try:
         time.sleep(3)
         Driver.get(IFTA)
         time.sleep(5)
         Driver.find_element(By.CLASS_NAME, "btn.header-btn.option-btn.ant-btn.ant-dropdown-trigger.ng-star-inserted.ant-btn-default").click()
         time.sleep(3)
         Driver.get(motivelogout)
         time.sleep(3)
         print(ClientName[a] + ' is complete')
         ClientOutcome[a] = 'verified'
         a += 1
         ITC_Miles_lite(True)
        except:
         print(ClientName[a] + ' login failed')
         ClientOutcome[a] = 'failed'
         Driver.get(motivelogout)
         a += 1
         ITC_Miles_lite(True)
    else :
        Clientlist.to_csv('VerifiedMiles.csv')

ITC_Miles_lite(True)


