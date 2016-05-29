import random

def findsentence(arg1) :
    print(arg1)

    if arg1 == None :
        return None

    else :
        sentence = random.choice(arg1)
        return sentence
