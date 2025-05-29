import functools  # short for function tools


def securing_admin_function(function):
    @functools.wraps(function)
    # ^^^^^^^^^^^^^^^^^^^^^^^^ this is going to tell secure_function that it is a wrapper for function
    # what this does that it keeps the name and the documentation of the get_admin_password() function
    def secure_function():
        if user["access level"] == "admin":

            return function()
        else:
            return f"No permission found for {user['username']}"

    return secure_function


@securing_admin_function  # here this is called the decorator
def get_admin_password():
    return "Saby1234"


user = {"username": "Saby", "access level": "admin"}
print(get_admin_password())
print(get_admin_password.__name__)