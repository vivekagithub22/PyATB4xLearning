# Multiple inheritance

class Father:

    father_vehicle = "bike"

    def house(self): # diamond problem
        print("Father's house")

    def father_money(self):
        return 5

class Mother:

    mother_vehicle = "scooty"

    def house(self): # diamond problem
        print("Mother's house")

    def mother_money(self):
        return 2

class Son1(Father, Mother):

    def son1_property(self):
        print("nothing")

class Son2(Mother, Father):

    def son2_property(self):
        print("nothing")


# Obj

s1 = Son1()
# if both the class A and B is having the function with same name, Class C inherited both A and B and when object of class C tries to access the function which is having the same name, then python calls the function by checking which class is inherited first "class Son(Father, Mother):"
# class Son(Father, Mother): here Father class is inherited first so it calls the function is father class
# It is MRO - Method Resolution Order
s1.house() # calling the function which is in both A and B with the same name
# child class can access the attributes and behaviours from both the inherited parent class
print(s1.father_money())
print(s1.mother_money())


s2 = Son2()
s2.house()
# if both the class A and B is having the function with same name, Class C inherited both A and B and when object of class C tries to access the function which is having the same name, then python calls the function by checking which class is inherited first "class Son(Mother, Father):"
# class Son(Mother, Father): here Mother class is inherited first so it calls the function is Mother class


