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
df = pd.read_csv('C:/Python/Email Reports/CF IN 1124.csv',encoding='latin-1')
Sender = df.sender_address
msgsubject = df.message_subject
forwards = df['message_subject'].str.startswith("FW:")
fwb = df['message_subject'].str.startswith("Fwd:")
fwa = df['message_subject'].str.startswith("Fw:")
fwcont = df['message_subject'].str.startswith('"FW:')
replies = df['message_subject'].str.startswith("RE:")
repliescont = df['message_subject'].str.startswith('"RE:')
repliess = df['message_subject'].str.startswith("Re:")
repliesss = df['message_subject'].str.startswith('"Re:')
autore = df['message_subject'].str.startswith("Automatic reply:")
internalcf = df['sender_address'].str.endswith("@glostone.com")
internalgs = df['sender_address'].str.endswith("@cleanfleet.org")
SRFAX = df['message_subject'].str.startswith('"SRFax Transmission')
MSS = df['message_subject'].str.startswith('Microsoft 365 security:')
DI = df['message_subject'].str.startswith('Cleanfleet - Past Due Invoice')
MR = df['message_subject'].str.startswith('Cleanfleet - Membership Renewal')
RN = df['message_subject'].str.startswith('Cleanfleet - Random Notice')
GT = df['message_subject'].str.startswith('GeoTab Telematics')
AR = df['message_subject'].str.startswith('Monthly Account Renewal')
PA = df['message_subject'].str.startswith('Payment Authorization Needed')
DNRWA = df['sender_address'].str.startswith('DoNotReply')
df = df.drop(df[(DNRWA == True) | (PA == True) | (AR == True) | (GT == True) | (RN == True) | (MR == True) | (DI == True) | (fwa == True) | (fwb == True) | (MSS == True) | (SRFAX == True) | (forwards == True) | (fwcont == True) | (replies == True) | (repliescont == True) | (repliess == True) | (repliesss == True) | (autore == True) | (internalcf == True) | (internalgs == True)].index)
df.to_csv('C:/Python/Email Reports/CF IN 1124.csv') 
