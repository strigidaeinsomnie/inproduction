point = 10
lines = 0

def printpoint() :
    while lines < point :
        lines = len(open('lamourvole.txt').readlines())
        print(lines)
        return lines
