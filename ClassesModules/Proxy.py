class Proxy:
    def __init__(self, cls, *args):
        self._object = cls(*args)

    def __getattr__(self, attrName):
        return getattr(self._object, attrName, None)
