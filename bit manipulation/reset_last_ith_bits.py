def reset(num, bit):
    mask = (~0) << bit

    num &= mask
    return num

    # 8 4 2 1
    # 1 1 1 1
    # 1 1 0 0


print(reset(15, 2))
