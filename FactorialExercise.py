def myFactorial(n: int):
    if n == 0:
        return 1
    else:
        return n * myFactorial(n-1)


myNumber = 5  # change here the test number
print(myFactorial(myNumber))
