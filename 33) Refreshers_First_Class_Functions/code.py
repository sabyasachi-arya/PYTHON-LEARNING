def divide(dividend, divisor):  # the formula function
    if divisor == 0:
        raise ZeroDivisionError("Divisor can not be zero.")

    return dividend / divisor


def calculate(*values, operator):   # another function to indirectly call the divide function
    # without directly putting arguments and calling divide function
    # *values can take multiple amount of arguments
    return operator(*values)


result = calculate(45, 5, operator=divide)  # here we are calling calculate function with two positional
# arguments and one name arguments, here we are not calling the divide function we are just telling Python that
# operator is equal to divide, operators value is now divide
# this is an example of using first class function
# operator is now the divide function and in line 11 return operator(*values)
# simple means that divide(45, 5), and we can only pass two positional arguments
# because divide chas only two parameters
print(result)
