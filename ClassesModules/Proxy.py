class Proxy:
    def __init__(self, cls):
        self._object = cls()

    def __getattr__(self, attrName):
        return getattr(self._object, attrName, None)
