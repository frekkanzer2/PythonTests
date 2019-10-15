# Scrivere la classe MyClass il cui metodo statico addMethod prende in input un parametro funzione e se e' diverso
# da None inserisce nella classe un metodo f uguale alla funzione


class MyClass:
    @staticmethod
    def addMethod(method):
        if method is not None:
            MyClass.f = method


def myHello():
    print("Hello")


MyClass.addMethod(myHello)
MyClass.f()
