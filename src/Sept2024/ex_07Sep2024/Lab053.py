# Method Overloading:
# Python does not support method overloading
# in the traditional sense.

class MathUtils(object):  # is- A object - single inheritance
    # Method - overloading - Not supported!
    def add(self, a, b):
        return a + b

    def add(self, a, b, c=10, d=1):
        return a + b + c + d

    def add(self, a, b, c):
        return a + b + c

math = MathUtils()
op1 = math.add(1, 2, 3) # it will call the function which is at the last
print(op1)