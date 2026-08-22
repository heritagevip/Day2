def is_email_valid(email):
    return"@" in email and "." in email
def is_password_valid(password):
    return len (password) >= 8
def clean_name(name):
    firstname, lastname = name.split(" ")
    return firstname, lastname
def log_msg(log):
    with open(r"main3", "a") as file:
        file.write(log + "\n")
name = "Ademokunwa Daniel"
email = "ademokunwadaniegmail.com"
password = "1234678"
def orchestrator ():
    log_msg("App Started")
    log_msg(f"user = {clean_name(name)}")
    if not is_email_valid(email):
        log_msg("invalid Email")
    else:
        log_msg("Enter your Password")
    if not is_password_valid(password):
        log_msg("Invalid Password")
    else:
        log_msg("Login Successfully")
    log_msg("app stopped")

orchestrator()
    