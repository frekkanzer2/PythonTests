def coroutine(decoratedFunction):
    def wrapper(*args, **kwargs):
        generator = decoratedFunction(*args, **kwargs)
        next(generator)
        return generator
    return wrapper


def abstractMethod(function):
    def wrapper(*args, **kwargs):
        raise NotImplementedError
    return wrapper


def multiplexer(decoratedClass):
    decoratedClass.ON = 1
    decoratedClass.OFF = 0
    decoratedClass.oldInit = decoratedClass.__init__

    def getStatus(mp):
        return mp.status

    def checkStatus(mp, status_toCheck):
        if mp.status == status_toCheck:
            return True
        else:
            return False

    def changeStatus(mp):
        if mp.status == decoratedClass.ON:
            mp.status = decoratedClass.OFF
        else:
            mp.status = decoratedClass.ON

    def __printStatus(mp):
        if mp.status == decoratedClass.ON:
            print("ON")
        else:
            print("OFF")

    def newInit(self, *args, **kwargs):
        self.status = decoratedClass.ON
        decoratedClass.oldInit(self, *args, **kwargs)

    decoratedClass.__init__ = newInit
    setattr(decoratedClass, "getStatus", getStatus)
    setattr(decoratedClass, "checkStatus", checkStatus)
    setattr(decoratedClass, "changeStatus", changeStatus)
    setattr(decoratedClass, "__printStatus", __printStatus)
    return decoratedClass
