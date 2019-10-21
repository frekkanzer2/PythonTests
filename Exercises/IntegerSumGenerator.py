def generator(number: int) -> list:
    myList = list()
    tempNumber = int(0)
    for i in range(number):
        tempNumber = i + tempNumber
        myList.append(tempNumber)
    return myList


print(generator(5))
