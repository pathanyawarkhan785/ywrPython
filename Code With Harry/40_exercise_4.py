name = input("enter name to encrypt: ")

if len(name) <= 3:
    name += name[0]
    name = name.replace(name[0], "", 1)
    print(name)

else:
    print(name[::-1])
