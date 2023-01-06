try:
    cost = int(input("Cost: "))
    income = 20000
    Risk = income // cost
    print(Risk)
except ZeroDivisionError:
    print("cost cannot be 0.")
except ValueError:
    print("invalid input")

