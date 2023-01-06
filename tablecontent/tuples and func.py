# unpacking

number = (1, 2, 3)
x, y, z = number

print(y)

# functions and 'parameters = (name) and argument (value of name)'
def greet_user(name):
    print(f"hello {name}")
    print("welcome")


print("start")
greet_user("Gabby")
greet_user("James")
print("finish!")

# adding two parameters (positional)
def user(name, surname):
    print(f"hello {name}, {surname}")
    print("welcome back!")


user("Isaac", "brown")
print("get started")

# keywords argument (non-positional) can be placed anywhere provided keyword is present
# NB: always use positional arguments before keyword argument
user("Isaac", surname="perry")

# return statement

def square(number):
    return number * number


print(square(4))

