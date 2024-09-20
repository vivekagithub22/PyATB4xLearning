# Public and private instance variable example

class Bank:
    def __init__(self, account_number, balance):
        self.__account_number = account_number #private
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount

    def check_balance(self):
        print("Balance after deposit: ", self.balance)

    def show_acc_num_if_auth(self, is_auth):
        if is_auth == True:
            print(self.__account_number) #private can be accessed inside the class, we have encapsulated the private variable inside the method
        else:
            print("Not allowed to print account number")

# create object
obj1 = Bank(82787387998, 100)
print("Initial balance: ", obj1.balance) #public
obj1.deposit(100)
obj1.check_balance()
obj1.show_acc_num_if_auth(True)

# once again deposit
print("---------------------------------")
print("Initial balance: ", obj1.balance)
obj1.deposit(100)
obj1.check_balance()



