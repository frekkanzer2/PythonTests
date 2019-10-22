def decoratorFactory(myMethod):
    def decoratorClass(Cls):
        Cls._counter = 0

        def getCounter(self):
            return getattr(self, "_counter", None)

        def incrementCounter(self):
            setattr(self, "_counter", self.getCounter() + 1)

        def newMethod(self, *args, **kwargs):
            incrementCounter(self)
            myMethod(*args, **kwargs)

        setattr(Cls, "getCounter", getCounter)
        setattr(Cls, myMethod.__name__, newMethod)

        return Cls
    return decoratorClass


def test(value):
    print("Hello", value)


@decoratorFactory(test)
class MyClass:
    pass


myItem = MyClass()
myItem.test(5)
myItem.test(8)
print(myItem.getCounter())
