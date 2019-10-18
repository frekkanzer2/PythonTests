class LinkedList:
    class Node:

        def __init__(self, value):
            self._element = value
            self._nextNode = None

        def setElement(self, value):
            self._element = value

        def getElement(self):
            return self._element

        def setNextNode(self, n):
            self._nextNode = n

        def getNextNode(self):
            return self._nextNode

    def __init__(self):
        self._head = None
        self._size = 0

    def addToHead(self, element):
        if element is not None:
            self._size += 1
            nodeToInsert = self.Node(element)
            oldHead = self._head
            self._head = nodeToInsert
            nodeToInsert.setNextNode(oldHead)

    def addToPosition(self, element, position):
        if element is not None:
            if position == 0:
                self.addToHead(element)
                return True
            elif position <= self._size:
                cycleNode = None
                for index in range(0, self._size):
                    if index == 0:
                        cycleNode = self._head
                    elif index == position:
                        actualNode = cycleNode.getNextNode()
                        nodeToInsert = self.Node(element)
                        cycleNode.setNextNode(nodeToInsert)
                        nodeToInsert.setNextNode(actualNode)
                        self._size += 1
                        return True
                    else:
                        cycleNode = cycleNode.getNextNode()
                return False
            else:
                return False

    def removeToHead(self):
        if self._size == 1:
            del self._head
            self._size = 0
        elif self._size > 1:
            oldHead = self._head
            self._head = oldHead.getNextNode()
            del oldHead
            self._size -= 1

    def removeToPosition(self, position):
        if position == 0:
            self.removeToHead()
            return True
        elif position < self._size:
            cycleNode = None
            for index in range(0, self._size):
                if index == 0:
                    cycleNode = self._head
                elif index == position:
                    actualNode = cycleNode.getNextNode()
                    cycleNode.setNextNode(actualNode.getNextNode())
                    del actualNode
                    self._size -= 1
                    return True
                else:
                    cycleNode = cycleNode.getNextNode()
            return False
        else:
            return False

    def getElementHead(self):
        return self._head.getElement()

    def getElementPosition(self, position):
        if position == 0:
            return self.getElementHead()
        elif position < self._size:
            cycleNode = None
            for index in range(0, self._size):
                if index == 0:
                    cycleNode = self._head
                elif index == position:
                    actualNode = cycleNode.getNextNode()
                    return actualNode.getElement()
                else:
                    cycleNode = cycleNode.getNextNode()
            return False
        else:
            return None

    def getSize(self):
        return self._size

    def output(self):
        stringToReturn = str()
        for index in range(0, self._size):
            if index == 0:
                cycleNode = self._head
                stringToReturn = stringToReturn + "" + cycleNode.getElement()
            else:
                cycleNode = cycleNode.getNextNode()
                stringToReturn = stringToReturn + " | " + cycleNode.getElement()
        return stringToReturn
