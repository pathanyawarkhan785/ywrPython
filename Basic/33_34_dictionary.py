dict = {"name": "abc", "class": 1, "sem": 2}

# print(dict)

# if key not exists in dict["name"] throws error while dict.get("name") returns None.

# print(dict["name1"])
# print(dict.get("name1"))

# print(dict.keys())
# print(dict.values())

dictItems = dict.items()
# print(dictItems)

# for key, val in dictItems:
#     print(f"{key} : {val}")

# dictionary methods

dict1 = {"xyz": "a", 2: "b", 3: "c", 4: "d"}
dict2 = {5: "e", 6: "f"}

# update
# add dict2's values to dict2

# dict1.update(dict2)
# print(dict1)

# clear
# clear all the values from dictionary and make empty dictionary.

# dict1.clear()
# print(dict1)

# pop
# removes key : xyz & its value

# dict1.pop("xyz")
# print(dict1)

# del
# here use square bracket, removes key : 1 & its value

# del dict1["xyz"]
# print(dict1)


# dict = {}
# newStr = "yawar"

# for i in newStr:
#     dict[i] = dict.get(i, 0) + 1 // if element exists return its value otherwise 0(second argument)

# print(dict)
