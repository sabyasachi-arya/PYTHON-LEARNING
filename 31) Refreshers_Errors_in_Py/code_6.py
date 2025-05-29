def divide(dividend, divisor):
    if divisor != 0:
        return dividend / divisor
    else:
        raise ZeroDivisionError("Divisor can not be zero.")


students = [
    {"name": "Rohan", "grades": [89, 78]},
    {"name": "Sab", "grades": []},   # copy & paste this [77, 87] to see other output
    {"name": "Saurabh", "grades": [67, 65]}
]

try:
    for s in students:
        name = s["name"]
        grades = s["grades"]
        avg = divide(sum(grades), len(grades))
        print(f"{name} has a average of {avg}")
except ZeroDivisionError:
    print(f"Error: {name} has no grades.")
else:
    print("--All Students average Calculated.--")
finally:
    print("Thank you!")