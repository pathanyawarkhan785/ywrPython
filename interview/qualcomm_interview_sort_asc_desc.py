def sortAscDsc(newStr):
    newStr = newStr.split(" ")
    newList = []

    for i in range(len(newStr)):
        if i % 2 == 0:
            newList.append("".join(sorted(newStr[i])))
        else:
            newList.append("".join(sorted(newStr[i], reverse=True)))

    return " ".join(newList)


print(sortAscDsc("cab cab cab cab"))
