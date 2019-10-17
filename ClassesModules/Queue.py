class Queue:
    pvt_length = None
    pvt_startNode = None
    pvt_endNode = None

    class Node:
        pvt_element = None
        pvt_nextNode = None
        pvt_previousNode = None

        def __init__(self, nodeValue):
            self.setElement(nodeValue)

        def getElement(self):
            return self.pvt_element

        def setElement(self, value):
            self.pvt_element = value

    def __init__(self):
        self.pvt_length = 0
        self.pvt_startNode = None
        self.pvt_endNode = None

    def addElement(self, element):
        nodeToSet = self.Node(element)
        if self.pvt_length == 0:
            self.pvt_startNode = nodeToSet
            self.pvt_endNode = nodeToSet
        else:
            oldStartNode = self.pvt_startNode  # Taking old start node
            self.pvt_startNode = nodeToSet  # New start node is nodeToSet
            oldStartNode.pvt_nextNode = self.pvt_startNode
            self.pvt_startNode.pvt_previousNode = oldStartNode
        self.pvt_length += 1

    def getElement(self):
        if self.pvt_length == 0:
            return None
        else:
            return self.pvt_endNode.getElement()

    def removeElement(self):
        if self.pvt_length == 1:
            self.pvt_length = 0
            self.pvt_startNode = None
            self.pvt_endNode = None
        elif self.pvt_length > 1:
            self.pvt_length -= 1
            newEndNode = self.pvt_endNode.pvt_nextNode
            del self.pvt_endNode
            self.pvt_endNode = newEndNode
            newEndNode.pvt_previousNode = None

    def getRemoveElement(self):
        if self.pvt_length == 0:
            return None
        else:
            elementToReturn = self.getElement()
            self.removeElement()
            return elementToReturn

    def getSize(self):
        return self.pvt_length
