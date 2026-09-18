
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
        #log_msg(f"Email : {self._email}")
    
    def clean_email(self):
        self._email = self._email.strip().lower()

    @property
    def email(self):
        return self._email
        log_msg("a")

    @email.setter
    def email(self, new_email):
        if "@" and "." in new_email:
            self._email = new_email
        else:
            raise ValueError("Invalid Email")

    


user1 = user("VIP", "Ademokunwaheritage@gmail.com    ", "12345678")
user1.email = "vip@gmail.com"
print(user1.email)
