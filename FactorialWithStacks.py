from Modules.IMT_Stack import Stack


def myFactorial(n: int):
    if n == 0:
        return 1
    else:
        return n * myFactorial(n - 1)


myStack = Stack()
print("Insert 5 numbers from keyboard")
for i in range(0, 5):
    myStack.addNode(int(input("Insert: ")))
print("All factorials f%2==0 will be filtered")
newStack = Stack()
for i in range(0, 5):
    value = myStack.getRemoveNode().getElement()
    value = myFactorial(value)
    if value % 2 == 0:
        newStack.addNode(value)
if newStack.getDimension() > 0:
    print("Done! New stack will be displayed now:")
    for i in range(0, newStack.getDimension()):
        print(newStack.getRemoveNode().getElement())
else:
    print("No elements found")
