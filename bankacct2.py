
import random
import json
import os
class owner:
    def __init__ (self,name, age):
        self.name = name
        self.age = age
        

class bankaccount:
    def __init__(self, balances, owner):
        self.balances = balances
        self.owner = owner
    
        if os.path.exists("accounts.json"):
            with open("accounts.json", "r") as file:
                loaded_data = json.load(file)
            self.account_number = loaded_data["Account_number"]
            self.data = {"Account_number": self.account_number, "Balances": self.balances}
        else:
            self.account_number = random.randint(1000000000, 9999999999)
            self.data = {"Account_number": self.account_number, "Balances": self.balances}
            with open("accounts.json", "w") as file:
                json.dump(self.data, file)
    
    def save(self):
        self.data = {"Account_number": self.account_number, "Balances": self.balances}
        with open("accounts.json", "w") as file:
            json.dump(self.data, file)

    def deposit(self, amount):
        self.amount = amount
        self.balances = self.balances + self.amount
        self.save()
    
    def withdraw(self, amounts):
        self.amounts = amounts
        if self.balances - self.amounts < 0:
            print(f"Insufficient Funds")
        else:
            self.balances = self.balances - self.amounts
        self.save()

    def check_balance(self):
        updated_balance = self.balances 
        print(self.balances)
        self.save()   
                
    
        
owner1 = owner("Heriatage", "18")
user1 = bankaccount(1000, owner1)
user1.deposit(110000)
user1.withdraw(2000)
user1.check_balance()









