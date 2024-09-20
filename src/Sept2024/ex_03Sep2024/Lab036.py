# parameterised argument constructor

class calc():
    a1 = None
    b1 = None

    def __init__(self, a1, b1):
        self.a1 = a1
        self.b1 = b1

    def sum1(self):
        return self.a1 + self.b1

    def sub1(self):
        return self.a1 - self.b1

    def mul1(self):
        return self.a1 * self.b1

    def div1(self):
        return self.a1 / self.b1

object1 = calc(3, 4)
print(object1.sum1())
print(object1.sub1())
print(object1.mul1())
print(object1.div1())
# One line code to print return values
print(f"Values of calc:\n"
      f"Sum: {object1.sum1()}\nSub: {object1.sub1()}\nmul: {object1.mul1()}\ndiv1: {object1.div1()}")

object2 = calc(4,9)
print(object2.mul1())

object3 = calc(7,2)
print(object2.sub1())

