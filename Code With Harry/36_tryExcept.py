# a = int(input("enter val: "))
# # b = [2, 7]

# try:
#     a = a + 2
#     print(a)
#     # print(b[a])

# except ValueError as err:
#     print(err)

# # except IndexError as err:
# #     print(err)

# # except TypeError as err:
# #     print(err)

# print("imp code needs to run.")

# ----------finally in python-------------


def func():
    try:
        a = int(input("enter val: "))
        print(a)
        return "try"

    except ValueError as err:
        print(err)
        return "except"

    # finally always execute it's code if code returned something still it returns.

    finally:
        print("this will always print.")

    print("this didn't print.")


y = func()
print(y)
