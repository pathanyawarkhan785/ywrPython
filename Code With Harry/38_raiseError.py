a = input("enter val: ")

if a == "quit":
    print("quit")

elif int(a) < 1 or int(a) > 10:
    raise ValueError("value must be between 0 to 11.")

else:
    print(a)
