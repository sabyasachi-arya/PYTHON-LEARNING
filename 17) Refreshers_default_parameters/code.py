# Default parameter values
def add(x, y=10):  # here y=10 is default parameter value, but x has no default value
    print(x + y)


add(10)
# so if we put an argument in add, that argument will be inserted into x because x is empty
add(x=12)  # we can also use named argument to provide the value to x
# add(x=12, 10) # can not be done because positional argument can not exist after named argument
print("-------------------------------------------------------------------------------------------------")


def add(x, y=10):  # here y=10 is default parameter value, but x has no default value
    print(x + y)


add(10, 15)
# now the new value of y is 15, and the default value of y is overwritten
add(x=14, y=13)
# also both named arguments can be used and y=10 default value is now y=13
# add(x=14, y)  # this cannot be done because if the first argument is a named arg and
# has a value then second one must have a value
