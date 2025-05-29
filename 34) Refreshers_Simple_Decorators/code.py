# def secure_function(): inside securing_admin_function(function): is called a decorator
def get_admin_password():    # this function returns the string value
    return "Saby1234"

# def secure_function(): inside securing_admin_function(function): is called a decorator


def securing_admin_function(function):    # this function is securing the admin and password
    # this function takes in a parameter called function where a function will be given as
    # an argument.
    # def secure_function(): inside securing_admin_function(function): is called a decorator
    def secure_function():  # this is another function inside a function which does not
        # take in any argument because it cas no parameter.
        if user["access level"] == "admin":  # if user's access level is "admin" then the
            # the argument function which was provided in the parameter function of
            # securing_admin_function will be returned, it will be called by ()
            return function()  # returning the callable function argument
        else:  # if user is not admin the code will print out this string value.
            return f"No permission found for {user['username']}"

    return secure_function  # the secure_function is not callable outside the securing_admin_function
    # and it does not take in any argument, it's job is to check weather the username is admin or not
    # and it's not called anywhere, so the def securing_admin_function(function): is getting
    # the secure_function in return.


user = {"username": "Saby", "access level": "admin"}  # user with username and access level keys and their values.

get_admin_password = securing_admin_function(get_admin_password)
# Now get_admin_password is equal to securing_admin_function(get_admin_password)
# that means the get_admin_password is protected and it is not called just the get_admin_password's value is
# securing_admin_function(get_admin_password)
# which simply means the new get_admin_password will have the value of old get_admin_password but after going through
# securing_admin_function.
# securing_admin_function takes a parameter called function and we are passing the get_admin_password function as
# the argument, then the secure_function(): inside of securing_admin_function checks the user set of keys and values
# from the keys it checks the value of "access level" and if the value of "access level" is "admin"
# then it returns the function and call it , function() is simply means get_admin_password() -> calling the function
# and at the end it is returning secure_function without calling it to the securing_admin_function(get_admin_password)
# now that means now get_admin_password = secure_function
print(get_admin_password())
# this line simply means secure_function() because get_admin_password = secure_function and calling
# get_admin_password means calling secure_function
# and why we are not returning the secure_function() in the line no.17 because if we call the function while
# returning it that means by checking the access level it will already give out a string value of either
# "Saby1234" or "No permission found for {user['username']}"
# while executing the get_admin_password() in line 37 means it will no more get a function in the replacement
# of get_admin_password but rather it will get the string value and then it will be simply means that
# get_admin_password() will going to call a string value like "Saby1234"() or
# "No permission found for {user['username']}"()
# these will be concluded as error and we will see an error in the output, so please put a () in line 17
# to see the error.
# def secure_function(): inside securing_admin_function(function): is called a decorator
