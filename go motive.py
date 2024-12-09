from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import autoit
import bs4
import pandas as pd
from bs4 import BeautifulSoup
import win32com.client
import fnmatch

clientlist = pd.read_csv('KeepTruckin_JulyMiles_Load.csv')

username = "eld_stidum@glostone.com"
password = "asdfasdf&qwerqwer"

GoMotive = "https://account.gomotive.com/log-in?referer_url=https%3A%2Fgomotive.com%2F"

Edge_options = Options()
Driver = webdriver.Edge(options=Edge_options)

time.sleep(2)

Driver.get(GoMotive)

Driver.find_element("id", "user_email").send_keys(username)
Driver.find_element("id", "user_password").send_keys(password)


Driver.find_element("id", "sign-in-button").click()

time.sleep(8)

if Driver.find_element("id", "pendo-close-guide-0dfa4bce"):
	Driver.find_element("id", "pendo-close-guide-0dfa4bce").click()
else:
	time.sleep(1)

reports = "https://app.gomotive.com/en-US/#/reports/ifta-trips/vehicle;start_date=2023-07-01;end_date=2023-07-31;report_id=26;report_type=normal"

Driver.get(reports)

time.sleep(6)

Driver.find_element(By.CLASS_NAME, "btn.header-btn.option-btn.ant-btn.ant-dropdown-trigger.ng-star-inserted.ant-btn-default").click()

time.sleep(1)

Driver.find_element(By.XPATH, "//*[text()='Export as CSV']").click()

time.sleep(1)

logout = "https://app.gomotive.com/en-US/#/logout"

Driver.get(logout)

time.sleep(1)

Driver.get(GoMotive)







