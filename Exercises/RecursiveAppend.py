def recursiveAppend(myList: list, counter: int):
    if counter > 0:
        myObject = "a"
        myList.append(myObject)
    if counter == 0:
        return 0
    else:
        counter -= 1
        return recursiveAppend(myList, counter)


myCounter = 5  # change here the value
mainList = list()
recursiveAppend(mainList, myCounter)
print(mainList)
