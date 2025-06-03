names = ["abc", "pqr", "ywr"]
ages = [3, 13, 23]

newZip = list(zip(names, ages))
# print(newZip)

names, ages = zip(*newZip)

# print(list(names))
# print(list(ages))

for i, j in newZip:
    print(i, j)
