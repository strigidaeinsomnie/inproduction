import time
import serial

def printnum(arg1, arg2) :
    listnums = arg1

    for num in listnums :
        forprint = str(num) + '\r'
        arg2.write(forprint.encode())
