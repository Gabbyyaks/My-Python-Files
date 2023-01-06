
for numbers in range(5, 20, 4):
    print(numbers)

# calculating sum using for loop
prices = [10, 20, 30]
total = 0
for price in prices:
    total += price
print(f"Total: {total}")

# nested loops

for x in range(4):
    for y in range(3):
        print(f'({x},{y})')

numbers = [5, 2, 5, 2, 2]

for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)

value = [3, 3, 3, 3, 8, 8]
for nums in value:
    result = ''
    for count in range(nums):
        result += 'x'
    print(result)

