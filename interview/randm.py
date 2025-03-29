import random

lst = []

i = 1
while i <= 10:
    val = int(random.randint(1, 100))
    if val not in lst:
        lst.append(val)
        i += 1

print(lst)
