# list is mutable.

lst = [42, 56, 24, 87, 23]

# print(lst)

# why index starts from 0 ?

# print(lst[0])
# *(lst + 0) -> *(0th element address + 0) -> *(0 + 0) -> *(0) -> get value at adress 0.

# print(lst[2])
# *(lst + 2) -> *(0th element address + 2) -> *(0 + 2) -> *(2) -> get value at adress 2.

# list indexing(negative)
# print(lst[-3])  # lst[len(lst) + (-3)] -> lst[(5 + (-3))] -> lst[2] -> 24

# # list comprehension

# newLst = [i * i for i in range(1, 6) if (i % 2 == 0)]
# print(newLst)

# ifLst = ["new", "abc", "xyz", "pqr"]
# if "abc" in ifLst:
#     print("yes")
# else:
#     print("no")

# list methods

lstMethod = [4, 24, 21, 16, 54, 75, 23, 16, 21]

# append
# The append() method appends an element to the end of the list.

# lstMethod.append(100)
# print(lstMethod)

# sort
# The sort() method sorts the list ascending by default.
# sort(reverse=True) sorts the list descending

# sortList = [46, 324, 7, 123, 74, 342]
# sortList.sort()
# print(sortList)

# reverse

revStr = [14, 23, 64]
# 1st method
# print(revStr[::-1])

# 2nd method
# revStr.reverse()
# print(revStr)

# index
# The index() method returns the position at the first occurrence of the specified value.

# print(lstMethod.index(21))

# count

# print(lstMethod.count(16))  # -> 2

# copy

# copyList = [1, 2, 3, 4, 5]

# lst2 = copyList.copy()

# lst2[0] = 5

# print(lst2)
# print(copyList)

# insert

# insList = [1, 2, 3]
# insList.insert(2, 12)
# print(insList)

# extend

# mainList = [1, 2, 3]
# extendList = [4, 5, 6]

# mainList.extend(extendList)
# print(mainList)

# # pass by reference

# arr = [1, 2, 3]
# arr2 = arr
# arr2[0] = 7
# print(arr)
# print(arr2)

# pass by value

# arr = [1, 2, 3]
# arr2 = arr.copy()
# arr2[0] = 7
# print(arr)
# print(arr2)
