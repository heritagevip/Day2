
from datetime import datetime
def  log_msg(msg):
    with open(r"log.txt", "a") as file:
        file.write(msg + "\n")
class user:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email
        if len(password) >= 8:
            self._password = password
        else:
            raise ValueError("invalid password")
        self.clean_email()
        log_msg(f"user {self.username}")
        log_msg(f"Email : {self._email}")
    
    def clean_email(self):
        self._email = self._email.strip().lower()

    
    def get_email(self):
        log_msg(f"Email was asseed at {datetime.now()}")
        return self._email
        
    def set_email(self, new_email):
        new_email = new_email.strip().lower()
        if "@" and "." in new_email:
            self._email = new_email
        else:
            raise ValueError("INVALID EMAIL")
        log_msg(f"Email was updated at {datetime.now()}")
        log_msg(f"New email = {new_email}")
    
    def set_pasword(self, new_password):
        if len(new_password) >= 8:
            self._password = new_password
        else:
            raise ValueError ("Invalid password")
    def get_password(self):
        return self._password
    


user1 = user("VIP", "Ademokunwaheritage@gmail.com    ", "12345678")
print(user1.get_email())
user1.set_email("Hdevx@gmail.com")
print(user1.get_email())
user1.set_pasword("Heritage@1234")
print(user1.get_password())