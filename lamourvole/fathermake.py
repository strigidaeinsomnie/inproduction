def fathermake(arg1, arg2, arg3) :
    front = arg1.find(arg2)
    rear = arg1.rfind(arg3)
    return arg1[front:rear]
