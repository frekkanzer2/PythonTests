from FunctionsModules.Decorators import coroutine


@coroutine
def handler_one(successor=None):
    while True:
        request = (yield)
        if 1 <= request <= 10:
            print("Gestito da ConcreteHandlerOne, richiesta {}".format(request))
        elif successor is not None:
            successor.send(request)


@coroutine
def handler_two(successor=None):
    while True:
        request = (yield)
        if 2 <= request <= 20:
            print("Gestito da ConcreteHandlerTwo, richiesta {}".format(request))
        elif successor is not None:
            successor.send(request)


@coroutine
def handler_three(successor=None):
    while True:
        request = (yield)
        if 3 <= request <= 30:
            print("Gestito da ConcreteHandlerThree, richiesta {}".format(request))
        elif successor is not None:
            successor.send(request)


@coroutine
def handler_default():
    while True:
        request = (yield)
        print("Non c'è un handler. La richiesta {} non può essere soddisfatta.".format(request))


class Client:
    """Client: Uses handlers"""

    def __init__(self):
        """Create the sequence of handlers that you want the requests to follow, and assign the sequence to
           local variable "handle"."""
        self.chain = handler_one(handler_two(handler_three(handler_default())))

    def delegate(self, r):
        """Iterates over requests and sends them, one by one, to handlers as per sequence of handlers
           defined above."""
        for i in r:
            self.chain.send(i)


# Create a client object
clientOne = Client()

# Create requests to be processed.
requests = [6, 12, 24, 18, 30, 40]

# Send the requests one by one, to handlers as per sequence of handlers defined in the Client class.
clientOne.delegate(requests)

"""Il programma deve stampare:
This is ConcreteHandlerOne handling request '6'
This is ConcreteHandlerTwo handling request '12'
This is ConcreteHandlerThree handling request '24'
This is ConcreteHandlerTwo handling request '18'
This is ConcreteHandlerThree handling request '30'
This is DefaultHandler telling you that request '40' has no handler right now.
"""
