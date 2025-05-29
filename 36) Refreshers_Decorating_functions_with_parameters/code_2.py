# Decorators with parameters:

import functools  # short for function tools


def new_decorator(access_level):  # new_decorator is another function which contains
    # def securing_admin_function(function): and which contains def secure_function(*args, **kwargs):
    # this function takes in an argument for the parameter = access_level
    def securing_admin_function(function):  # then this function takes in an argument which is function
        @functools.wraps(function)  # wrapping the function with functools so that it keeps it's name
        def secure_function(*args, **kwargs):  # takes in multiple positional and keyword argument
            if user["access_level"] == access_level:  # if user's access_level key is same with the argument of
                # new_decorator(access_level) then it is going to return the function which is
                # get_admin_password for get_admin_password():
                # get_user_password for get_user_password():
                return function(*args, **kwargs)
            else:  # if the user's access_level key is not same with the argument of then this string will return
                return f"No {access_level} permission found for {user['username']}"

        return secure_function  # then this function will be returned without calling it will be called by
    # print(get_user_password()) or print(get_admin_password())

    return securing_admin_function  # then at the end this function will be returned without calling
    # it will be called by:
    # print(get_user_password()) or print(get_admin_password())


@new_decorator(access_level="admin")  # here this is called the decorator with parameter
# that means def new_decorator(access_level= "admin"):
def get_admin_password():
    return "Saby_1234"
# if the user["access_level"] is "admin" then this function will be returned


@new_decorator(access_level="guest")
def get_user_password():
    return "User1234"
# if the user["access_level"] is "guest" then this function will be returned


user = {"username": "Saby", "access_level": "admin"}  # 1st user with access_level = "admin"

print(get_user_password())  # now the get_user_password function has access_level="guest" in its decorator parameter
# so the user's "access_level" key will be checked and as we can see it's not "guest" , it's "admin", so, the
# user["access_level"] == access_level is not true that's why it will return this following string:
# "No {access_level} permission found for {user['username']}" = No guest permission found for Saby

print(get_admin_password())  # now the get_admin_password function has access_level="admin" in its decorator parameter
# so the user's "access_level" key will be checked and as we can see it's "admin", so, the
# user["access_level"] == access_level is true that's why it will return this following: "Saby_1234"

print('--------------------------------------')

user = {"username": "Rohan", "access_level": "guest"}  # 2nd User with access_level = "guest"

print(get_user_password())  # now the get_user_password function has access_level="guest" in its decorator parameter
# so the user's "access_level" key will be checked and as we can see it's "guest" , it's not "admin", so, the
# user["access_level"] == access_level is true that's why it will return this following : "User1234"

print(get_admin_password())  # now the get_admin_password function has access_level="admin" in its decorator parameter
# so the user's "access_level" key will be checked and as we can see it's "guest", not "admin", so, the
# user["access_level"] == access_level is not true that's why it will return this following string:
# "No {access_level} permission found for {user['username']}" = No admin permission found for Rohan
