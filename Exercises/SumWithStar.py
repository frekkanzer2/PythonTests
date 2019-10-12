def customSum(*values: int):
    mySum = 0
    for i in values:
        mySum += i
    return mySum


valueList = [1, 2, 3, 4, 5]
outSum = customSum(*valueList)
print(outSum)
