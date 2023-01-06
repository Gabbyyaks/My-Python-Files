import random


staffs = ['lawrence', 'perry', 'silver', 'Drew', 'steve']
HOD = random.choice(staffs)
print(HOD)

# probability of throwing two dice
class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second


dice = Dice()
print(dice.roll())

