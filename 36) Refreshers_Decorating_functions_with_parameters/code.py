import functools  # short for function tools


def securing_admin_function(function):
    @functools.wraps(function)
    def secure_function(*args, **kwargs):  # this can take multiple amount of positional arguments and keyword arguments
        # because the get_password function is getting replaced with this secure_function and
        # get_password has one argument with it so, we need to put these *args, **kwargs in parameter
        # so that secure_function() can take as many arguments as get_password has passed
        # and *args for any number of positional arguments and **kwargs for any number keyword arguments
        if user["access level"] == "admin":
            return function(*args, **kwargs)  # will return function the with the arguments
        # because this secure_function is returning the function and get_password has arguments
        # so the function which is getting return must have a method that can take arguments
        else:
            return f"No permission found for {user['username']}"

    return secure_function


@securing_admin_function  # here this is called the decorator
def get_password(panel):
    if panel == "admin":
        return "Saby1234"
    elif panel == "guest":
        return "super_secure_password"


user = {"username": "Saby", "access level": "admin"}
print(get_password("admin"))
print(get_password.__name__)