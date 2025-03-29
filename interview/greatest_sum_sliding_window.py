# finding max sum of subarray 4 using sliding window technique


def maxSum(lst, k):

    maxSum = 0
    currSum = 0
    lenOfLst = len(lst)

    for i in range(k):
        maxSum += lst[i]

    currSum = maxSum

    for i in range(k, lenOfLst):
        currSum = currSum - lst[i - k] + lst[i]
        if currSum > maxSum:
            maxSum = currSum

    print(maxSum)


maxSum([5, 8, 1, 2, 7, 4, 3], 4)
