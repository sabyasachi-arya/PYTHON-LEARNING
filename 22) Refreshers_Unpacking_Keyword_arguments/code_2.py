def name_age(**kwargs):
    print(kwargs)


def print_nicely(**kwargs):
    name_age(**kwargs)
    for arg, value in kwargs.items():
        print(f"{arg}: {value}")


print_nicely(name="Saurabh", age=26)