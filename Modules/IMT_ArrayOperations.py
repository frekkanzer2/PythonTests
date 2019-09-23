def arraySum(array: list):
    """
    Input: an array of integers
    Output: the sum of all elements
    """
    customSum = 0
    for i in array:
        customSum += i
    return customSum


def arrayMultiplication(array: list):
    """
    Input: an array of integers
    Output: the multiplication of all elements
    """
    customSum = 1
    for i in array:
        customSum *= i
    return customSum


def arrayFindMin(array: list):
    """
    Input: an array of integers
    Output: the minimum element
    """
    if len(array) == 0:
        return None
    else:
        customMin = array[0]
        if len(array) > 1:
            # case array's len > 1 -> search the min
            for index in range(1, len(array)):
                if array[index] <= customMin:
                    customMin = array[index]
            return customMin
        else:
            # case array's len = 1 -> the min is in the first position
            return customMin


def arrayFindMax(array: list):
    """
    Input: an array of integers
    Output: the maximum element
    """
    if len(array) == 0:
        return None
    else:
        customMax = array[0]
        if len(array) > 1:
            # case array's len > 1 -> search the max
            for index in range(1, len(array)):
                if array[index] >= customMax:
                    customMax = array[index]
            return customMax
        else:
            # case array's len = 1 -> the max is in the first position
            return customMax
