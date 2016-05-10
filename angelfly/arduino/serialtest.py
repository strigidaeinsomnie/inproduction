import serial
import time

ser = serial.Serial()
ser.baudrate = 9600
ser.port = 2 # COM3->2,COM5->4
ser.open()
time.sleep(1)

if ser.isOpen():
  ser.write("1")
ser.close()
