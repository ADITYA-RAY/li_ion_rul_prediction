import serial
from datetime import datetime
import time
from database import create_db, insert_to_instant_db, close_db, get_prev_mode
create_db()
from soc import get_soc
from cycle_data import cycle_calculations

ser = serial.Serial('/dev/ttyACM0', 9600)

while True:
    try:
        line = ser.readline().decode().strip()
        voltage, current, temperature, status = map(float, line.split(','))

        # measuring the soc
        soc = get_soc(mode,current)
        timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        # inserting instantaenous data to database
        insert_to_instant_db(timestamp,voltage,current,temperature,soc,status)
        print(f"{timestamp}: Voltage: {voltage} V, Current: {current} A, Temperature: {temperature}, Mode: {mode}")

        # check if cycle has completed
        prev_mode = get_prev_mode()
        if prev_mode == None:
            prev_mode = 0

        cycle = 1 if prev_mode and not mode else 0
        if cycle:
        # if cycle as completed do feature calculation
            cycle_data = cycle_calculations()
        # insert cycle data row to database
            insert_to_cycle_db(cycle_data)

        time.sleep(10)

    except KeyboardInterrupt:
        print("Communication Breaked!")
        break
        
ser.close()
close_db()