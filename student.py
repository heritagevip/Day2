def add_studet(**student):
    return(student)
def log_msg(log):
    with open(r"main4.log", "a") as file:
        file.write(log + "\n")
student1 = add_studet(name = "Heritage", department = "Software Engineering", school = "futes")
log_msg(f"{student1}")
print(student1["name"])