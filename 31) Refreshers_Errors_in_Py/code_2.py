# A piece of code with errors and traceback:
def divide(dividend, divisor):
    if divisor != 0:
        return print(dividend / divisor)
    else:
        raise ZeroDivisionError("Divisor can not be zero.")
    # creating an error/exception , ZeroDivisionError is built-in Python Error class that we can use.
    # we have to use raise keyword to raise an error in output and the string attached to the error class
    # can be modified. This error will give a traceback meaning in which lines the error occurred
    # it can be useful to debug or correction of the code
    # example: line 13, in <module>divide(sum(grades), len(grades))
    # line 5, in divide raise ZeroDivisionError("Divisor can not be zero.")


grades = []
divide(sum(grades), len(grades))