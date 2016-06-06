#-------------------------------------------------------

from linklist import *
from choicelink import *
from fathermake import *
from xhtmlopen import *
from washxhtml import *
from findsentence import *
from dustshoot import *
from lamemoire import *
from findnum import *
from printnum import *

import time
import re
import serial

#-------------------------------------------------------

mother = 'http://www.aozora.gr.jp/'
fatherfront = ''
fatherrear = 'c'
keyinitial = 'index_pages/sakuhin'
keytitle = '../cards'
keyxhtml = '.files/'
keyxhtmlclass1 = 'div'
keyxhtmlclass2 = 'main_text'

initialfront = '"'
initialrear = '"'
titlefront = '/'
titlerear = '"'
xhtmlfront = '/'
xhtmlrear = '"'

linklists = None
links = None
linktitle = None
linklistxhtml = None
linkxhtml = None
xhtml = None
sentence = None
word = None

ser = serial.Serial(port = '/dev/ttyS0', baudrate = 9600)
clear = '\r\r'

intime = 0

#-------------------------------------------------------

while intime <= 10 :

    while word == None :

        while sentence == None :
            linklists = linklist(mother, keyinitial)
            links = choicelink(mother, linklists, initialfront, initialrear)

            linklists = linklist(links, keytitle)
            linktitle = choicelink(mother, linklists, titlefront, titlerear)

            father = fathermake(linktitle, fatherfront, fatherrear)

            linklistxhtml = linklist(linktitle, keyxhtml)


            while xhtml == None:
                linkxhtml = choicelink(father, linklistxhtml, xhtmlfront, xhtmlrear)

                xhtml = xhtmlopen(linkxhtml, keyxhtmlclass1, keyxhtmlclass2)


            washedxhtml = washxhtml(xhtml)

            text = dustshoot(washedxhtml)

            sentence = findsentence(text)

        else :
            word = lamemoire(sentence)

    else :
        listnums = findnum(word)
        printnum(listnums, ser)

        ser.write(clear.encode())
        ser.write(word.encode())
        ser.write(clear.encode())

        print(word)

        linklists = None
        links = None
        linktitle = None
        linklistxhtml = None
        linkxhtml = None
        xhtml = None
        sentence = None
        word = None

    time.sleep(5)
    intime += 1

#-------------------------------------------------------
