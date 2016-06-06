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

#----------------------------------

html1 = urllib.request.urlopen(mother)
soup1 = BeautifulSoup(html1, 'lxml')
linklists1 = soup.find_all(href=re.compile(keyinitial))

prelink1 = str(random.choice(linklists1))
front1 = prelink1.find(initialfront) + 1
rear1 = prelink1.rfind(initialrear)
slicedlink1 = prelink1[front1:rear1]
links1 = mother + slicedlink1

print (links1)

html2 = urllib.request.urlopen(links)
soup2 = BeautifulSoup(html2, 'lxml')
linklists2 = soup.find_all(href=re.compile(keytitle))

prelink2 = str(random.choice(linklists2))
front2 = prelink2.find(titlefront) + 1
rear2 = prelink2.rfind(titlerear)
slicedlink2 = prelink2[front2:rear2]
links2 = mother + slicedlink2

print (links2)
