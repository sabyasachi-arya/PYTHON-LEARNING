from from_code import divide   # here we are bringing the particular function divide form, from_code.py
# import from_code  # it's also can be done ,does same thing it brings all the functions and classes inside the
# from_code
print(divide(100, 10))
# from_code.py:  from_code
# this output will appear because print("Importing functions from : ", __name__) was hardcoded in from_code.py
# if we use __name__ in this file it will also say __main__
# conclusion: __name__ will the name of the file where the __name__ is hardcoded
# print(__name__)  # Remove # to see
# therefore the functions of my_lib.py is imported in from_code.py and from_code.py is imported in this file
# so the functions of my_lib.py & from_code.py are imported in this file altogether
# by checking the output we can see __name__ of my_lib.py and __name__ of from_code.py
