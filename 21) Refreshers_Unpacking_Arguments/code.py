def multiple_value_in_a_single_parameter(*args):
    print(args)  # gives a tuple of arguments
    print(*args)  # gives the arguments normally


multiple_value_in_a_single_parameter(1, 4, 6, 7)
# *args means multiple arguments(values) can be provided into single parameter
# *args is just python default name for the parameter, we can name it whatever we want
# such *what_ever_we_want


def multiple_value_in_a_single_parameter(*what_ever_we_want):
    print(what_ever_we_want)
    print(*what_ever_we_want)


multiple_value_in_a_single_parameter(13, 16, 56, 45)