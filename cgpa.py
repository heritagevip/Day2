def students_name(names):
    name = names.upper()
    return(name)

def course_mark(cos104, cos126, cos124):
    total_mark = cos104 + cos124 + cos126
    average = total_mark/3
    return total_mark, average

total, average = course_mark(50, 70, 70)
def calculate_grade(average):
    if average >= 70:
        return "A"
    elif average >=60:
        return "B"
    elif average >=50:
        return "C"
    elif average >=45:
        return "D"
    elif average >=40:
        return "E"
    else:
        return "F"

print(f"Dear {students_name("Heritage")}\nTotal mark = {total}\nAverage = {average}\nGrade = {calculate_grade(average)}")
