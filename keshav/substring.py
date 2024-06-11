def count_substring(myStr, subStr):

    start = 0
    count = 0

    for i in range(0, len(myStr)):
        x = myStr.find(subStr, start)
        if x != -1:
            start = x + 1
            count += 1
    return count


print(count_substring("ABCDCDC", "CDC"))
