# Method Overriding - Same name in the parent and child class
# child always override the parent functions
# super(). means call my parent function or attribute
class GrandFather:
    x = 10
    def home(self):
        print("Old Home")

class Father(GrandFather):
    a = 11
    def home(self):
        print("1BHK")
        print(self.a)
        print(super().x)

class Son(Father):
    b = 12
    def home(self):
        super().home() # Father Behaviour by super().
        print(super().a) # Father Attributes by super().
        print("No House")
        print(self.b)


        # self - me
        # super() - Parent, Super class, Father

pramod = Son()
pramod.home()
print(pramod.x) # if you want to call the parent's parent class attribute or function, we can directly call outside the class