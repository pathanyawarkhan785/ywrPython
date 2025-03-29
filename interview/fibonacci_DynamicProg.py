def fibDp(num):

    fibList = [0, 1]
    sum = 1

    for _ in range(num - 2):
        fibList.append(fibList[-1] + fibList[-2])
        sum += fibList[-1]

    print(fibList)
    print(sum)


fibDp(8)
