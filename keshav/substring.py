myStr = "ABCDCDC"
subStr = "CDC"
start = 0
count = 0

for i in range(0, len(myStr)):
    x = myStr.find(subStr, start)
    if x != -1:
        start = x + 1
        count += 1

print(count)
