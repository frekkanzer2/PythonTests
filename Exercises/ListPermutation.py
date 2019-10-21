from itertools import permutations
from FunctionsModules.CheckTypes import checkIfInt


def listPermutation(myList: list) -> list:
    for element in myList:
        checkIfInt(element)
    listToReturn = permutations(myList)
    return list(listToReturn)


aList = [1, 2, 3]
print(aList)
newList = listPermutation(aList)
print(newList)
print(len(newList))
