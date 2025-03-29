def sum_prefix(lst):

    for i in range(1, len(lst)):
        lst[i] += lst[i - 1]

    print(lst)


sum_prefix([10, 20, 10, 5, 15])
