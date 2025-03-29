str = "james"

# all the results are same
# str[0] -- str[4]
# print(str[0:5])
# print(str[0:])  # py interpretor automatically takes len(str) after :
# print(str[::1])  # here py interpretor automatically takes 0 before : & len(str) after :

# negative slicing
# here if you take negative indices py interpretor adds its length to this indices and do slicing
# just like in this example str[-4+5=1:-2+5=3] -> str[1:3] -> am

print(str[-4:-2])
