default_y = 12


def add(x, y=default_y):
    print(x + y)


add(x=15)

default_y = 20
add(x=15)
# changing a variable that has been used as a default parameter value does not modify the function
# so the value of default_y = 12 is defined when the function gts created, it can not be changed after that
# even after re-assigning variable again, so it is not recommended to be done ,
# and it is recommended to put value inside the parameter or in the function call
