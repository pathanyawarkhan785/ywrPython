import random

# old javascript method for generate integer
num1 = int(random.random() * 100)
# print(num1)

# new python method for generate integer
num2 = random.randint(1, 6)  # here remember that 1 & 6 is also included
print(num2)
