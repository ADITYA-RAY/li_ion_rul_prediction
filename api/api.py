import gspread
import time
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint as pp
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json",scope)
client = gspread.authorize(creds)

sheet = client.open("rul_data").sheet1
data = sheet.get_all_records() 
index = 0
while True:
    time.sleep(2)
    index+=1
    sheet.insert_row([index, 'new', 'new', 'new'],2)