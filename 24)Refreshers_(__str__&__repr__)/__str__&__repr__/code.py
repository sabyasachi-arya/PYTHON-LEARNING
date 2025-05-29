# starting and ending with "__" is known as special method:
# __str__ and __repr__

class Person:  # class
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):  # __str__ is a special method ,used to return a string from class
        return f"Your name is {self.name} and you are {self.age} years old."

    def __repr__(self):
        return f"<{self.name},{self.age}>"   # __repr__ has same features like __str__ but usually used to
    # show strings which are meant to see for the other programmers or for debugger
    # usually python ignores __repr__ if a __str__ is used and getting printed out , and python thinks that
    # it is meant for users to see the __str__ string not the __repr__ string.

sab = Person("Saby", 27)  # object
print(sab)  # and must use print function to print out string that has been returned by the class

print("---------------------------------------------")


class Person2:  # class
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"<{self.name},{self.age}>"   # here you will be able to __repr__ string


rohan = Person2("Rohan", 26)  # object
print(rohan)  # and must use print function to print out string that has been returned by the class
print(rohan.__repr__())
