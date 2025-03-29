a = int(input("enter val: "))

print(isinstance(a, int))

if a < 1 or a > 10:
    raise ValueError("Value must be between 1 to 10.")

else:
    print(a)
