import random

# diction = {1: "Snake", 2: "Water", 3: "Gun"}
# print("1.Snake 2.Water 3.Gun")
# inp = int(input("select any one: "))

# userChoose = diction[inp]
# compChoose = random.choice(list(diction.values()))

# print(f"user chooses: {diction[inp]}")
# print(f"computer chooses: {compChoose}")

# if userChoose == compChoose:
#     print("Draw")
# elif (
#     userChoose == "Snake"
#     and compChoose == "Water"
#     or userChoose == "Gun"
#     and compChoose == "Snake"
#     or userChoose == "Water"
#     and compChoose == "Gun"
# ):
#     print("User Wins.")
# else:
#     print("Computer Wins.")


# method 2

lst = [
    [["Snake", "Snake"], ["Water", "Water"], ["Gun", "Gun"]],
    [["Snake", "Water"], ["Water", "Gun"], ["Gun", "Snake"]],
    [["Water", "Snake"], ["Gun", "Water"], ["Snake", "Gun"]],
]

print("1.Snake 2.Water 3.Gun")
inp = int(input("select any one: "))
diction = {1: "Snake", 2: "Water", 3: "Gun"}
userChoose = diction[inp]
compChoose = random.choice(list(diction.values()))

print(f"user chooses: {userChoose}")
print(f"computer chooses: {compChoose}")


if [userChoose, compChoose] in lst[0]:
    print("Draw")
elif [userChoose, compChoose] in lst[1]:
    print("User Wins.")
else:
    print("Computer Wins.")
