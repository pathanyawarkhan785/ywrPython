strs = ["flower", "flow", "flight", "flop"]

strs.sort(key=len)
print(strs)

temp = strs[0]
newTemp = ""

j = 1

for i in range(0, len(strs[0])):
    if temp[i] == strs[j][i]:
        newTemp += temp[i]
        temp = temp.replace(temp, newTemp)
j += 1

print(newTemp)
