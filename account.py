
import random
import os
import json
class user:
    def __init__(self, name, age , birthday, pin, ):
        self.name = name
        self.age = age
        self.birthday = birthday
        self._pin = pin 


class bankaccount:
    def __init__(self,user, balance=0 ):
        self.user = user
        self._balance = balance
    
        if os.path.exists("bank.json"):
            with open("bank.json", "r") as file:
                loaded_data = json.load(file)
            self._account_number = loaded_data["Account_Number"]
            self.data = {"Name": self.user.name, "Account_Number": self._account_number, "Birthday": self.user.birthday, "Pin": self.user._pin, "Balance": self._balance}
        else:
            self._account_number = random.randint(0000000000, 9999999999)
            self.data = {"Name": self.user.name, "Account_Number": self._account_number, "Birthday": self.user.birthday, "Pin": self.user._pin, "Balance": self._balance}
            with open("bank.json", "w") as file:
                json.dump(self.data, file)
        
    def save(self):
            self.data = {"Name": self.user.name, "Account_Number": self._account_number, "Birthday": self.user.birthday, "Pin": self.user._pin, "Balance": self._balance}
            with open("bank.json", "w") as file:
                json.dump(self.data, file)
    
    def report(self, transaction_type, amount, Message):
        self.transaction_type = transaction_type
        reports = {"Transaction_type": transaction_type, "Amount": amount, "Balances": self._balance , "Transaction status": Message}
        with open("report.jsonl", "a") as file:
            file.write(json.dumps(reports)+  "\n")
    @property
    def balance(self):
        return self._balance
    
    @property
    def account_number(self):
        return self._account_number
    
    def deposit(self, amount):
        self.amount = amount
        self._balance += self.amount
        self.save()
        self.report("Deposit", self.amount,"Succesfull")
    
    def withdraw(self, amounts):
        self.amounts = amounts
        pin = int(input("Enter Your Pin "))
        if pin == self.user._pin:
            if self._balance - self.amounts > 100:
                self._balance -= self.amounts
                print(f"{amounts} withdraw Succesful")
                self.save()
                self.report("Withdraw", self.amounts, "Succesfull")
            else:
                print("Insufficient Balance")
                self.report("Withdraw", self.amounts, "Failed")
        else:
            print("Wrong pin")
            self.report("Withdraw", self.amounts, "Invalid pin ")

   
    def transfer(self, account_numbers, price):
        accounts = [
        {"Name": "Heritage", "Account_Number": 5649698267, "Birthday": "July 25 2008", "Pin": 1234, "Balance": 920},
        {"Name": "daniel", "Account_Number": 5649698268, "Birthday": "July 25 2008", "Pin": 1234, "Balance": 920},
        {"Name": "vip", "Account_Number": 5649698269, "Birthday": "July 25 2008", "Pin": 1234, "Balance": 920}
    ] 
        self.account_numbers = account_numbers
        for a in accounts:
            if account_numbers == a["Account_Number"]:
                print(a["Name"])




              
    



user1 = user("Heritage", 18, "July 25 2008", 1234, )
account1 = bankaccount(user1)
account1.deposit(2000)
user2 = user("Daniel", 19, "August 30 2010", 0000)
account2 = bankaccount(user2)
account2.deposit(1000)
print(account2.account_number)
account1.transfer(5649698268, 200)
