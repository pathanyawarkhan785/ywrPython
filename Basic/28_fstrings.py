# old method

str = "hello {1} how's your {0}"
name = "abc"
part = "head"

print(str.format(part, name))

# new method for string literals

methodType = "new"
dataType = "string"
newStr = f"This is {methodType} method, for {dataType} literals."
print(newStr)
