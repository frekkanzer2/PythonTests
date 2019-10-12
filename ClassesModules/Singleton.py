class Singleton:
    # Storage for the instance
    _instance = None

    # Constructor
    def __init__(self, Class, *params):
        # _instance is a class variable
        if Singleton._instance is None:
            Singleton._instance = Class(*params)

    # Getting an attribute of _instance
    def __getattr__(self, attr):
        return getattr(self._instance, attr)

    # Setting an attribute of _instance
    def __setattr__(self, attr, newValue):
        return setattr(self._instance, attr, newValue)

    # Getting the singleton id
    def getid(self):
        return id(self._instance)

