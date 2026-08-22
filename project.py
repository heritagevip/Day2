def student_reg(name, department, age,):
    data = {
        "name": name,
        "Department": department,
        "Age": age,
    }
    return(data)
students = [
    student_reg("Heritage", "Software Engieering", "19"),
    student_reg("Daniel", "Computer Science", "20"),
    student_reg("VIP", "Software Engineering", "18")
]
for student in students:
    print(student["name"])