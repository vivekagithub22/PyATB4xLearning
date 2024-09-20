# Hierarchical inheritance
# B,C,D can inherit A

class Father:

    def father_property(self):
        print("1BHK")

class Son1(Father):

    def son1_property(self):
        print("2BHK")

class Son2(Father):

    def son2_property(self):
        print("3BHK")

class Son3(Father):

    def son3_property(self):
        print("No house")

# Obj
amit = Son1()
amit.son1_property()
amit.father_property()
# son1 can access his own attributes and behaviours as well as his father's attributes and behaviours

pramod = Son2()
pramod.son2_property()
pramod.father_property()
# son2 can access his own attributes and behaviours as well as his father's attributes and behaviours

lucky = Son3()
lucky.son3_property()
lucky.father_property()
# son3 can access his own attributes and behaviours as well as his father's attributes and behaviours



