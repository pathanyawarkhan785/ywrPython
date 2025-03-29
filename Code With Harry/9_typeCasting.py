a = "1"
b = 2

# print(int(a) + int(b))
# print(a + b) # TypeError: can only concatenate str (not "int") to str

# implicit typecasting
# python converts smaller data type to higher datatype it's called implicit typecasting

c = 1.1  # higher datatype
d = 4  # lower datatype
res = c + d
print(type(res), res)  # here results automatically converts into higher datatype
