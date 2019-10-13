# All methods in this library will raise an exception if the type of the value is not allowed


def checkIfString(value):
    if not isinstance(value, str):
        raise ValueError(value, "is not a string")


def checkIfInt(value):
    if not isinstance(value, int):
        raise ValueError(value, "is not an integer")


def checkIfFloat(value):
    if not isinstance(value, float):
        raise ValueError(value, "is not a float")


def checkIfBoolean(value):
    if not isinstance(value, bool):
        raise ValueError(value, "is not a boolean")


def checkIfList(value):
    if not isinstance(value, list):
        raise ValueError(value, "is not a list")


def checkIfTuple(value):
    if not isinstance(value, tuple):
        raise ValueError(value, "is not a tuple")


def checkIfSet(value):
    if not isinstance(value, set):
        raise ValueError(value, "is not a set")


def checkIfFrozenSet(value):
    if not isinstance(value, frozenset):
        raise ValueError(value, "is not a frozenset")


def checkIfDict(value):
    if not isinstance(value, dict):
        raise ValueError(value, "is not a dict")


def checkIfCustom(value, customType):
    if not isinstance(value, customType):
        raise ValueError(value, "is not an instance of", customType)
