from bs4 import BeautifulSoup

def washxhtml(arg1) :
    prewash = BeautifulSoup(str(arg1), 'lxml')
    return prewash.get_text()
