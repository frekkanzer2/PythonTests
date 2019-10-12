# Create a script that counts the instances of a Class


class Counter:
    numberOfInstances = 0

    @classmethod
    def newInstance(cls):
        cls.numberOfInstances += 1

    @classmethod
    def getNumberOfInstances(cls):
        return cls.numberOfInstances

    def __init__(self):
        self.newInstance()


first = Counter()
second = Counter()
third = Counter()
fourth = Counter()
print(first.getNumberOfInstances())
