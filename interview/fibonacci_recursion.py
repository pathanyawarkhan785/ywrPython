def fiboRec(num):
    if num <= 1:
        return num
    return fiboRec(num - 1) + fiboRec(num - 2)
    print(num)


print(fiboRec(6))
