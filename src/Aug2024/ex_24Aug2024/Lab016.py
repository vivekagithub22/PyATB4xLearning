"""
Functions & Types of functions in Python
"""

# A block of code which can be reused to perform a specific task
# Function in python are defined using def keyword, followed by function name and parenthesis ():
# definition, calling
# They may or may not return something
# Functions can take parameters and return values.

""" 
Definition
"""
def greet():
    print("Hello")

"""    
Calling   
"""
greet()

# Built-in functions created by python
# print(), input(), max(), type(), id(), abs(), pow(), upper(), len(), list(), math.pi(), range(), math.factorial(), sorted(), int(), str(), bool(), float()

# custom-made functions, user defined functions
# def greet():

""" Rules for function name """
# We cannot use camelCase, instead we use lowercase separated by _ underscore -> name_lastname():
# We can use _():
# We cannot use only numbers 123():, can be letters or group of letters followed by numbers -> promod123():, p123():

""" we can invoke a function within another function"""

def name1(): # function 1
    print("Viveka")

def name2(): # function 2
    print("Varthini")
    name1() # invoked function 1 into function 2

name2() # by calling function 2, function 1 will also be called

""" Passing variable name within ()""" """ We can declare the parameter while defining the function, we can pass the argument while calling the function"""

def greet_by_name(name): # name is a variable name, name is the parameter of the function
    print("Hello", name)

greet_by_name("viveka") # is the argument that you pass to the function. while calling the func, we need to pass the variable value/ argument.
greet_by_name(123) # variable value can be anything
greet_by_name(3.14)
greet_by_name(True)

""" User input """

def greeting(x_name):
    print("Hello,", x_name)

x_name = input("Enter your name:\n")
greeting(x_name)





