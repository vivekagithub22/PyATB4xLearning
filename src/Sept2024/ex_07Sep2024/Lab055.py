# Static Methods
# A static method is a method that belongs to a class rather than an instance of the class.

# To access the methods inside the class, we need to create obj and call the methods.
# if we make the methods as static we no need to create obj, we can directly call it using ClassName.method_name

class O:
    @staticmethod
    def sum(a, b):
        return a + b


class MathOperations(O):

    def div(self, a, b):
        return a / b

    def mul(self, a, b):
        return a * b

    @staticmethod
    def sum(a, b):
        return a + b

    @staticmethod
    def sub(a, b):
        return a - b


# Non Static in Nature - Object creation is mandatory, and should be called using object
object_ref = MathOperations()
output = object_ref.div(10, 5)
output2 = object_ref.mul(10, 5)
print(output)
print(output2)

# Static methods can be called directly without creating the Object.
print(MathOperations.sum(4, 5))
print(MathOperations.sub(4, 5))
print(O.sum(4, 5))

# to access static methods it should be --> ClassName.method_name

# to access non static methods - (Object creation is mandatory) it should be --> object.method_name

