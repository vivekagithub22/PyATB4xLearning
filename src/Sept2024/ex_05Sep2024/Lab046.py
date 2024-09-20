# Multilevel inheritance

class Grandfather():
    grandfather_gold = "1gm gold"

    def grand_father_house(self):
        print("1BHK")

class Father(Grandfather):
    father_diamond = "22 karat diamond"

    def father_house(self):
        print("2BHK")

class Son(Father):
    BTC = "1BTC"

    def son_house(self):
        print("3BHK")

# Obj of son
# child class can access the attributes and behaviours of it's own parent and grandparent class

son = Son()
print(son.father_diamond)
son.father_house()
print(son.grandfather_gold)
son.grand_father_house()


