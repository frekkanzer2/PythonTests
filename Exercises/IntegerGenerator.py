def generator(value: int) -> list:
    myList = list()
    for i in range(value):
        myList.append(i)
    return myList


totalList = [1, 8, 6, 5]
for index in range(len(totalList)):
    totalList[index] = generator(totalList[index])
print(totalList)
