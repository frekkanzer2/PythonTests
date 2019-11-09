from ClassesModules.Observer import *


class MyState(Observer):
    def __init__(self, name, startValue=None):
        super().__init__()
        self.nameState = name
        self._value = startValue

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, newValue):
        self._value = newValue
        self.call_observer_all()


class MyListener(AbstractListener):
    def __init__(self, name):
        super().__init__(name)

    def observer_call(self, model):
        print(">> {} - {} has the following value: {}".format(self.name, model.nameState, model.value))


state = MyState("State A")
state.add_observer(MyListener("Listener A1"))
state.add_observer(MyListener("Listener B1"), MyListener("Listener B2"), MyListener("Listener B3"))
print("HERE SHOULD CALL ALL LISTENERS")
state.value = "CORRECT"
print("REMOVING LISTENERS...")
state.remove_observer_name("Listener B3")
state.remove_observer_name("Listener A1")
print("CALLING ONLY ONE LISTENER")
state.call_observer_name("Listener B2")
print("CALL ALL LISTENERS")
state.call_observer_all()
