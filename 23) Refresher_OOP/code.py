# Object Oriented Programming:

# A CODE WITHOUT OOP:

student = [{"name": "Rohan", "grades": (73, 97, 88, 67, 84)},
           {"name": "Sourav", "grades": (77, 47, 98, 87, 82)},
           {"name": "Saby", "grades": (75, 99, 48, 67, 77)}
           ]


def average(sequence):
    return sum(sequence) / len(sequence)


print(average(student[0]["grades"]))
print(average(student[1]["grades"]))
print(average(student[2]["grades"]))

print("-------------------------------------------------------------------")
# A CODE WITH OOP:


class Student:   # class name starts with capital letter(not necessary but recommended)
    def __init__(self):     # recommended name self but can be named anything
        # __init__ is a special method, it is not function because it's inside a class
        self.name = "Rohan"
        self.grades = (73, 97, 88, 67, 84)
        # it is accessing the name property inside of self because self "." name, means inside

    def avg(self):
        return sum(self.grades)/len(self.grades)

# What Is the __init__ Method in Python?
# The __init__ method is an instance method that is responsible for
# initializing a newly created instance (object) of a class.
# The method takes the object as its first argument (self),
# followed by any additional arguments that need to be passed to it.


student = Student()
print(student.name)
print(student.grades)
print(student.avg())
# ^^^^^^^^^^^^^^^^^
# print(Student.avg(student)) # both are same but the line 43 is a little longer and this is
# easy step to run the avg
