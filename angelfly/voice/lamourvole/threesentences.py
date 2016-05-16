#-------------------------------------------------------

from linklist import linklist
from choicelink import choicelink
from fathermake import fathermake
from xhtmlopen import xhtmlopen
from washxhtml import washxhtml
from findsentence import findsentence
from dustshoot import dustshoot
from lamemoire import lamemoire
import re

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


f = open('lamourvole.txt', 'a')
f.write(word)
f.close()
#-------------------------------------------------------
