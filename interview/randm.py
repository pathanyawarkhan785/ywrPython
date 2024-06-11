import random

lst = []

for i in range(0, 10):
    lst.append(int(random.random() * 10))

print(list(set(lst)))
