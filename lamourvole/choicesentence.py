import random

def choicesentence(arg1, arg2) :
    listsentence = random.shuffle(arg1)

    for sentence in listsentence :
        sentencelen = len(sentence)
        print(sentencelen)

        if sentencelen > arg2 :
            return sentence
            break

    else :
        return None
