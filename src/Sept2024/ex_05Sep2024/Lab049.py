# Hybrid inheritance
# it is a mixture of Multiple and hierarchical inheritance

# multiple types of inheritance,
# such as single, multiple, and hierarchical inheritance.

# Img representation of inheritance
# https://eraser.imgix.net/workspaces/V1rGGsUC3exwXT9FRzVL/WWS31TdyovhjTB1TVo9v2jWpPei1/Fu_txXzEfn1sqW9Kt3ENl.png?ixlib=js-3.7.0


class A: # Father
    def methodA(self):
        return "Method A"

class B(A): # Son1
    def methodB(self):
        return "Method B"

class C(A): # Son2
    def methodC(self):
        return "Method C"


class D(B, C): #Sister  # Multiple, Multilevel - MRO(Method Resolution Order - First)
    def methodD(self):
        return "Method D"

d = D()
print(d.methodA())
print(d.methodB())
print(d.methodD())
print(d.methodC())