def find_second_largest(my_list):
    largest = second_largest = float("-inf")

    for num in my_list:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest:
            second_largest = num

    return second_largest


my_list = [10, 5, 8, 20, 15]
result = find_second_largest(my_list)
print(result)
