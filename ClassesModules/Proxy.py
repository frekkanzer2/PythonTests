class Proxy:
    def __init__(self, cls):
        self.object = cls()

    def __getattr__(self, attrName):
        return getattr(self.object, attrName, None)
