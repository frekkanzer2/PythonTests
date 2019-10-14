class Borg:
    _varDict = {}

    def __new__(cls, *args, **kwargs):
        # Create an object that it will be returned
        objToReturn = super().__new__(cls, *args, **kwargs)
        # Changing variables' dict
        objToReturn.__dict__ = cls._varDict
        # Returning the new object
        return objToReturn
