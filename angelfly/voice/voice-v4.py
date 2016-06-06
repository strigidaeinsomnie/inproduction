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
count1 = 0
count2 = 0

#-------------------------------------------------------

while intime <= 10 :

    while word == None :

        while sentence == None :
            linklists = linklist(mother, keyinitial)
            links = choicelink(mother, linklists, initialfront, initialrear)

            linklists = linklist(links, keytitle)
            linktitle = choicelink(mother, linklists, titlefront, titlerear)

            father = fathermake(linktitle, fatherfront, fatherrear)

            if father == None :
                continue

            linklistxhtml = linklist(linktitle, keyxhtml)

            count1 += 1

            if count1 >= 5 :
                count1 = 0
                continue

            while xhtml == None:
                count += 1

                if count2 >= 5 :
                    count2 = 0
                    continue

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

    time.sleep(10)
    intime += 1

    count1 = 0
    count2 = 0

#-------------------------------------------------------
