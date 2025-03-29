def setLast(num, bit):
    mask = (1 << bit) - 1
    num |= mask
    return num


# bit = 3 so we need to make last 3 bit to 1
# 1 1 0 0 1 0 -> 50(input)
# 1 1 0 1 1 1 -> 55(expected) last 3 bit set to 1


print(setLast(50, 3))
