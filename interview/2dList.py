lst = [[1, 2], [3, 4]]

temp = 0


if lst[0][0] < lst[0][1]:
    temp = lst[0][0]
elif lst[0][1] < lst[0][0]:
    temp = lst[0][1]
elif lst[1][0] < lst[1][1] and lst[1][0] < temp:
    print(lst[1][0])
elif lst[1][1] < lst[1][0] and lst[1][1] < temp:
    print(lst[1][1])
else:
    print(temp)
