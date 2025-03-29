# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists


# read

# f = open("File Handling/main.txt", "r")
# print(f.read())
# f.close()

# write

# f = open("File Handling/main.txt", "w")
# f = f.write("this is new str.")
# print(f)
# f.close()

# append

# f = open("File Handling/main.txt", "a")
# f = f.write("\nanother line.")
# print(f)
# f.close()

# create x

# f = open("File Handling/main.txt", "x")
# f.close()

# with keyword

# with open("File Handling/main.txt") as file:
#     data = file.read()

# print(data)

# seek

# f = open("File Handling/main.txt", "r")
# f.seek(5)
# data = f.read()
# print(data)
# f.close()

# tell

# f = open("File Handling/main.txt", "r")
# f.seek(10)
# tell = f.tell()
# data = f.read()
# print(tell)
# print(data)
# f.close()

# truncate

# f = open("File Handling/main.txt", "a")
# tru = f.truncate(20)
# print(tru)
# f.close()
