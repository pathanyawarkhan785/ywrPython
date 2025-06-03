num = 799


def func(num):
    for i in range(3):
        temp = num % 10
        print(num)
        if temp < 7 and temp > 0:
            return False
        num //= 10
    return True


print(func(num))
