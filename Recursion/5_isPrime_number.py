def isPrime(num, i):

    if i <= 1:
        return 1

    if num % i == 0:
        return 0

    return isPrime(num, i - 1)


num = 11
res = isPrime(num, num - 1)

if res:
    print("Prime")
else:
    print("Not Prime")
