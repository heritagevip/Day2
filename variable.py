
def log_msg(msg):
    with open(r"main5.log", "a") as file:
        file.write(msg + "\n")

class owner:
    def __init__(self, name, age):
        self.name = name
        self.age = age 
        


class bankaccount:
    def __init__(self, balance,owner):
        self.balance = balance
        self.owner = owner
    
    def deposit(self, amount):
        self.balance = self.balance + amount
        print(self.balance)
        log_msg(f"{self.owner.name} added {amount} to his bank account")

    def withdraw(self, price):
        self.price = price
        new_balance = self.balance - self.price
        if  self.balance - self.price < 0:
            print("insufficient Funds")
            log_msg(f"{self.owner.name} tried to withdraw money but he gat no money in his acct")
        else:
            print(f"You are about to withdraw {self.price} and your new balance is {new_balance}")
            log_msg(f"{self.owner.name} withdraw {self.price}")
    def check_balance(self):
        Updated_balance = self.balance
        print(f"Dear {self.owner.name} your balance is {Updated_balance}")
        log_msg(f"{self.owner.name} checked his account balance")

owner1 = owner("Heritage", 20)
balance1 = bankaccount(30, owner1)
balance1.deposit(400)
balance1.deposit(30)
balance1.withdraw(50)
balance1.check_balance()
