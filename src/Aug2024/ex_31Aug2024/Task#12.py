"""
Class and Object Assignment

Create a Employee Class
A - name,age, phone, address, eid
B - walk, talk, print details
with the Constructor which will set the values
Ask the user about the information for E1, E2
print the details of the E1, E2 via the print employee functions.
"""


class Employee:
    # Attributes
    name = None
    age = None
    phone = None
    address = None
    eid = None

    # Constructor
    def __init__(self, name, age, phone, address, eid):
        print("Automatically called when object is created")
        self.name = name
        self.age = age
        self.phone = phone
        self.address = address
        self.eid = eid

    # Behaviour
    def walk(self):
        print("Who is walking? - ", self.name)

    def talk(self):
        print("Who is talking? - ", self.name)

# Create obj
E1 = Employee(input("Enter the name of Employee: "), int(input("Enter the age of Employee: ")), int(input("Enter the phone of Employee: ")), input("Enter the address of Employee: "), int(input("Enter the eid of Employee: ")))
print("Employee details:",'\n',"Name:", E1.name, "Age:", E1.age, "Phone_num:", E1.phone, "Address:", E1.address, "Eid:", E1.eid)
E1.walk()
E1.talk()
E2 = Employee(input("Enter the name of Employee: "), int(input("Enter the age of Employee: ")), int(input("Enter the phone of Employee: ")), input("Enter the address of Employee: "), int(input("Enter the eid of Employee: ")))
print("Employee details:",'\n',"Name:", E2.name, "Age:", E2.age, "Phone_num:", E2.phone, "Address:", E2.address, "Eid:", E2.eid)
E2.walk()
E2.talk()







