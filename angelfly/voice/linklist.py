from bs4 import BeautifulSoup
import re
import urllib2.request

def linklist(arg1, arg2) :
    html = urllib2.request.urlopen(arg1)
    soup = BeautifulSoup(html, 'lxml')
    return soup.find_all(href=re.compile(arg2))
