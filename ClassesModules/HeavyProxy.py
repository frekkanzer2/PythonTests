class HeavyProxy:
    def __init__(self, cls, *args):
        self._object = cls(*args)
        self._params = list()

    def __getattr__(self, attrName):
        return getattr(self._object, attrName, None)

    def callMethod(self, methodName, *args):
        callingMethod = getattr(self._object, methodName, None)
        self._params.append((callingMethod, *args))

    def execute(self):
        for itemMethod in self._params:
            callingMethod, *methodParams = itemMethod
            callingMethod(*methodParams)
