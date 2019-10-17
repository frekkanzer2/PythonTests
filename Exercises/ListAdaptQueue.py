from ClassesModules.Queue import Queue
from ClassesModules.Stack import Stack


class MyAdapter(Queue):

    def __init__(self, instance):
        self.instance = instance

    def addElement(self, element):
        if isinstance(self.instance, list):
            self.instance.append(element)
        elif isinstance(self.instance, Stack):
            self.instance.addElement(element)

    def getElement(self):
        if isinstance(self.instance, list):
            return self.instance[len(self.instance) - 1]
        elif isinstance(self.instance, Stack):
            return self.instance.getElement()

    def getRemoveElement(self):
        if isinstance(self.instance, list):
            tempInst = self.instance[len(self.instance) - 1]
            del self.instance[len(self.instance) - 1]
            return tempInst
        elif isinstance(self.instance, Stack):
            return self.instance.getRemoveElement()


myQueue = Queue()
myList = list()
myStack = Stack()
listAdapter = MyAdapter(myList)
stackAdapter = MyAdapter(myStack)
itemList = [myQueue, listAdapter, stackAdapter]
itemList[0].addElement("Hello")
itemList[1].addElement("Another")
itemList[2].addElement("World")
itemList[1].addElement("Ups")
itemList[1].getRemoveElement()
for i in range(0, 3):
    print(itemList[i].getElement())
