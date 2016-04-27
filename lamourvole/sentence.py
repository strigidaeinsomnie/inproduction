#-------------------------------------------------------

from linklist import linklist
from choicelink import choicelink
from fathermake import fathermake
from xhtmlopen import xhtmlopen
from washxhtml import washxhtml
from findsentence import findsentence
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

    #print(linkinitial)

    linklisttitle = linklist(linkinitial, keytitle)
    linktitle = choicelink(mother, linklisttitle, titlefront, titlerear)

    #print(linktitle)

    father = fathermake(linktitle, fatherfront, fatherrear)

    linklistxhtml = linklist(linktitle, keyxhtml)


    while xhtml == None:
        linkxhtml = choicelink(father, linklistxhtml, xhtmlfront, xhtmlrear)
        #print(linkxhtml)

        xhtml = xhtmlopen(linkxhtml, keyxhtmlclass1, keyxhtmlclass2)


    washedxhtml = washxhtml(xhtml)
    #print(washedxhtml)

    #text = re.sub('\（[^\）]*\）', '', washedxhtml)
    #cleantext = re.sub('[\t\n\r\f\v]', 'kkk', text)
    #cleantext = re.sub('\u3000', '　', text)
    #Text = re.findall('「([^」]*)」', cleantext)

    #print(text)
    #print('Text == ', Text, len(Text))

    sentence = findsentence(washedxhtml)

else :
    print('sentence == ', sentence)
