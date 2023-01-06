names = ['Emmy', 'josh', 'Gabby', 'isaac']
# to change an item in the list
names[1] = 'Genesis'
print(names)
print(names[0:3])

# program to print highest number in a list
numbers = [5, 3, 4, 10, 6, 8]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)


# 2D lists

matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
]
matrix[0][1] = 15
print(matrix[0][1])

# forloop to print items in matrix
for row in matrix:
    for item in row:
        print(item)

# list methods

numbers = [5, 7, 2, 9, 0]
names = ['Isaac', 'Emmy', 'Gabby', 'Genesis']

numbers.remove(2)
print(numbers)

names.insert(3, 'marvelous')
print(names)

# to remove duplicates from a list
numbers2 = [1, 3, 8, 3, 5, 1]
none = []
for numbers in numbers2:
    if numbers not in none:
        none.append(numbers)
print(none)

