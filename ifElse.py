# age = int(input("enter age: "))
# print(age)

# print(age < 12)
# print(age > 12)
# print(age <= 12)
# print(age >= 12)
# print(age == 12)
# print(age != 12)

# exercise 2

# good morning
# good afternoon
# good evening

hour = int(input("enter hour: "))
min = int(input("enter minute: "))

if hour > 23 or min > 59:
    print("enter hour & min correctly.")

if hour < 12 and min < 60:
    print("Good Morning")
elif hour > 13 and hour < 18 and min < 60:
    print("Good Evening")
else:
    print("Good Night")
