def isKthBitSet(num, k):

    mask = 1 << k

    if num & mask > 0:
        return True
    else:
        return False


# 1 0 1 1   <--  11 in binary                perform and(&) operation between num and mask
# 1 0 0 0   <--  1 << 3 == 8(decimal)
# 1 0 0 0   <--  ans is > 0 so 3rd bit is set(means 1)
# 3 2 1 0   <--  indexing work like this

print(isKthBitSet(11, 3))
