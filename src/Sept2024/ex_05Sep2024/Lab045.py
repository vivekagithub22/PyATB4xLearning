"""
# Inheritance
- Acquire the Attributes and Behaviour from another class.
- `3BHK House -Father -> Inherit - Son`
- `concept in object-oriented programming (OOP)`
- `that allows a class (child class) to inherit attributes and methods of parent class`

**Types of Inheritance**

- **Single** - 85%  - # API, Web Automation
- Multiple
- Multi level
- Hybrid
- Hierarchical

"""

# Single inheritance

#Parent Class
class Father:
    #Attribute
    Father_gold = "Father's gold" # instance variable

    #Behaviour
    def father_house(self):
        print("Father has 2BHK")
    def father_car(self):
        print("Father has a car")

#Child class
class Son(Father):
    Son_diamond = "diamond"

    def truck(self):
        print("Son has a truck")


#Obj

son_obj = Son()
son_obj.father_house() # child class can access parent class behaviour
print(son_obj.Father_gold) # child class can access parent class attribute
son_obj.truck() # child can access it's own function and attributes

# parent class cannot inherit child class
#print(father_obj.truck())

