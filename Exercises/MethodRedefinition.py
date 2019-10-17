class Redefinition:
    class InnerClass:
        @classmethod
        def methodF(cls):
            print("Hello")

    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls, *args, **kwargs)
        obj.f = cls.InnerClass.methodF
        return obj


myObj = Redefinition()
myObj.f()
