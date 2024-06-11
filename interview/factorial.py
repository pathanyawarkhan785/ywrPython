num = int(input("Enter a number you want factorial: "))
fact = 1

if num < 0:
    print("factorial not possile for negative numbers.")
elif num == 0:
    print("factorial of 0 is 1.")
else:
    for i in range(1, num + 1):
        fact = fact * i
    print(f"factorial of {num} is {fact}.")
