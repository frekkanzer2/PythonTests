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
