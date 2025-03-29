import math

a = int(input("Enter num: "))

if a < 1:
    print("enter valid input.")

elif a == 1:
    print("1 is not a prime number.")

else:
    for i in range(2, math.ceil(math.sqrt(a))):
        if a % i == 0:
            print(f"{a} is not a prime number.")
            break
    else:
        print(f"{a} is a prime number.")
