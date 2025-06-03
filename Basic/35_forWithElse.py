# when using loop with else statement, if condition will be satisfied then else is not executed.
# if loop finished just like print 1 to 10 then else will be printed.

# for i in range(1, 6):
#     print(i)

# else:
#     print("loop finished.")

# for i in range(1, 6):
#     print(i)
#     if i == 3:
#         break

# else:
#     print("this will not executed.")

# same with while loop

# i = 1
# while i < 6:
#     print(i)
#     i = i + 1

# else:
#     print("this will be executed.")

i = 1
while i < 6:
    print(i)
    i = i + 1
    if i == 3:
        break

else:
    print("this will not executed.")
