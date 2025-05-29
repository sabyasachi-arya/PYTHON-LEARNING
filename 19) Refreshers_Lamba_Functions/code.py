# a normal function:
def add(x, y):
    return x + y


print(add(10, 22))
# Now writing the same function with LAMBDA

add_1 = lambda x, y: x + y  # This is how you write a lambda function
# ^^^^   ^^^   ^^^^  ^^^^^^
#  |     |       |        |
#  |     |       |      Formulas / equation
#  |     |     Variables/parameters
#  |  lambda function
# function name

# Lambda function generally does not require return

print(add_1(100,262))

# another way of defining and executing lambda functions:

(lambda a, b: a - b)(10, 5)  # <<<< in lambda we can put arguments right beside of lambda function
print((lambda a, b: a - b)(10, 5))




