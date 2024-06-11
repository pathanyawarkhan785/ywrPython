num = int(input("Enter from how many numbers of sum you want: "))
sum = 0

if num < 1:
    raise ("Number can not be negative or zero.")


while num >= 0:
    sum += num
    num -= 1

print(sum)
