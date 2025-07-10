class student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
students = student("Ali", 18, 9)
print(f"student: name {students.name} age {students.age} grade {students.grade}")