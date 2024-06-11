def mostOccur(lst):
    maxCount = lst.count(lst[0])
    for i in lst:
        if lst.count(i) > maxCount:
            maxCount = i

    return maxCount


print(mostOccur([1, 2, 2, 4, 2, 7, 2, 2, 6]))
