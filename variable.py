
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
            self.balance = self.balance - self.price
    def check_balance(self):
        Updated_balance = self.balance
        print(f"Dear {self.owner.name} your balance is {Updated_balance}")
        log_msg(f"{self.owner.name} checked his account balance")


class user:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
    
    def say_hi_to_user(self, user):
        print(f"Sending message to {user.username}: Hi {user.username}, and  it is {self.username} ")

class student_info:
    def __init__(self, name, age, level):
        self.name = name
        self.age = age
        self.level = level


class student:
    def __init__(self, student_info):
        self.score = []
        self.student_info = student_info
    
    def add_score(self, new_score): 
        self.score.append(new_score)
        print(self.score)
    
    def average(self,):
        average_grade = sum(self.score) / len(self.score)
        print(f"Dear {self.student_info.name}, your average grade is {average_grade}.")
        
student_name1 = student_info("Heritage", "20", "200")
student1 = student(student_name1)
student1.add_score(59)
student1.add_score(48)
student1.add_score(88)
student1.average()
