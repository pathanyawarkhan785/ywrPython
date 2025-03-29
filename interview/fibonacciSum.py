def fib(num):
    first = 0
    second = 0
    sum = 1

    if num <= 0:
        return 0

    curr = 1
    for i in range(1, num):
        first = second
        second = curr
        curr = first + second
        sum += curr
    return sum


# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144

print(fib(5))
