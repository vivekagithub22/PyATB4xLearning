# Example by myself

class Toilet:


    def __init__(self, public_toilet, __private_toilet, _protected_toilet):
        self.strangers = public_toilet
        self.__housemates = __private_toilet
        self._relatives = _protected_toilet

    def housemates(self, *name):
        if name == "viveka" or "kuppu" or "mano":
            print(self.__housemates) # we have encapsulated private variable inside the method/function
        else:
            print("Not allowed")



# object
obj1 = Toilet("Allowed to use Public toilet", "Allowed to use private toilet inside the house", "Allowed to use protected toilet inside the compound")
print(obj1.strangers)
print(obj1._relatives)
obj1.housemates("viveka", "mano")


