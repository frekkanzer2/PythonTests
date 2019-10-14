class Adapter:
    def __init__(self, obj, dictMethods):
        self.obj = obj
        self.__dict__.update(dictMethods)
