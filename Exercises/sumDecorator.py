def myDecorator(function):
    def wrapper(argument: list):
        for i in range(len(argument)):
            if not isinstance(argument[i], int):
                argument[i] = int(argument[i])
        return function(*argument)
    return wrapper


@myDecorator
def mySum(*numbers):
    result = 0
    for item in numbers:
        result += item
    return result


myResult = mySum([3, "4", 5.2])
print("Result is", myResult)
