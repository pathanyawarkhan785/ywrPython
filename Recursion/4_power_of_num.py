def powerOfNum(num, pow):

    if pow <= 0:
        return 1

    return num * powerOfNum(num, pow - 1)


print(powerOfNum(2, 5))
