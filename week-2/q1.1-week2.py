# 1. Class Car
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_details(self):
        print(f"Car: {self.make} {self.model}, Year: {self.year}")

car1 = Car("Toyota", "Corolla", 2021)
car1.display_details()


# 2. Class Rectangle
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

rect = Rectangle(10, 5)
print("Area:", rect.area())
print("Perimeter:", rect.perimeter())


# 3. Inheritance Example
class Animal:
    def speak(self):
        print("Some sound")

class Dog(Animal):
    def speak(self):
        print("Woof!")

dog1 = Dog()
dog1.speak()
