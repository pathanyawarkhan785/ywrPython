lst = [19, 26, 12, 15, 29, 17]

# method 1
print(lst[len(lst) - 1])

# method 2
print(lst[-1])  # for last element
print(lst[-2])  # for second last element & goes on

# method 3
lastElem = lst.pop()
print(lastElem)
