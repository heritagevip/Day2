
from datetime import datetime
def  log_msg(msg):
    with open(r"log.txt", "a") as file:
        file.write(msg + "\n")
class user:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email
        self.password = password
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
        self._email = new_email
        log_msg(f"Email was updated at {datetime.now()}")
        log_msg(f"New email = {new_email}")
    


user1 = user("VIP", "Ademokunwaheritage@gmail.com    ", "12345678")
print(user1.get_email())
user1.set_email("Hdevx@gmail.com")
print(user1.get_email())