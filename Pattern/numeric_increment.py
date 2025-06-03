def numericPat(num):
    val = 1

    for i in range(1, num + 1):
        for j in range(i):
            print(val, end=" ")
            val += 1
        print("")


numericPat(5)

# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
