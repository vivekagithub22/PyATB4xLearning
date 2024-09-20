a = 10 # global variable
print(a)


class Person:
    b = 11 # Instance - Belong to class
    c = 11 # Instance - Belong to class

    # Behaviour / function
    def print_infor(self):
        global a # Declare it as global, to reassign the value
        a = "Hello"
        print(a)  # global variable can be accessed directly within functions
        print(self.b) # to use the instance variable within the function we need have to mention self.
        print(self.c)



object_Ref = Person()
object_Ref.print_infor()
print(a) # global variable can be accessed directly anywhere
# print(b) -> we cannot directly call the instance variable outside the class, instead use the below
print(object_Ref.b) # data members and member function in a class can be accessed using objects.
