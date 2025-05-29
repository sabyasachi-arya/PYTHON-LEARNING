# Fixing the previous problem:
from typing import List, Optional


class Student:
    def __init__(self, name: str, grades: Optional[List[int]] = None):  # assigning the default parameter
        # to None
        self.name = name
        self.grades = grades or []  # if the grades is None then empty list , if the grades has
        # list or value then List[int]
        # and Optional is doing making List[int] as optional
        # like: List of integer is optional but None is default value
        # if List[int] is not received through arguments then None will be passed

    def take_exam(self, result):
        self.grades.append(result)


s_1 = Student("Saby")
s_1.take_exam(90)
print(s_1.grades)
s_2 = Student("Rohan")
print(s_2.grades)