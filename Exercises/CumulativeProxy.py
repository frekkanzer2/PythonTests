class MyClass:
    # direct invocation
    def f(self, a=None):
        print("TestF")

    # queue invocation
    def g(self, x=None, y=None):
        print("TestG")

    # queue invocation
    def create(self):
        print("TestCreate")

    # flush invocation
    def finalize(self):
        print("TestFinalize")


class MyProxy:
    def __init__(self, instance):
        self._instance = instance
        self.queue = list()

    # direct invocation
    def f(self, a=None):
        self._instance.f()

    # queue invocation
    def g(self, x=None, y=None):
        self.queue.append(self._instance.g)

    # queue invocation
    def create(self):
        self.queue.append(self._instance.create)

    # flush invocation
    def finalize(self):
        self._instance.finalize()
        for funct in self.queue:
            funct()


test = MyProxy(MyClass())
test.f()
test.g()
test.create()
test.g()
test.finalize()

