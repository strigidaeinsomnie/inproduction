#--------------------------------

from bs4 import BeautifulSoup
import random
import re
import RPi.GPIO as GPIO
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

pattern1 = re.compile(b'.')
pattern2 = re.compile('[0-9]')

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
light = GPIO.PWM(12, 50)  # channel=12 frequency=50Hz
light.start(10)

ser = serial.Serial(port = '/dev/ttyAMA0', baudrate = 9600)
clear = '\r\r'

waitlight = 0.5
wait = 5
sw1 = 0

#----------------------------------

while sw1 <= 100 :
    xhtml = None

    html1 = urllib.request.urlopen(mother)
    soup1 = BeautifulSoup(html1, 'lxml')
    linklists1 = soup1.find_all(href=re.compile(keyinitial))

    try :
        prelink1 = str(random.choice(linklists1))
    except IndexError :
        continue

    front1 = prelink1.find(initialfront) + 1
    rear1 = prelink1.rfind(initialrear)
    slicedlink1 = prelink1[front1:rear1]
    links1 = mother + slicedlink1

    print (links1) #--あいうえお選ぶ

    html2 = urllib.request.urlopen(links1)
    soup2 = BeautifulSoup(html2, 'lxml')
    linklists2 = soup2.find_all(href=re.compile(keytitle))

    try :
        prelink2 = str(random.choice(linklists2))
    except IndexError :
        continue

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

    try :
        prelink3 = str(random.choice(linklists3))
    except IndexError :
        continue

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

    washin1 = re.sub('\（[^\）]*\）', '', washed)
    washin2 = re.sub('[\t\n\r\f\v]', '', washin1)
    washin3 = re.sub('\u3000', '　', washin2)
    text = re.findall('「([^」]*)」', washin3)

    print(text) #--ルビをとってかぎ括弧さがす

    try :
        sentence = random.choice(text)
    except IndexError :
        continue

    print(sentence) #--ことばを一つ選ぶ

    #------------------------------

    listnums = []
    listwords = pattern1.findall(sentence.encode())

    while len(listwords) > 0 :
        chara = str(listwords[0])
        listwords = listwords[1:]

        num = pattern2.findall(chara)

        while len(num) > 1 :
            listnums.append(num[0])
            num = num[1:]

        num.append(0)
        listnums.append(num[0])

    for printnum in listnums :
        numlight = int(printnum) * 10
        light.ChangeDutyCycle(numlight)
        print(numlight)
        time.sleep(waitlight)

    ser.write(sentence.encode())
    ser.write(clear.encode())

    #-----------------------------

    sw1 += 1
    time.sleep(wait)
