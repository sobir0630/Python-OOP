from termcolor import colored

class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
       
students = [     
    student("Ali", 18),
    student("Vali", 25),
    student("Hasan", 38),
    student("Husan", 38),
    student("Karim", 14)
]


max_age = max(students, key=lambda student: student.age)
print(f"eng kattai student {colored(max_age.name, 'blue')} yoshi {colored(max_age.age, 'blue')}")

