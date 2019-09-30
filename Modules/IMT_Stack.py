class Stack:

    pvt_lastNode = None
    pvt_length = None

    class Node:
        pvt_element = None
        pvt_subNode = None

        def __init__(self, element, subNode):
            self.pvt_element = element
            self.pvt_subNode = subNode

        def getElement(self):
            return self.pvt_element

        def getSubNode(self):
            return self.pvt_subNode

    def __init__(self):
        self.pvt_lastNode = None
        self.pvt_length = 0

    def addNode(self, element):
        if self.pvt_length == 0:
            self.pvt_lastNode = self.Node(element, None)
            self.pvt_length = 1
        else:
            tempNode = self.pvt_lastNode
            self.pvt_lastNode = self.Node(element, tempNode)
            self.pvt_length += 1

    def getNode(self):
        if self.pvt_length == 0:
            return None
        else:
            return self.pvt_lastNode

    def removeNode(self):
        if self.pvt_length > 0:
            tempPointer = self.pvt_lastNode.getSubNode()
            pointerToRemove = self.pvt_lastNode
            self.pvt_lastNode = tempPointer
            del pointerToRemove

    def getRemoveNode(self):
        nodeToReturn = self.getNode()
        self.removeNode()
        return nodeToReturn

    def getDimension(self):
        return self.pvt_length
