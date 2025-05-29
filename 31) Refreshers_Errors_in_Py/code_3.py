# A piece of code with errors only but not tracebacks:
def divide(dividend, divisor):
    if divisor != 0:
        return print(dividend / divisor)
    else:
        raise ZeroDivisionError


grades = []

try:
    divide(sum(grades), len(grades))  # try keyword will try to perform this function first
except ZeroDivisionError:       # if a ZeroDivisionError happens or if the try kw finds a ZeroDivisionError in
    # the function while executing it then except will perform to raise the error 
    print(f"There is no element in your list 'grade'")
