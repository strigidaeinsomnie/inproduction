from bs4 import BeautifulSoup
import urllib2

def xhtmlopen(arg1, arg2, arg3) :
    html = urllib2.urlopen(arg1)
    soup = BeautifulSoup(html, 'lxml')
    return soup.find(arg2,{arg3})
