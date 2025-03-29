# Consider the set of integers {1, 2, 3, ...., 5000}. The number of integers that is divisible by neither 3 nor 4 is : [MN]\


count = 0

for i in range(1, 5001):
    if i % 3 != 0 and i % 4 != 0:
        count += 1
print(count)  # 2500
