# string characters
print("Hello i'm drew your home assistant")
# variables
age = 20
gender = True
print(age + gender)
# program to take in user input
# name = input("type in your name")
# print("welcome back" + name)
# Data types
# birth_year = input("Enter your birth year: ")
# age = 2022 - int(birth_year)
# print(age)

# Data types ii
# int()=( whole numbers )... float() = ( decimals )... bool() = (true or false )... str() = (characters)...
# First = input("First: ")
# Second = input("Second: ")
# sum = int(First) + int(Second)

# Strings functions
course = "python for me"
# to print all strings in upper case
print(course.upper())
# to print all strings in lower case
print(course.lower())
# to replace me with us
print(course.replace("me", "us"))
# to check if 'all' is in sentence or string
print("all" in course)
# To find the index of a letter
print(course.find('o'))
print(len(course))

# Arithmetic Operations
print(20 + 80)
print(10 - 2)
print(10 * 2)
print(10 ** 2)
print(10 / 2)
print(10 // 2)
print(10 % 3)

# operator precedence
x = 10 + 3 * 2
y = (10 + 3) * 2

# comparison operators
x = 3 > 2
print(x)
y = 4 < 5
print(y)
k = 20 >= 19
print(k)
g = 15 <= 5
print(g)
a = 12 == 13
print(a)
b = 18 != 10
print(b)

# Logical operators
price = 5
print(not price > 10)

# and(both)
# or (at least one)
# not (inverse)

# if statements
temperature = 35

if temperature > 30:
    print("it's a hot day")
    print("Drink plenty of water")
elif temperature > 20:  # (20, 30]
    print("it's a nice day")
elif temperature < 10:
    print("it's a bit cold")
else:
    print("it's cold")
print("Done")

# While loops

i = 1
while i <= 10:
    print(i * '*')
    # print(i)
    i = i + 1

# Lists
names = ["Peter", "james", "henry", "phill", "mark"]
names[0] = "pere"
print(names[0:3])
print(names)

# List Methods
numbers = [1, 2, 3, 4, 5]
# to add new number at the end of the list
numbers.append(6)
# numbers.insert(0, -1)
numbers.remove(4)
# numbers.clear()
print(3 in numbers)
print(len(numbers))
print(numbers)

# For Loops
number = [1, 2, 3, 4, 5]
for item in number:
    print(item)

# using while loop
i = 0
while i < len(numbers):
    print(numbers[i])
    i = i + 1

# The range() Function
numbers = range(5, 10, 2)
for number in range(5):
    print(number)
# Tuples
numbers = (1, 2, 3)
print(numbers)
