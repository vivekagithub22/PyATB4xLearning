"""
#### Polymorphism
- OOPs concept, Interview
- Objects -> has many forms
- behaviour - behaves different based on who is calling
- Polymorphism allows objects of different classes to be treated as objects of a common superclass.
- By using two ways we can achieve Polymorphism - Method Overriding(run-time), Method Loading
"""

# Method overriding
# says that, Child or subclass can have same name of the method as the parent or super class


class Shape:
    def area(self):
        print("Print the AREA of the shape")


class Rectangle(Shape): # IS-A - Single Inheritance
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length*self.width


class Circle(Shape): # Hierarchical Inheritance
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


shape1 = Rectangle(3,4)
print(shape1.area())

shape2 = Circle(10)
print(shape2.area())