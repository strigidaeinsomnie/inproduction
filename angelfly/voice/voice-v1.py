#-------------------------------------------------------

from linklist import *
from choicelink import *
from fathermake import *
from xhtmlopen import *
from washxhtml import *
from findsentence import *
from dustshoot import *
from lamemoire import *
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

xhtml = None
sentence = None

ser = serial.Serial(port = '/dev/ttyAMA0', baudrate = 9600)

#-------------------------------------------------------

while sentence == None :
    linklistinitial = linklist(mother, keyinitial)
    linkinitial = choicelink(mother, linklistinitial, initialfront, initialrear)

    linklisttitle = linklist(linkinitial, keytitle)
    linktitle = choicelink(mother, linklisttitle, titlefront, titlerear)

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
    word += '\r'
    wordprint = word.encode()

ser.write(wordprint)

#-------------------------------------------------------
