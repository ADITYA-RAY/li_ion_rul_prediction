import serial
import time
from serial_communication import writeToSerial
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)

def relayControl(command):
    writeToSerial(command)

