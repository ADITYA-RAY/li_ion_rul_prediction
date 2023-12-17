import serial
from datetime import datetime
import time
from database import create_db, insert_to_instant_db, close_db, get_prev_mode
create_db()
from soc import get_soc
# from cycle_data import cycle_calculations
import requests
from variables import uri


def fetch_status():
    url = "http://192.168.1.8:5000/api/state"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return "Charging" if data[0][1] else "Discharging"  
    else:
        print("Failed to fetch data. Status code:", response.status_code)
        print("Response content:", response.text)

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600)
    while True:
        try:
            line = ser.readline().decode().strip()
            print(line)
            voltage, current, temperature, status = map(float, line.split(','))

            prev_mode = get_prev_mode()
            if prev_mode == None:
                prev_mode = 0
            # print(prev_mode, int(status))
            # cycle = 1 if prev_mode and not int(status) else 0
            # if cycle:
            #     print("hello")
            # # if cycle as completed do feature calculation
            #     cycle_data = cycle_calculations()
            # # insert cycle data row to database
            #     insert_to_cycle_db(cycle_data)
            
            # measuring the soc
            soc = get_soc(status,current)
            timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

            # inserting instantaenous data to database
            insert_to_instant_db(timestamp,voltage,current,temperature,soc,status)
            # print(f"{timestamp}: Voltage: {voltage} V, Current: {current} A, Temperature: {temperature}, Mode: {status}")
            # check if cycle has completed


            # communicate form python to arduino
            command = fetch_status()
            ser.write(command.encode('utf-8'))

            time.sleep(10)

        except KeyboardInterrupt:
            print("Communication Breaked!")
            break
            
    ser.close()
    close_db()