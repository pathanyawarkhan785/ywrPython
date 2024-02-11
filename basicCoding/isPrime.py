a = 412

if a == 1:
    print("1 is not a prime number.")

if a > 1:
    for i in range(2, a):
        if a % i == 0:
            print(f"{a} is not a prime number.")
            break
    else:
        print(f"{a} is a prime number.")
