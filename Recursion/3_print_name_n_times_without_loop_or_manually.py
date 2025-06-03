def printName(n, name):
    if n == 0:
        return
    print(name)
    printName(n - 1, name)


n = int(input("Enter how many times you want to print your name: "))
printName(n, "yawar")
