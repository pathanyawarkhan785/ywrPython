list1 = [2, 6, 2, 5, 4, 9, 3]

# map
# with single iterators & lambda

# print(list(map(lambda x: x**2, list1)))

# with multiple iterators
# sum = lambda x, y: x + y

# val1 = [1, 2, 3]
# val2 = [4, 5, 6]

# mapVal = list(map(sum, val1, val2))
# print(mapVal)


# filter with lambda
# filterList = list(filter(lambda x: x > 3, list1))
# print(filterList)

# reduce
from functools import reduce

reduceList = reduce(lambda x, y: x - y, list1)
# our list is list1 = [2, 6, 2, 5, 4, 9, 3]
# so when we do x - y it work like this
# 2 - 6 = -4 then subtract 3rd value
# -4 - 2 = -6 then subtract 4th value
# -6 - 5 = -11 then subtract 5th value
# -11 - 4 = -15 then subtract 6th value
# -15 - 9 = -24 then subtract 7th value
# -24 -3 = -27 then subtract 8th value

# print(reduceList)

lst2 = [1, 2, 3, 4]
rList = reduce(lambda x, y: x + y, lst2)
print(rList)
