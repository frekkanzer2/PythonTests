from FunctionsModules.Decorators import multiplexer


@multiplexer
class Switch:
    pass


mySwitch = Switch()
Switch.__printStatus(mySwitch)
Switch.changeStatus(mySwitch)
print(Switch.getStatus(mySwitch))
print(Switch.checkStatus(mySwitch, Switch.ON))
Switch.changeStatus(mySwitch)
Switch.__printStatus(mySwitch)
