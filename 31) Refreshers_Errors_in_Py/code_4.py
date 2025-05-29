# A piece of code with errors only:
def divide(dividend, divisor):
    if divisor != 0:
        return print(dividend / divisor)
    else:
        raise ZeroDivisionError("Divisor can not be zero.")


grades = []

try:
    divide(sum(grades), len(grades))
except ZeroDivisionError as error:  # as error or whatever we can call it ,what it does is that it creates
    # a variable called error and put inside the value of the error we used if there is one like in here it's
    # "Divisor can not be zero"
    print(f"There is no element in your list 'grade'.")
    print(error)
