def multiply(*args):
    print(args)
    total = 1
    for arg in args:
        total = total * arg

    return total


def apply(*args, operator):
    if operator == "*":
        return multiply(args)
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator provided to apply()"


print(apply(1, 3, 5, 7, operator="+"))

print(apply(1, 3, 5, 7, operator="*"))
# why the output is different of operator="+"
# is because the in operator="+" the args are getting summed by sum(args) because
# sum(args) getting separates values from a value sets of apply(1, 3, 5, 7, operator="+")
# but multiply(args) is not getting values from the value set of apply(1, 3, 5, 7, operator="*")
# but rather its getting a whole tuple as value like line-2 and also can be seen in output
# it's getting passed a packed argument like tuple not getting separate arguments to multiply
# total = total + arg where total is 1 and 1 * (1, 3, 5, 7) = (1, 3, 5, 7)


# solution by unpacking arguments:


def multiply_1(*args):
    print(args)
    total = 1
    for arg in args:
        total = total * arg

    return total


def apply_1(*args, operator):
    if operator == "*":
        return multiply_1(*args)  # unpacking the arguments into four values
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator provided to apply()"


print(apply_1(1, 3, 5, 7, operator="*"))