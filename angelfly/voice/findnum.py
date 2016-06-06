import re

pattern1 = re.compile(b'.')
pattern2 = re.compile('[0-9]')

def findnum(arg1) :
    listnums = []
    listwords = pattern1.findall(arg1.encode())

    while len(listwords) > 0 :
        chara = str(listwords[0])
        listwords = listwords[1:]

        num = pattern2.findall(chara)

        while len(num) > 1 :
            listnums.append(num[0])
            num = num[1:]

        num.append(0)
        listnums.append(num[0])

    return listnums
