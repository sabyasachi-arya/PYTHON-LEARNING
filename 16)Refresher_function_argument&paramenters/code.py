def add(x, y):  # def add has two parameters x and y
    print(x + y)


add(12, 25)   # here 12 and 25 are two arguments for two parameters
# two parameters mean this add function has two variables called x and y
# two arguments means two values two variables(parameters)

print("-------------------------------------------------------------------")


def full_name(name, surname):
    print(f"{name} {surname}")


full_name("Sourav", "Bose")  # These are also known as positional arguments
full_name("Rohan", "Mondal") # These are also known as positional arguments
full_name(surname="Bhattacharjee", name="Sabyasachi")  # These are known as named or keyword arguments
