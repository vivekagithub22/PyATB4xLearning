# Custom Exception - Own

class BalanceLowException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


balance = 100
withdrawal = int(input("Enter the withdrawal amount: "))
if withdrawal > balance:
    raise BalanceLowException("Balance is low, enter a less amount")
else:
    print("Remaining balance is: ", balance - withdrawal)
