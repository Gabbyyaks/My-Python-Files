class Point:
    def move(self):
        print("move0")

    def draw(self):
        print("draw")


point1 = Point()
point1.x = 10
point1.y = 20
print(point1.x)
point1.draw()

point2 = Point()
point2.x = 5
print(point2.x)

# Constructors

class Stat:
    def __init__(self, key, en):
        self.key = key
        self.en = en

    def make(self):
        print("make")

    def stop(self):
        print("stop")


test = Stat(45, 15)
print(test.en)

class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, welcome {self.name}")


peps = Person("john Doe")
peps.talk()

bob = Person("Bob Smith")
bob.talk()

# Inherit
class Mammal:
    def walk(self):
        print("walk")

class Dog(Mammal):
    def bark(self):
        print("bark")


class Cat(Mammal):
    def stubborn(self):
        print("stubborn")


dog1 = Dog()
dog1.walk()

cat1 = Cat()
cat1.stubborn()