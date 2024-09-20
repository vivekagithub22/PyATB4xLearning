a = 10 # global variable
class MyClass:

    # public instance variable
    public_var = "I am PUBLIC" # can be accessed outside the class and anywhere in the program using self.
    college = "ABC"

    # Private variable
    __private_var = "I am private." # starts with double __ , cannot be accessed outside the class
    __password = "1234"

    # Protected variable
    _protected_var = "I am protected." # starts with single _ , can be accessed outside the class, within subclass & within same directory/package

    pramod =  "TTA"
    __pramod_bank =  100000000000
    _outer_bathroom = "for housemates and known people"


object = MyClass()
print(object.public_var) # can be accessed outside the class
print(object._protected_var) # can be accessed outside the class
# print(object.__private_var) # cannot be accessed outside the class
# print(object.__password) # cannot be accessed outside the class