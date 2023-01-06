
weight = int(input("weight: "))
unit = input("(K)g or (L)bs: ")
if unit.upper() == "K":
    converted = weight / 0.45
    print("Weight in Lbs: " + str(converted))
else:
    converted = weight * 0.45
    print("Weight in Kgs: " + str(converted))

name = "John Smith"
age = 20
is_new = True

# checking data type
# print(type(var_name))
# user input

# name = input("what is your name? ")
color = input("what's your favourite color? ")
print(name + " likes " + color)

# conversion
# name = input("enter name: ")
birth_year = input("Type your birth-year: ")
age = 2022 - int(birth_year)
print(name + " is " + str(age) + " years old")

# formatted strings
