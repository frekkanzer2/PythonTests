from FunctionsModules.CheckTypes import checkIfCustom
from FunctionsModules.Decorators import abstractMethod


# You should create a class that extends AbstractListener
class AbstractListener:
    # You have to implement observer_call
    def __init__(self, name="%listener_empty_name%"):
        self._liName = name

    @abstractMethod
    def observer_call(self, model):
        pass

    @property
    def name(self):
        return self._liName


# You should create a class that extends Observer
class Observer:
    # You subclass must call super().__init__()
    def __init__(self):
        self.listeners = []

    def add_observer(self, listener, *otherListeners) -> bool:
        listOfListeners = [listener]
        for obs in otherListeners:
            listOfListeners.append(obs)
        for obs in listOfListeners:
            try:
                checkIfCustom(obs, AbstractListener)
            except ValueError:
                return False
            self.listeners.append(obs)
            obs.observer_call(self)
        return True

    def remove_observer(self, listener) -> bool:
        if self.listeners.__contains__(listener):
            self.listeners.remove(listener)
            return True
        return False

    def remove_observer_all(self):
        for item in self.listeners:
            self.listeners.remove(item)

    def remove_observer_name(self, name):
        for item in self.listeners:
            if item._liName == name:
                self.listeners.remove(item)
                break

    # call this function when you have to active all listeners
    def call_observer_all(self):
        for obs in self.listeners:
            obs.observer_call(self)

    # call this function when you have to active only one listener
    def call_observer(self, listener):
        if self.listeners.__contains__(listener):
            for item in self.listeners:
                if item == listener:
                    item.observer_call(self)
                    break

    # call this function when you have to active only one listener
    def call_observer_name(self, name):
        for item in self.listeners:
            if item._liName == name:
                item.observer_call(self)
                break



