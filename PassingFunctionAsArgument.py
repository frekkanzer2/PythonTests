def mySum(a, b):
    return a + b


def mySub(a, b):
    if a >= b:
        return a - b
    else:
        return b - a


def operation(a, b, myFunct):
    return myFunct(a, b)


value = operation(5, 10, mySub)
print(value)
