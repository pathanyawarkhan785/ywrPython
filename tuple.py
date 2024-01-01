# same as list but immutable
# same process as list like slicing

# tpl = (23, 56, 23, 74)
# tpl2 = tpl

# print(tpl)
# print(tpl2)

# if 23 in tpl:
#     print("present")
# else:
#     print("absent")


# tuple methods

tpl3 = (2, 31, 34, 4, 2, 3, 4, 2, 6, 2, 8)
# print(tpl3)

# count
# print(tpl3.count(2))

# index

"""in this line we are finding index for 2 so first we do slicing of -> 8 to len(tpl3) -> 8 to 11 ->
here 8 to 11 have this elements (6,2,8) now 2 is on 9th index so it returns 9."""


# indexTwo = tpl3.index(2, 8, len(tpl3))
# print(indexTwo)

# len

lenTpl = (3, 2, 4, 2, 4)
print(len(lenTpl))
