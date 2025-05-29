def hello():  # defining a function name hello
    print("Hello!")  # the main purpose of this callable variable hello()
# when you define a function, you create a callable variable.


hello()
# this is how to run a function.


def user_age_in_secs():
    user_age = int(input("Please enter your age: "))
    age_in_secs = user_age * 365 * 24 * 60 * 60
    print(f"Your age in seconds: {age_in_secs}")


user_age_in_secs()