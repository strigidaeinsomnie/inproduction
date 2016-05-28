from bs4 import BeautifulSoup
import urllib.request

def xhtmlopen(arg1, arg2, arg3) :
    html = urllib.request.urlopen(arg1)
    soup = BeautifulSoup(html, 'lxml')
    return soup.find(arg2,{arg3})
