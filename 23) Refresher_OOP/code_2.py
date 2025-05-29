class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def avg(self):
        return sum(self.grades)/len(self.grades)


student = Student("Rohan", (73, 97, 88, 67, 84))
student_2 = Student("Sourav", (77, 47, 98, 87, 82))

print(student.name)
print(student.grades)
print(student.avg())

print(student_2.name)
print(student_2.grades)
print(student_2.avg())
