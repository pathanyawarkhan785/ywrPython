# factorial code
# if function called itself is called a recursion.


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))

# fibonacci series


def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)


print(fibo(3))


# 0 , 1 , 1 , 2 , 3 , 5 , 8 , 13 , 21 , 34
