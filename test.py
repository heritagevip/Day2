def student_info(name, department, level):
    student_info = name + " " +department + " " + level 
    print(student_info)
student_info("Heritage", "Software Engineering", "100" )
student_info("Daniel", "Software Engineering", "200")
for name in student_info:
    print(name)