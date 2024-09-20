class Person:
    # Class Variables
    # Instance variables
    # name = "Amit" # when we assign value to instance variable in a class it becomes hardcoded value

    # So to initialise or to create multiple object and multiple attribute values, we need to use parameterised constructor
    def __init__(self, name):  # if we use default constructor then we cannot set the value while creating the object
        self.name = name

    def walk(self):
        return self.name

# object
amit = Person("amit")
pramod = Person("pramod")
print(amit.name)
print(pramod.name)
print("Who is walking with the object pramod -> ", pramod.walk())