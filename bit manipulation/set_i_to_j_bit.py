def setItoJ(num, i, j):
    mask = ((1 << (j - i + 1)) - 1) << i
    num |= mask
    print(num)


setItoJ(24, 0, 2)
