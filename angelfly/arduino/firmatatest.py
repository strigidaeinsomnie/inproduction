from firmata import *

arduino = Arduino("/dev/ttyACM0",baudrate=57600) # 3 for COM4
arduino.pin_mode(13,firmata.OUTPUT)
arduino.delay(2)

while True:
    arduino.digital_write(13,firmata.HIGH)
    arduino.delay(3)
    arduino.digital_write(13,firmata.LOW)
    arduino.delay(3)
