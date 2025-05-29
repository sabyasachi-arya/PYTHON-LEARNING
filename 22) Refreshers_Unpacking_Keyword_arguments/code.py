# Unpacking Keyword arguments:

def name_age(**kwargs):   # kwargs is a default parameter name by python, which just simply
    # means keyword-arguments, kwargs is a default name, anything can be used as name
    print(kwargs)

# ** is used to collect several keyword arguments such as , age=27.
# ** collects all the keyword arguments and put into a dictionary where the dictionary key is the
# name of the argument so end up with a name key with a value: Sabyasachi and age key with
# numeric value.


name_age(name="Sabyasachi", age=27)  # So basically it will create a dictionary out of named
# arguments
print("------------------------------------------")
# and also you can do the other way around, you can unpack a dictionary into named arguments


def named(name, age):
    print(name, age)


details = {"name": "Rohan", "age": 26}

named(**details)
# _______________________________________________________
def named(**kwargs):
    print(kwargs)


details = {"name": "Rohan", "age": 26}

named(**details)
