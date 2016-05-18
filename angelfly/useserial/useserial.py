import serial

ser = serial.Serial(baudrate = 9600, port = '/dev/ttyAMA0')
ser.open()

print(word, file = ser)
