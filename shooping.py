
class bankaccount:
    MIN_BALANCE  = 100

    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balane = balance


    def deposit(self, amount):
        if self._is_valid_amount:
            self._balane += amount
            self.__transat_log("Deposit", amount )
        else:
            print("Invalid Deposit ")
    
    def withdraw(self, amount):
        if self._balane > amount:
            self._balane -= amount
            self.__transat_log("Withdraw", amount)

    @property
    def balance(self):
        return self._balane

    def _is_valid_amount(self, amount):
        return amount > 0

    def __transat_log(self, transaction_type, amount):
        print(f"Logging {transaction_type}, of {amount} by {self.owner}")

account1 = bankaccount("Heritage", 500)
account1.deposit(10)
account1.withdraw(200)
print (account1.balance)