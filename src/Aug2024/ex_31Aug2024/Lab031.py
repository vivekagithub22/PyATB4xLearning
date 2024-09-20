class Dog: # Class Name will always start from the Capital letter. Class name follows CamelCase
    # A
    name = None
    breed = None
    color = None

    # B
    # Behaviour: What the attributes can do.
    # In behaviour self means current object, self is mandatory argument used in every behaviour.
    def sleep(self):
        print("Sleeping", self.name)

    def bark(self):
        print("bark")

    def eat(self, food):
        print(food)


dog1 = Dog()
print(dog1.name)
dog1.name = "Chow"
print(dog1.name)
dog1.sleep()

print("----------------------")


dog2 = Dog()
print(dog2.name)
dog2.name = "Mow"
print(dog2.name)
dog2.sleep()

dog3 = dog1