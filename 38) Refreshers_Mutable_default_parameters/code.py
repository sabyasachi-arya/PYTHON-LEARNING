from typing import List


class Student:
    def __init__(self, name: str, grades: List[int] = []):  # This is a bad idea
        # [] is default value , this is how we can set a default value of any parameter
        # now because we are  giving the default value to a list then self.grade is name for this specific []
        self.name = name
        self.grades = grades

    def take_exam(self, result):
        self.grades.append(result)


s_1 = Student("Saby")
s_1.take_exam(90)
print(s_1.grades)
s_2 = Student("Rohan")
print(s_2.grades)  # that should not be 90 because there is no .take_Exam() assigned with s_2
# when we create two students self.grades in both of them are names to the same list []
# so as long as you are using default parameter for all the students
# they will share the same grades [], and as we know earlier if we change a mutable value of two or more
# variable which are sharing the value, will have the same value or share the same grades
# lists are mutable so we should not use mutable value in parameter
# but if we pass in different list for each students then the variables are not using the same value
# which default [] empty list and each one has different list assigned to them as we know if
# two variable has different empty list assigned on their name then they will not share values
s_3 = Student("Sourav", [30, 66])
print(s_3.grades)
s_4 = Student("Dip", [50, 76])
print(s_4.grades)
