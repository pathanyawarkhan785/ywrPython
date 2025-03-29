num = int(
    input("Enter a number you want to check whether it is an Armstrong number or not: ")
)

newNum = str(num)
res = 0

for i in range(0, len(newNum)):
    res += int(newNum[i]) ** 3

if num == res:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
