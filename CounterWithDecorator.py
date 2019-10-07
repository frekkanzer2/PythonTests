# Create a counter class via decorator


def dec_counterClass(decoratedClass):
    decoratedClass.numberOfInstances = 0
    decoratedClass.oldInit = decoratedClass.__init__

    def moddedInit(self, *args, **kwargs):
        decoratedClass.numberOfInstances += 1
        decoratedClass.oldInit(self, *args, **kwargs)

    decoratedClass.__init__ = moddedInit

    return decoratedClass


@dec_counterClass
class Counter:
    var = 0


a = Counter()
b = Counter()
c = Counter()
print(a.numberOfInstances)
