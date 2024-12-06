# John's automation for Clearinghouse

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
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
import pathlib



email = 'johnm@glostone.com'
password = 'L!feBurger2021'
clearinghouse = "https://clearinghouse.fmcsa.dot.gov/Query?PageNumber=1&SelectedTimeframe=Days7"

#Make chrome headless aka no window

chrome_options = Options()
chrome_options.add_argument("user-data-dir=C:\environments\selenium")
wd = webdriver.Chrome(options=chrome_options)
wd.minimize_window()
#launchingchrome

wd.get(clearinghouse)

time.sleep(.25)

wd.find_element("id", "user_email").send_keys(email)
wd.find_element("name", "user[password]").send_keys(password)

time.sleep(.25)

wd.find_element("name", "button").click()

twofact = int(input("Enter two factor passcode:"))

wd.find_element(By.CLASS_NAME, "usa-input.usa-input--big.string.required.one-time-code-input__input.validated-field__input").send_keys(twofact)

wd.find_element(By.CLASS_NAME, "usa-button.display-block.margin-top-5.usa-button--big.usa-button--wide").click()

wd.get(clearinghouse)

wd.find_element("id", "DownloadButton").click()

time.sleep(5)