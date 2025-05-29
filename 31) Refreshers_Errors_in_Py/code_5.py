def divide(dividend, divisor):
    if divisor != 0:
        return dividend / divisor
    else:
        raise ZeroDivisionError("Divisor can not be zero.")


grades = []
# grades = [10, 20, 30, 40, 70]  # copy the list to see the other output

try:
    avg = divide(sum(grades), len(grades))  # try to run this
except ZeroDivisionError as error:
    print(f"There is no element in your list 'grade'.")  # if error happens it will run this
    print(error)
else:
    print(f"Average of Grades: {avg}")  # if no error happens 'else' will run this
finally:
    print("Go away now.")  # to run a piece of code no matter if there is an error or not


# more examples of errors such as : TypeError, ValueError, RuntimeError etc.
