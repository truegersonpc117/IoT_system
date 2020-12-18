import serial
import time
arduino = serial.Serial(port='COM3', baudrate=9600, timeout=.1)
arduino.flushInput()

while True:
    try:
        ser_bytes=arduino.readline()
        print(ser_bytes)
    except:
        print("Keyboard interrupt")
        break
    