class MyClass:
    counter = 0

    def functionDecorator(function):
        def wrapper(*args):
            MyClass.counter += 1
            return function(*args)
        return wrapper

    @functionDecorator
    def methodA(self):
        pass

    @functionDecorator
    def methodB(self):
        pass

    @functionDecorator
    def methodC(self):
        pass


item = MyClass()
print("Starting class counter =", item.counter)
item.methodA()
item.methodB()
print("Class item counter =", item.counter)
anotherItem = MyClass()
anotherItem.methodA()
anotherItem.methodB()
anotherItem.methodC()
print("Class another item counter =", anotherItem.counter)
