# 1. Encapsulation Example
class Employee:
    def __init__(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

emp = Employee(50000)
print("Initial Salary:", emp.get_salary())
emp.set_salary(60000)
print("Updated Salary:", emp.get_salary())

# Trying to access private variable directly
try:
    print(emp.__salary)
except AttributeError:
    print("Cannot access private attribute directly!")


# 2. Multiple Inheritance
class A:
    def greet(self):
        print("Hello from A")

class B:
    def greet(self):
        print("Hello from B")

class C(A, B):
    pass

obj = C()
obj.greet()  # Method Resolution Order calls A.greet()


# 3. Abstract Method Example
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

circle = Circle(5)
square = Square(4)
print("Circle area:", circle.area())
print("Square area:", square.area())


# 4. Class Variable Example
class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

obj1 = Counter()
obj2 = Counter()
obj3 = Counter()
print("Total objects created:", Counter.count)
