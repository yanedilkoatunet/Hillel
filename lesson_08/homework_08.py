class Student:
    def __init__(self, name, surname, age, average_grade):
        self.name = name
        self.surname = surname
        self.age = age
        self.average_grade = average_grade

    def change_average_grade(self, new_grade):
        self.average_grade = new_grade

student = Student ("Liza", "Nedilko", 22, 4.5)
print(student.name)
print(student.surname)
print(student.age)
print(student.average_grade)

student.change_average_grade(5)

print(student.average_grade)
