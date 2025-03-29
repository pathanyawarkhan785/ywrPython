def setBit(num, k):
    mask = 1 << k
    num = num | mask
    return num


# 1 0 1 1   <--  11 in binary                perform or(|) operation between num and mask
# 0 1 0 0   <--  1 << 2 == 4(decimal)
# 1 1 1 1   <--  ans is > 0 so 3rd bit is set(means 1)
# 3 2 1 0   <--  indexing work like this


print(setBit(11, 2))
