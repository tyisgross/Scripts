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
outlook = "https://outlook.office.com/mail/"
milesfolder = "https://outlook.office.com/mail/AAMkAGI2Zjc0MWIyLTQ1NzQtNGQ2NC1iMzczLTRjODI3OGVhMjdkNQAuAAAAAACMeylGRhVyRqnBIYUu2q8wAQC4yPOMg0mDRKrsViwqv06IAAAYHcCvAAA%3D"
fuelfolder = "https://outlook.office365.com/mail/AAMkAGI2Zjc0MWIyLTQ1NzQtNGQ2NC1iMzczLTRjODI3OGVhMjdkNQAuAAAAAACMeylGRhVyRqnBIYUu2q8wAQC4yPOMg0mDRKrsViwqv06IAAAYHcCwAAA%3D"
outuser = "tyg@glostone.com"
outpassword = "Gr0$$Fl33t"
ClientList = pd.read_csv('C:/Python/AugustMiles.csv')
ClientUser = ClientList.UserName
ClientPass = ClientList.Password
ClientName = ClientList.CompanyName
ClientMiles = ClientList.Miles
ClientFuel = ClientList.Fuel
a = 0
Driver = webdriver.Chrome()
time.sleep(.5)
IFTA = "https://app.gomotive.com/en-US/#/reports/ifta-trips/vehicle;start_date=2023-08-01;end_date=2023-08-31;report_id=26;report_type=normal"
GoMotive = "https://account.gomotive.com/log-in?referer_url=https%3A%2Fgomotive.com%2F"
FuelTax = "https://app.gomotive.com/en-US/#/reports/ifta-fuel/vehicle;start_date=2023-08-01;end_date=2023-08-31;report_id=27;report_type=normal"
motivelogout = "https://app.gomotive.com/en-US/#/logout"
Driver.get(GoMotive)
time.sleep(4)
Driver.execute_script("window.open('https://outlook.office.com/mail/','OutlookTab');")
time.sleep(4)
#Driver handle 0 will be GoMotive and 1 will be Outlook
Driver.switch_to.window(Driver.window_handles[1])
Driver.find_element(By.CLASS_NAME, "form-control.ltr_override.input.ext-input.text-box.ext-text-box").send_keys(outuser)
Driver.find_element(By.CLASS_NAME, "win-button.button_primary.button.ext-button.primary.ext-primary").click()
time.sleep(2)
Driver.find_element(By.CLASS_NAME, "form-control.input.ext-input.text-box.ext-text-box").send_keys(outpassword)
Driver.find_element(By.CLASS_NAME, "win-button.button_primary.button.ext-button.primary.ext-primary").click()
time.sleep(2)
Driver.find_element(By.CLASS_NAME, "win-button.button_primary.button.ext-button.primary.ext-primary").click()
time.sleep(3)
Driver.get(fuelfolder)
time.sleep(7)
def ITC_Miles(login):
    global a
    try:
        Driver.switch_to.window(Driver.window_handles[0])
        Driver.get(FuelTax)
        time.sleep(2)
        Driver.find_element("id", "user_email").send_keys(ClientUser[a])
        Driver.find_element("id", "user_password").send_keys(ClientPass[a])
        Driver.find_element("id", "sign-in-button").click()
        time.sleep(10)
        Driver.find_element(By.CLASS_NAME, "btn.header-btn.option-btn.ant-btn.ant-dropdown-trigger.ng-star-inserted.ant-btn-default").click()
        time.sleep(1)
        Driver.find_element(By.XPATH, "//*[text()='Export as CSV']").click()
        time.sleep(1)
        Driver.get(motivelogout)
        time.sleep(1)
        print(ClientName[a] + " fuel .csv order succeeded"
        outlookdownload(True)


def outlookdownload(start):
    global a
    time.sleep(40)
    Driver.switch_to.window(Driver.window_handles[1])
    Driver.find_element(By.XPATH, "//div[@style='position: absolute; left: 0px; top: 0px; height: 81px; width: 100%;']").click()
    time.sleep(2)
    Driver.find_element(By.LINK_TEXT, "Click here to Download Report.").click()
    time.sleep(5)
    for milesfiles in glob.glob('C:/Users/tyg.GLOSTONETRUCKIN/Downloads/*.csv'):
        os.rename(milesfiles, ClientImport[a])
    a += 1
    ITC_Miles(True)

ITC_Miles(True)
