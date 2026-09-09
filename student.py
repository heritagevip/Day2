class student:
    def __init__(self, name, age, department, ):
        self.name = name
        self.age = age 
        self.department = department
        
    def greetings(self):
        if self.age >= 18:
            print(f"Hello {self.name} welcome to FUTES ")
        else:
            print(f"Hello {self.name} you are not qualified for the admission ")
    def addmission_letter(self):
        print("Hello greeting form the FUTES Board we want to congratulate you for gaining admisstion into our prestigious university")

student1 = student("Heritage", 18, "Software Engineering")
student1.greetings()
student1.addmission_letter()