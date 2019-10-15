# Scrivere un decoratore di classe che decora una classe in modo tale che se la classe non contiene la funzione f
# allora viene invocata la funzione ff della MyClassFF


def decoratorMethodFF(cls):
    if getattr(cls, "f", None) is None:
        setattr(cls, "f", MyClassFF.ff)
        return cls


class MyClassFF:
    @classmethod
    def ff(cls):
        print("Hello!")


@decoratorMethodFF
class TestClass:
    pass


test = TestClass()
TestClass.f()
