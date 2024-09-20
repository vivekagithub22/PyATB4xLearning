# Constructor
# Its ia a Special Function in a Class,  __init__()
# It will be automatically called when you create an Object
"""
1. Two Types
    1. Default with no argument
    2. Parameterised - with argument
2. Constructor doesn't return anything
3. `__init__`  name of the constructor
4. Self - current Object , `__init__`

"""

# Eg of constructor with no arguments
class Dog:
    # Attribute
    name = None

    def __init__(self): # Constructor
        print("By default I'm automatically called when an object is created'")

    # Behaviour
    # In behaviour self means current object, self is mandatory argument used in every behaviour.
    def sleep(self):
        print("Sleeping")

# create obj
dog1 = Dog() # Object is created
# Haven't called anything but when you run the program the constructor will be automatically called when an object is created. Print statement will be printed
