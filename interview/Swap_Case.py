def swap_case(s):

    # method 1
    # return s.swapcase()

    # method 2
    res = []

    for char in s:
        if char.islower():
            res.append(char.upper())
        else:
            res.append(char.lower())

    return "".join(res)


print(swap_case("yAwaR"))
