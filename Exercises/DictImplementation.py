from FunctionsModules.CheckTypes import checkIfString


class MyDictionary:
    class MyPair:
        def __init__(self, key: str, value):
            checkIfString(key)
            self.key = key
            self.value = value

        def getKey(self):
            return self.key

        def getValue(self):
            return self.value

        def setKey(self, newKey):
            self.key = newKey

        def setValue(self, newValue):
            self.value = newValue

    def __init__(self):
        self.instance = list()
        self._length = 0

    def __len__(self):
        return self._length

    def __setitem__(self, key, value):
        if self.__len__() == 0:
            tempPair = MyDictionary.MyPair(key, value)
            self.instance.append(tempPair)
        else:
            flag = False
            for item in self.instance:
                if item.getKey() == key:
                    flag = True
                    item.setValue(value)
                    break
            if flag is False:
                tempPair = MyDictionary.MyPair(key, value)
                self.instance.append(tempPair)
        self._length += 1

    def __getitem__(self, key):
        if self.__len__() == 0:
            return None
        else:
            toReturn = None
            for item in self.instance:
                if item.getKey() == key:
                    toReturn = item.getValue()
            return toReturn

    def __delitem__(self, key):
        if self.__len__() > 0:
            for item in self.instance:
                if item.getKey() == key:
                    del item
            self._length -= 1

    def __eq__(self, otherDictionary):
        if self.__len__() == 0 and otherDictionary.__len__() == 0:
            return True
        elif self.__len__() == otherDictionary.__len__():
            toReturn = True
            for index in range(0, self.__len__()):
                firstDictCouple = self.instance[index]
                secondDictCouple = otherDictionary.instance[index]
                if firstDictCouple.getKey() != secondDictCouple.getKey() or firstDictCouple.getValue() != secondDictCouple.getValue():
                    toReturn = False
                    break
            return toReturn
        else:
            return False

    def __contains__(self, key):
        if self.__len__() == 0:
            return False
        else:
            flag = False
            for item in self.instance:
                if item.getKey == key:
                    flag = True
                    break
            return flag
