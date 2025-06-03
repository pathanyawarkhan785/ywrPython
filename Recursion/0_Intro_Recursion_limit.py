import sys

print(sys.getrecursionlimit())  # 1000 default
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())  # updated to 2000

count = 0


def recursion():
    global count

    if count > 1500:
        return

    count += 1
    print(count)
    recursion()


recursion()
