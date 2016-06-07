#--------------------------------

from bs4 import BeautifulSoup
import random
import re
import serial
import time
import urllib.request

#--------------------------------

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

ser = serial.Serial(port = '/dev/ttyS0', baudrate = 9600)

sw1 = 0

#----------------------------------

while sw1 <= 5 :
    html1 = urllib.request.urlopen(mother)
    soup1 = BeautifulSoup(html1, 'lxml')
    linklists1 = soup1.find_all(href=re.compile(keyinitial))

    try :
        prelink1 = str(random.choice(linklists1))

    except ValueError :
        pass

    front1 = prelink1.find(initialfront) + 1
    rear1 = prelink1.rfind(initialrear)
    slicedlink1 = prelink1[front1:rear1]
    links1 = mother + slicedlink1

    print (links1) #--あいうえお選ぶ

    html2 = urllib.request.urlopen(links1)
    soup2 = BeautifulSoup(html2, 'lxml')
    linklists2 = soup2.find_all(href=re.compile(keytitle))

    prelink2 = str(random.choice(linklists2))
    front2 = prelink2.find(titlefront) + 1
    rear2 = prelink2.rfind(titlerear)
    slicedlink2 = prelink2[front2:rear2]
    links2 = mother + slicedlink2

    print (links2) #--作品選ぶ

    fatfront = links2.find(fatherfront)
    fatrear = links2.rfind(fatherrear)
    father = links2[fatfront:fatrear]

    print(father) #--リンクをたどる

    html3 = urllib.request.urlopen(links2)
    soup3 = BeautifulSoup(html3, 'lxml')
    linklists3 = soup3.find_all(href=re.compile(keyxhtml))

    prelink3 = str(random.choice(linklists3))
    front3 = prelink3.find(xhtmlfront) + 1
    rear3 = prelink3.rfind(xhtmlrear)
    slicedlink3 = prelink3[front3:rear3]
    linkxhtml = father + slicedlink3

    print(linkxhtml) #--ファイルにたどり着いた　zipの時がある

    html4 = urllib.request.urlopen(linkxhtml)
    soup4 = BeautifulSoup(html4, 'lxml')
    xhtml = soup4.find(keyxhtmlclass1, {keyxhtmlclass2})

    print(xhtml) #--本文を見つけた

    if xhtml == None : #--zipのときはやりなおし
        continue

    prewash = BeautifulSoup(str(xhtml), 'lxml')
    washed = prewash.get_text()

    print(washed)

    #-------------ここまでは失敗することないよ

    xhtml = None
    sw1 += 1
