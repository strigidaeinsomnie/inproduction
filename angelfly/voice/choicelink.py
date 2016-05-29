import random

def choicelink(arg1, arg2, arg3, arg4) :
    print(arg2)

    if arg2 == None :
        return None

    else :
        prelink = str(random.choice(arg2))
        front = prelink.find(arg3) + 1
        rear = prelink.rfind(arg4)
        slicedlink = prelink[front:rear]
        return arg1 + slicedlink
