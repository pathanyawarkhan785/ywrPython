print("1.Encrypt 2.Decrypt")
opt = int(input("enter your option : "))

if opt == 1:
    name = input("enter name to encrypt: ")

    if len(name) <= 3:
        name += name[0]
        name = name.replace(name[0], "", 1)
        print(name)

    else:
        print(name[::-1])
