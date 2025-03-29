input = "A5B7C3"
temp = ""

i = 0
while 1:
    # print(i)
    if i >= (len(input) - 1):
        break

    if (
        ord(input[i].lower()) >= 97
        or ord(input[i].lower()) <= 122
        and isinstance((input[i + 1]), int)
    ):
        temp = temp + (input[i] * int(input[i + 1]))
        # print(temp)
        i = i + 2
    else:
        temp += input[i]
        # print(temp)
        i = i + 1

print(temp)
