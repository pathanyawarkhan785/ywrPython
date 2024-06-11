# str = "Hello World"

# print(str.lower())
# print(str.upper())


# str2 = "-----------Hello-------------World-----------"
# print("\n---------------------strip------------------------\n")
# # strip : removes any leading, and trailing whitespaces.

# print(str2.rstrip("-"))  # removes any leading, and trailing whitespaces from right.
# print(str2.lstrip("-"))  # removes any leading, and trailing whitespaces from left.
# print(
#     str2.strip("-")
# )  # removes any leading, and trailing whitespaces from both side but not from middle.

str3 = "hello mark, I am sr.mark."

# replace
# string.replace(oldvalue, newvalue, count)
# count: Optional. A number specifying how many occurrences of the old value you want to replace. Default is all occurrences.

# print(
#     str3.replace("mark", "james", 1)
# )  # here we selected 1 count so only 1 occurrences will be replaced.

# split
# string.split(separator, maxsplit)
# maxsplit	Optional. Specifies how many splits to do. Default value is -1, which is "all occurrences"
# The split() method splits a string into a list.

# print(
#     str3.split(" ", 2)
# )  # here 2 is maxsplit means from 2 spaces it will be splited after they combine whole word in 1 element.

# capitalize
# this method converts first character in upper case and the rest string in lower case.

# print(str3.capitalize())

# center
# string.center(length, character)
# character	Optional. The character to fill the missing space on each side. Default is " " (space)

# print(str3.center(100, "-"))

# count
# string.count(value, start, end)
# value	Required. A String. The string to value to search for
# start	Optional. An Integer. The position to start the search. Default is 0
# end	Optional. An Integer. The position to end the search. Default is the end of the string

# print(str3.count("mark", 0, 10))


# endsWith
# value	Required. The value to check if the string ends with
# start	Optional. An Integer specifying at which position to start the search
# end	Optional. An Integer specifying at which position to end the search

# print(str3.endswith("z"))
# print(str3.endswith("."))

# startsWith
# value	Required. The value to check if the string starts with
# start	Optional. An Integer specifying at which position to start the search
# end	Optional. An Integer specifying at which position to end the search

# print(str3.startswith("a"))
# print(str3.startswith("h"))

# find
# The find() method finds the first occurrence of the specified value.
# The find() method returns -1 if the value is not found.
# The find() method is almost the same as the index() method, the only difference is that the index() method raises an exception if the value is not found.
# value	Required. The value to search for
# start	Optional. Where to start the search. Default is 0
# end	Optional. Where to end the search. Default is to the end of the string

# print(str3.find("a"))
# print(str3.find("z")) # returns -1


# index

# print(str3.index("a"))
# print(str3.index("z"))  # throws error

# iselnum
# The isalnum() method returns True if all the characters are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9).
# Example of characters that are not alphanumeric: (space)!#%&? etc.

# print(str3.isalnum())

# isalpha
# The isalpha() method returns True if all the characters are alphabet letters (a-z).

# print(str3.isalpha())

# islower
# The islower() method returns True if all the characters are in lower case, otherwise False.
# Numbers, symbols and spaces are not checked, only alphabet characters.

# print(str3.islower())

# isprintable
# The isprintable() method returns True if all the characters are printable, otherwise False.

# str4 = "hello xyz\n"
# print(str4.isprintable())  # result false because \n is not printable.

# isspace
# The isspace() method returns True if all the characters in a string are whitespaces, otherwise False.

# str5 = "      "
# print(
#     str5.isspace()
# )  # if all the string is blank or having only blank spaces in string return true

# istitle
# The istitle() method returns True if all words in a text start with a upper case letter, AND the rest of the word are lower case letters, otherwise False.

# strTitle = (
#     "Hello james"  # "Hello James" -> return True -> because H & J is Capital here.
# )
# print(strTitle.istitle())  # it checks all the word's first character is capital or not.

# isupper
# The isupper() method returns True if all the characters are in upper case, otherwise False.

# strUpper = "HELLO Y"
# print(strUpper.isupper())

# swapcase
# The swapcase() method returns a string where all the upper case letters are lower case and vice versa.

# swapCase = "Hello James"
# print(swapCase.swapcase())

# title

# title = "hello james how are you"
# print(title.title())  # converts all the word's first character into capital letter.

# isnumeric
"""The isnumeric() method returns True if all the characters are numeric (0-9), otherwise False.
Exponents, like ² and ¾ are also considered to be numeric values.
"-1" and "1.5" are NOT considered numeric values, because all the characters in the string must be numeric, and the - and the . are not."""

txt = "121"
x = txt.isnumeric()
print(x)
