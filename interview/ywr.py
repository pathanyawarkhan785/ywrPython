def secondLargest(num):

    max = float("-inf")
    secondMax = float("-inf")

    for i in range(len(num)):
        if num[i] > max:
            secondMax = max
            max = num[i]
        elif max > num[i] and secondMax < num[i]:
            secondMax = num[i]

    print(secondMax)


secondLargest([1, 2, 3, 45, 67, 10])
