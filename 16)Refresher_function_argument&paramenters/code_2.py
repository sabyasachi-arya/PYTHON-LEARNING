def divide(dividend, divisor):  # 10/2 = 5 here 10 is dividend, 5 is divisor
    if divisor != 0:
        print(dividend / divisor)
    else:
        print("You can not divide something with 0")


divide(100, 25)  # with both positional argument
divide(dividend=40, divisor=5)  # with both named argument
divide(30, divisor=10)  # with one positional argument and one named argument,
# but cannot be done other way around or else we will encounter an error
# divide(dividend=30, 10)  # if we do this we will encounter an error
divide(100, 0)
