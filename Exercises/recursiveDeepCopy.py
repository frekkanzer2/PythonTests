# Test cases:
#   [1, 2, 3]
#   [1, [2, 3]]
#   [[1, 2], [3, 4]]


def recursiveDeepCopy(myList: list):
    newList = list()
    for element in myList:
        if not isinstance(element, list):
            newList.append(element)
        else:
            tempList = recursiveDeepCopy(element)
            newList.append(tempList)
    return newList


aList = [3, [4, 5], [6, 7, [8]]]
bList = recursiveDeepCopy(aList)
print(bList)
