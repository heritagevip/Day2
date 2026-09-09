
def log_msg(msg):
    with open(r"student,log", "a") as file:
        file.write(msg + "\n")



class Student():
    def __init__(self, name, matric_no, age, gender):
        self.name = name
        self.age = age
        self.matric_no = matric_no
        self.gender = gender
        log_msg(f"{self.name} registered Successfully")
    
    def score(self, x):
        self.x = x
        if x >= 70:
            return 5
        elif x >= 60:
            return 4
        elif X >= 50:
            return 3
        elif x >= 40:
            return 2
        elif x >= 30:
            return 1
        else:
            return 0

    def course_score(self, x, unit):
        return x * unit
        


    def course_unit(self, cos104_unit= 3, cos102_unit= 2, cos122_unit=2, mth102_unit=2, phy102_unit=2):
        total_unit = cos102_unit + cos122_unit + cos104_unit + mth102_unit + phy102_unit

Student1 = Student("Heritage", 222001, 14, "male")
print(Student1.course_score(70,3))