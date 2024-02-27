lst = [54, 34, 67, 34]

max = lst[0]

for i in range(1, len(lst)):
    if max < lst[i]:
        max = lst[i]

print(max)
