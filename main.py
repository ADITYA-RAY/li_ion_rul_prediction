import serial
import csv
from datetime import datetime
import os

ser = serial.Serial('/dev/ttyACM0', 9600)
csv_filename = "arduino_data.csv"

# Check if the CSV file already exists
write_headers = not os.path.isfile(csv_filename)

with open(csv_filename, mode='a', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)

    # Write headers only if the file is being created
    if write_headers:
        csv_writer.writerow(["Timestamp", "Voltage (V)", "Current (A)", "Mode"])

    try:
        while True:
            try:
                line = ser.readline().decode().strip()
                voltage, current, status = map(float, line.split(','))
                mode = "Charging" if status else "Discharging"

                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                csv_writer.writerow([timestamp, voltage, current, mode])
                csv_file.flush()

                print(f"{timestamp}: Voltage: {voltage} V, Current: {current} A, Mode: {mode}")

            except KeyboardInterrupt:
                print("Data logging stopped by the user.")
                break

    except KeyboardInterrupt:
        print("Data logging and CSV writing stopped by the user.")

ser.close()
