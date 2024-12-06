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
import bs4
import pandas as pd
import glob
import fnmatch
from bs4 import BeautifulSoup
os.chdir("C:/")
ClientList = pd.read_csv('C:/Python/August.csv')
ClientUser = ClientList.UserName
ClientPass = ClientList.Password
ClientName = ClientList.CompanyName
ClientMiles = ClientList.Miles
ClientFuel = ClientList.Fuel
a = 0
Driver = webdriver.Chrome()
time.sleep(.5)
GoMotive = "https://account.gomotive.com/log-in?referer_url=https%3A%2Fgomotive.com%2F"
motivelogout = "https://app.gomotive.com/en-US/#/logout"
Marketplace = "https://app.gomotive.com/en-US/#/app-marketplace/app/glostone-trucking-solutions"
Driver.get(GoMotive)
time.sleep(4)

def MotiveLogin(login):
    global a
    try:
        Driver.get(Marketplace)
        time.sleep(10)
        Driver.find_element("id", "user_email").send_keys(ClientUser[a])
        Driver.find_element("id", "user_password").send_keys(ClientPass[a])
        Driver.find_element("id", "sign-in-button").click()
        time.sleep(10)
        Driver.find_element(By.CLASS_NAME, "ui.primary.button.install-btn.ng-star-inserted").click()
        time.sleep(2)
        Driver.find_element(By.XPATH, '//button[text()="Install"]').click()
        time.sleep(5)
        Driver.find_element(By.XPATH, '//button[text()="Done"]').click()
        print(ClientName[a] + ' app installation requested')
        time.sleep(3)
        Driver.get(motivelogout)
        time.sleep(10)
        a += 1
        MotiveLogin(True)
    except:
        print(ClientName[a] + ' app installation failed')

MotiveLogin(True)


# New website that has the api key : https://app.gomotive.com/en-US/#/admin/developers/api