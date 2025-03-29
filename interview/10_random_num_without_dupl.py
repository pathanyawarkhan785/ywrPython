import random


def randomNum(num):
    lst = []
    while len(lst) < num:
        val = int((random.random() * num) + 1)
        if val not in lst:
            lst.append(val)

    return lst


print(randomNum(10))
