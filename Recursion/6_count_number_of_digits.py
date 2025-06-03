def countDigits(num):
    if num <= 0:
        return 0

    return 1 + countDigits(num // 10)


num = 47982
print(countDigits(num))
