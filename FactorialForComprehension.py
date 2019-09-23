def myFactorial(n: int):
    """
        It returns the factorial of n
    """
    if n == 0:
        return 1
    else:
        return n * myFactorial(n-1)


rightValues = [myFactorial(i) for i in range(1, 11) if myFactorial(i) % 3 == 0]
print(rightValues)
