def add(x, y):
    print(x + y)
    return x - y


add(50, 45)  # because add function has print func inside of it, it's going to
# print out the x + y for this above line.
print(add(90, 45))  # because now we are printing the add function
# because add function has print inside
# the print function is going to print out x + y ,and because there is return x - y in add also
# and we are printing the add function so the x - y is getting printed out
