beg = 18
end = 79

if beg < 1:
    print("Enter Correct stsrting.")

for num in range(beg, end + 1):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num)
