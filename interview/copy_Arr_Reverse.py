def copyAndReverse(arr):
    arrLen = len(arr)
    newArr = [0] * arrLen

    i = 0

    while i < arrLen:
        newArr[arrLen - 1 - i] = arr[i]
        i += 1

    print(newArr)


copyAndReverse([1, 2, 3, 4, 5])
