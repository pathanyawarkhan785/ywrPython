lst1 = [1, 4, 3, 2]
lst2 = [5, 4, 6, 7]

lst2 = set(lst2)


for i in lst1:
    if i in lst2:
        print(True)
    else:
        print(False)


def func(str):
    str = str.split(" ")

    for i in range(len(str)):

        if i % 2 == 0:
            str[i] = "".join(sorted(str[i]))

        else:
            str[i] = "".join(sorted(str[i], reverse=True))

    print(" ".join(str))


func("def xyz cba")


# input:- "def xyz cba"
# output:- "def zyx abc"
