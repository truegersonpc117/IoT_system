import socket
import serial
import time

ms=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ms.connect(('192.168.0.19', 9800))

arduino = serial.Serial(port='COM3', baudrate=9600, timeout=.1)
arduino.flushInput()

while True:
    try:
        ser_bytes=arduino.readline()
        print(ser_bytes)
        ms.sendall(ser_bytes)

    except KeyboardInterrupt:
        ms.close()