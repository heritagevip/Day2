#def info(name, Country = "n/a", Age = "n/a"):
#    print(f"i am {name} from {Country} and i am {Age} old ")
#info(name=8, Country=8, Age=8)
#def create_user(**kwargs):
#    print(kwargs)
#    print(type(kwargs))
#create_user(name="Heritage", age=2, country="Nigeria", school="futes", year=2026)
#def user(*arg):
#    print(arg)
#    print(type(arg))
#user("Heritage", 19, "Futes")
#create_user(name= "Daniel", age= 3 )
#def daily_log(logs):
#    with open(r"C:\Users\Heritage\Desktop\Day2\main.log", "a") as file:
#        file.write(logs + "\n")

#daily_log("Admin logged in")
#daily_log("Admin logged out")
#daily_log("Admin Removed You")

def clean_and_split(email):
    cl_email = email.strip().lower()
    username, domian  = cl_email.split("@")
    return {"username": username,
            "domain": domian}

#print(clean_and_split("    AdeMokunwa Daniel Ademokunwadaniel@gmail.com   "))
def is_vaild_email(email):
    return "@" in email and  "."in email

def log_msg(logs):
    with open(r"main2.log", "a") as file:
        file.write(logs + "\n")
log_msg("App Started")
email = "ademokunwadaniel@gmail.com"
if not is_vaild_email(email):
    log_msg(f"Invaild Email {email}")
else:
    clean_and_split(email)
    log_msg(f"{clean_and_split(email)}")
log_msg("App Ended")

