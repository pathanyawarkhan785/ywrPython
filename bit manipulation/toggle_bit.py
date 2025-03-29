def toggle(num, toggleBit):

    mask = 1 << toggleBit
    return num ^ mask


print(toggle(10, 2))
