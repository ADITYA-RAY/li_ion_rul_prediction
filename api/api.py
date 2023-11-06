import gspread
import time
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint as pp

import serial
from datetime import datetime

ser = serial.Serial('/dev/ttyACM0', 9600)

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json",scope)
client = gspread.authorize(creds)

sheet = client.open("rul_data").sheet1
data = sheet.get_all_records() 

try:
        while True:
            try:
                line = ser.readline().decode().strip()
                voltage, current, temperature, status = map(float, line.split(','))
                mode = "Charging" if status else "Discharging"

                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                sheet.insert_row([timestamp, voltage, current, temperature, mode],2)




            except KeyboardInterrupt:
                print("Data logging stopped by the user.")
                break

except KeyboardInterrupt:
        print("Data logging and CSV writing stopped by the user.")
