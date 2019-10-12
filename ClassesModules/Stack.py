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

    # Add an element into the stack
    def addElement(self, element):
        if self.pvt_length == 0:
            self.pvt_lastNode = self.Node(element, None)
            self.pvt_length = 1
        else:
            tempNode = self.pvt_lastNode
            self.pvt_lastNode = self.Node(element, tempNode)
            self.pvt_length += 1

    # Get the last element of the stack
    def getElement(self):
        if self.pvt_length == 0:
            return None
        else:
            return self.pvt_lastNode.getElement()

    # Remove the last element of the stack
    def removeElement(self):
        if self.pvt_length > 0:
            tempPointer = self.pvt_lastNode.getSubNode()
            pointerToRemove = self.pvt_lastNode
            self.pvt_lastNode = tempPointer
            del pointerToRemove

    # Get the last element of the stack and remove it
    def getRemoveElement(self):
        if self.pvt_length > 0:
            nodeToReturn = self.getElement()
            self.removeElement()
            return nodeToReturn
        return None

    # Get the size of the stack
    def getDimension(self):
        return self.pvt_length
