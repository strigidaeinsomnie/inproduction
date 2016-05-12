import serial
import serial.tools.list_ports

ser = serial.Serial()
ser.baudrate = 9600
ser.port = list(serial.tools.list_ports.comports())[0][0]
ser.open()
ser.write("Hello")
