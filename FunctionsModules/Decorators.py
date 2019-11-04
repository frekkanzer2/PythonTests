def coroutine(decoratedFunction):
    def wrapper(*args, **kwargs):
        generator = decoratedFunction(*args, **kwargs)
        next(generator)
        return generator
    return wrapper
