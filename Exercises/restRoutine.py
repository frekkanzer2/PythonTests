from FunctionsModules.Decorators import coroutine


@coroutine
def myRestCoroutine(numb):
    while True:
        value = (yield)
        if value % numb == 0:
            print("Ok")
        else:
            print("ERROR")


instanceCoroutine = myRestCoroutine(2)
instanceCoroutine.send(10)
instanceCoroutine.send(6)
instanceCoroutine.send(7)
instanceCoroutine.send(4)
instanceCoroutine.send(13)
