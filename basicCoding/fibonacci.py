# 0 , 1 , 1 , 2 , 3 , 5 , 8 , 13 , 21 , 34 , 55
first = 0
second = 1

num = int(input("Enter how many numbers you want to print: "))

if num < 1:
    raise "kindly enter correct number."
elif num == 1:
    print(f"{first}")
elif num == 2:
    print(f"{second}")
else:
    print(f"{first}")
    print(f"{second}")
    for i in range(0, num - 2):
        res = first + second
        print(f"{res}")
        first = second
        second = res
