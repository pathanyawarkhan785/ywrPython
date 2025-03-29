def resetIthBitToZero(num, k):

    mask = 1 << k
    num ^= mask

    return num


print(resetIthBitToZero(11, 3))
