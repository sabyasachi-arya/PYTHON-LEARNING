# A piece of code without errors:
def divide(dividend, divisor):
    if divisor != 0:
        return print(dividend / divisor)
    else:
        return print("You can not divide something with zero.")


a = int(input("Enter dividend: "))
b = int(input("Enter divisor: "))
divide(a, b)

grades = [59, 79, 87, 45, 90]
divide(sum(grades), len(grades))

