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

hour = int(input("Enter hour: "))
minute = int(input("Enter minute: "))

if hour > 23 or hour < 0 or minute > 59 or minute < 0:
    print("Please enter hour and minute correctly.")
else:
    if hour < 12:
        print("Good Morning")
    elif hour < 18:
        print("Good Evening")
    else:
        print("Good Night")
