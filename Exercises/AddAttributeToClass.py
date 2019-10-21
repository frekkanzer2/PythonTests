class EmptyClass:
    @classmethod
    def adderAttribute(cls, attrName: str, value) -> bool:
        if getattr(cls, attrName, None) is None:
            setattr(cls, attrName, value)
            return True
        else:
            return False


class EmptySubClass(EmptyClass):
    pass


item = EmptyClass()
print(item.adderAttribute("myAttr", 10))
print(item.adderAttribute("anotherAttr", 20))
print(item.adderAttribute("myAttr", 30))
anotherItem = EmptySubClass()
print(anotherItem.adderAttribute("helloAttr", 50))
print(anotherItem.adderAttribute("anotherAttr", 100))
