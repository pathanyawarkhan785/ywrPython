def revNum(num):
    if num == 0:
        return
    print(num)
    revNum(num - 1)


revNum(10)
