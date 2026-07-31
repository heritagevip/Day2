'''multi= """ this is a multi line code 
it is useful for multitasking
"""
first_name = "Ademokunwa"
last_name = "Heritage"
space = " "
full_name = first_name + space + last_name
print("i hope everyone is enjoying their holiday. \n Are you ?")
print("day \t Topic \t excercise")
print("1 \t 5 \t 5")
print("2 \t 6 \t 8")
print("this is a symbol of backlash (\\)")
print("Every programming language starts with 'Hello world!'")
print ('i am %s %s and my fullname is %s' %(first_name, last_name, full_name))
language = 'python'
print (language [-4])'''
name = "Heritage"
department = "Software engineering"
matric_no = 2501050268
NB = ''' A == 5 (70-100), B == 4 (60-69), C == 3 (50-59), D ==2 (40-49), E ==1 (30-39), F == 0 (0-29)'''
print(NB)
cos_102_score = int(input("Enter Your Cos 102 result point in fig in range (1-5) "))
cos_104_score = int(input("Enter Your Cos 102 result point in fig in range (1-5) "))
csc_122_score = int(input("Enter Your Cos 102 result point in fig in range (1-5) "))
cos_124_score = int(input("Enter Your Cos 102 result point in fig in range (1-5) "))
cos_126_score = int(input("Enter Your Cos 102 result point in fig in range (1-5) "))
phy_102_score = int(input("Enter Your Cos 102 result point in fig in range (1-5) "))
mth_102_score = int(input("Enter Your Cos 102 result point in fig in range (1-5) "))
phy_108_score = int(input("Enter Your Cos 102 result point in fig in range (1-5) "))
gst_112_score = int(input("Enter Your Cos 102 result point in fig  in range (1-5)"))
tqp = float(input("Enter Total Quality Points (TQP): "))
total_unit = int(input("Enter Total Units (TU): "))

gpa = tqp / total_unit

print("Your GPA is:", round(gpa, 2))

if gpa >= 4.50:
    print("Class of Degree: First Class")
elif gpa >= 3.50:
    print("Class of Degree: Second Class Upper")
elif gpa >= 2.40:
    print("Class of Degree: Second Class Lower")
elif gpa >= 1.50:
    print("Class of Degree: Third Class")
elif gpa >= 1.00:
    print("Class of Degree: Pass")
else:
    print("Class of Degree: Fail")


