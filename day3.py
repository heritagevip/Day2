'''my_cart = [19.33, 35.22, 46, 78]
my_data = {"car": "rolls_royce", "name": "Heritage", "owner": "Heritage"}
my_cart.append(33.5)
user_1 = {"username" : "Heritage", "id" : 1, "course": "Software engineering", "CGPA": 4.88}
user_2 = {"username" : "VIP", "id": 2, "course": "Software engineering", "CGPA": 4.98}
my_user = [user_1, user_2]
for user in my_user:
    print("username;", user['username'])
    print("course;", user['course'])
    print("CGPA", user['CGPA'])
number = [1,2,3,4, 10, 40, 15, 34, 47]
number_sq = [] 
factor_of_3 = []
factor_of_4 = []
for num in number:
    num_sq = num ** 3
    number_sq.append(num_sq)
is_even = []
is_odd = []
for num in number_sq:
    if num %2 == 0:
        is_even.append(num)
    elif num %3 ==0:
        factor_of_3.append(num)
    elif num %4 == 0 :
        factor_of_4.append(num)
    else:
        is_odd.append(num)
print(is_even, is_odd, factor_of_3, factor_of_4)
x =int(input("Enter your number"))
i = 0
while x > i:
    if x/1 or x/x == x or 1:
        print("This is a prime number")
    else:
        print("This is not a prime number")
name = ["Gbolahan", "ADE", "japelens", ]
for i in name:
    print(f"Hello {i} welcome to Heritage premium Akara and rosted corn spot, At Heritage spot you taste premium food and being served like a V.IP")
import random
guess = int(input("Guess a number"))
num = 10
i = 0
while guess > 1:
    if guess == num:
        print("your answer is correct")
        break
    else:
        continue
student_names = []
num_of_student = int(input("How many student are in the class "))
for i in range (num_of_student):
    name = input("enter student name ")
    student_names.append(name)
for name in student_names:
    student_names.index(name)
    print(name)
import math 
x = float(input("Enter the value of x "))
p = (math.sin(x)**2) + (math.cos(x)**2)
print(p)
a=float(input("input your value for a"))
b=float(input("input your value for b"))
import math
y=(math.sqrt(a**2+b)/(b+1))
print(y)
a=float(input("enter number of available oranges"))
b=float(input("enter the number of people"))
c= int(a//b)
print(c)
x = int(input("Enter your age "))
if x >= 18:
    print("welcome")
elif x >= 13:
    print("ife is a stupid boy")
else:
    print("oluwalonimi is good girl ")
count = 0
while count <= 5:
    print(count)
    count += 1
def my_print(txt):
    print(txt)
name = ["HERITAGE", "VIP", "DANIEL"]
for user in name:
    if user == "VIP":
        my_print(f"{user} - Very important person")
    else:
        my_print(user)
message = """
 Hello {name}, welcome to  Heritage premium Akara and rosted corn spot, At Heritage spot you taste premium food and being served like a V.IP to order visit {website}
 """#.format(name = "Daniel", website = "Vipakara.com")
def msg(my_name = "Heritage", my_website = "vipakara.com"):
    my_msg = message.format(name = my_name, website = my_website)
    print(my_msg)
student_scores = [
    {"name": "Heritage", "department": "Software Enginnering", "Level": "100 level"},
    {"name": "vip", "department": "computer science", "Level" :"100 level"},
    {"name": "Gbolahan", "department": "Data Science ", "Level": "100 level"},
    {"name": "Ade", "department": "Ict", "Level": "100 level"},
    {"name": "Jere", "department": "SLT", "Level" :"100 level"},
]
for student in student_scores:
    print(f"{student["name"]} your department is {student["department"]} you are in {student["Level"]}")
def my_function():
    print("Hello world")
msg = "hello {name}, {greeting}"
def greetings():
    print(greetings)
my_msg = msg.format(my_name = name, greetings = greetings )
print()
import math
num = 44.01
a = [1,2,3]
for x in a:
    a.remove(x)
print(a)
f = 4
case = "lower"
def clean_text(name):
    cleaned = name.lower().strip()
    print(cleaned)
clean_text("Heritage    ")
name = ["ola", "ife", "ade",]
print(name)
num=[1,2,3,4,5]
print(num)'''
x = 30
a = 0
while a >= 0:
    print("Hello world")
    if a == 2:
        break
    a+=1
    