# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists


# read

# f = open("IO\main.txt", "r")
# print(f.read())
# f.close()

# write

# f = open("IO\main.txt", "w")
# f = f.write("this is new str.")
# print(f)
# f.close()

# append

# f = open("IO\main.txt", "a")
# f = f.write("another line.")
# print(f)
# f.close()

# create x

# f = open("IO/new.txt", "x")
# f.close()

# with keyword

# with open("IO/main.txt") as file:
#     data = file.read()

# print(data)

# seek

# f = open("IO/main.txt", "r")
# f.seek(5)
# data = f.read()
# print(data)
# f.close()

# tell

# f = open("IO/main.txt", "r")
# f.seek(10)
# tell = f.tell()
# data = f.read()
# print(tell)
# print(data)
# f.close()

# truncate

# f = open("IO/main.txt", "a")
# tru = f.truncate(10)
# # data = f.read()
# # print(data)
# print(tru)
# f.close()

# f = open("IO/main.txt", "r")
# data = f.read()
# print(data)
# f.close()
