def divide(dividend, divisor):
    if divisor != 0:
        return print(dividend/divisor)
    else:
        return print("You dumb! something is cannot be divided by zero.")


divide(10, 0)


# another way but longer process:
def divide(dividend, divisor):
    if divisor != 0:
        return dividend/divisor
    else:
        return "You dumb! something is cannot be divided by zero."


result = divide(120, 6)
print(result)
# --------------------------------------------
# another way but smart with more features:


def divide_1(dividend_1, divisor_1):
    if divisor_1 != 0:
        return print(f"Your answer is: {dividend_1 / divisor_1}")
    else:
        return print("You dumb! something is cannot be divided by zero.")


divide_1(dividend_1=int(input("Enter first number: ")), divisor_1=int(input("Enter second number: ")))
