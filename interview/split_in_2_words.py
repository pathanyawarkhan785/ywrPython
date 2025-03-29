def splitTwo(newStr):

    newStr = newStr.split()
    newList = []

    for i in range(0, len(newStr)):
        if i % 2 == 0:
            newList.append(newStr[i + 1])
        else:
            newList.append(newStr[i - 1])

    return " ".join(newList)


print(splitTwo("i love my india"))

# input:- i love my india
# output:- love i india my
