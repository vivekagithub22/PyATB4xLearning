"""
## Encapsulation
- bind the data variables with the methods.
- data variable - Data Member / Class Variables / instance variables
- Wrapping or binding the data variables by using the methods is called Encapsulation.
- Hide the data members by using methods
- Methods - Def function within the class.

A class can safeguard the attributes by using public, protected and private keywords. i.e - basically hiding the data members by using methods

# Public : Variable - Don't Mention anything
- Members are accessible from anywhere in the program.

# Protected : _
Members are intended for internal use within the class and its subclasses and only within the same package/directory

# Private : __
Members are only accessible within the class they are defined in.

"""


# In a normal situation

class Car:
    name = None
    password = 123

    def __init__(self):
        self.password = "pramod"

    def change_password(self):
        print(self.password)

ob1 = Car()
print(ob1.password) # in normal we can directly access the instance variable by using object, so outsiders can use the instance variable

# to prevent this we use encapsulation
