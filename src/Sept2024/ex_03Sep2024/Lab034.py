""" Create a class by taking user input """

class Person:

    # No need to mention the attributes since we are going to get the input from the user
    def __init__(self): # default constructor with no argument
        self.name = input("Enter the name: \n")
        self.age = int(input("Enter the age: \n"))
        self.phone_num = int(input("Enter the phone number: \n"))
        self.address = input("Enter the address: \n")

    # Behaviour
    def print_details(self):
        print(f" Person details:\n Name is: {self.name}\n Age is: {self.age}\n phone_num is: {self.phone_num}\n address is: {self.address}\n")

person1 = Person() # object is created, constructor will be called
person1.print_details() # normal function call

person2 = Person() # object is created, constructor will be called
person2.print_details()

