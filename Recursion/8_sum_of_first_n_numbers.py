def sumOfNnumbers(n):

    if n <= 0:
        return 0
    return n + sumOfNnumbers(n - 1)


print(sumOfNnumbers(10))
