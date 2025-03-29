def swap_case(s):

    res = []

    for char in s:
        if char.islower():
            res.append(char.upper())
        else:
            res.append(char.lower())

    return "".join(res)


if __name__ == "__main__":
    s = input()
    result = swap_case(s)
    print(result)
