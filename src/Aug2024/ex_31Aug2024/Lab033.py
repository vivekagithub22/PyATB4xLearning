# Eg of constructor with parameterised argument

""" Why constructor is required ? - To initialise the value of attributes/ instance variables """

class Dog:
    # Attribute
    name = None # Instance variable
    age = None
    #colour = "black" -> hardcoded, then the value becomes common to all the objects, cannot have unique

    def __init__(self, name, age): # Constructor
        print("By default I'm automatically called when an object is created'")
        self.name = name # self.name = name -> acts as dog1.name = value
        self.age = age

    # Behaviour
    def sleep(self):
        abc = 10 # local variable
        print("Sleeping")
        print("who is sleeping ? - ", self.name)

# create obj
dog1 = Dog("Chow", 10) # Passing arguments while creating objects
print(dog1.name)
print(dog1.age)
dog1.sleep()

dog2 = Dog("Mow", 20) # Object is created
print(dog2.name)
print(dog2.age)
dog2.sleep()



""" 
dog1 = Dog("Chow") -> Object is created
name - Chow
self.name = name -> acts as dog1.name = chow
print(dog1.name) -> prints "Chow"

"""