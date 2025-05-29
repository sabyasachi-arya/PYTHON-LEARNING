def securing_admin_function(function):

    def secure_function():
        if user["access level"] == "admin":

            return function()
        else:
            return f"No permission found for {user['username']}"

    return secure_function


@securing_admin_function
def get_admin_password():
    return "Saby1234"


user = {"username": "Saby", "access level": "admin"}
# get_admin_password = securing_admin_function(get_admin_password)
# we no longer need this line of coding because if you put at,"@" syntax in top of a function that will prevent
# the function from being created as is instead it will create it and pass it through the decorator directly
# Simply means we are no longer creating another new variable get_admin_password with and replacing it with
# secure_function but the @securing_admin_function is directly taking the get_admin_function() and replacing it
# with secure_function(). And when we are calling get_admin_password() we are now calling secure_function()
# directly.
print(get_admin_password())
# But there is a problem with decorators as a whole when we replace the function get_admin_password() with
# secure_function() , the name of the function also changes, the get_admin_password as a name and it's
# features still exist in Python but it is no longer registered as function internally, now secure_function() is
# now registered as an internal function, that means get_admin_password() name is also replaced by secure_function()
# and now some libraries of python will use that name .
print(get_admin_password.__name__)
# Here you will see the name of that function has been changed to secure_function
# So, to solve this problem we must do something ,we will see that in code_2.py
