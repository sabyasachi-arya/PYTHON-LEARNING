from libs import my_lib
#  ^^^^ This is a relative import because this is imported from a folder
# import libs.my_lib  # this also can be done instead of first import
# that's why these are Relative imports
# from .libs.operations import operator  # we can also do this instead of first line of import both are same
# with "." python is finding the project file as a path to find the libs then operations then importing operator.py
# But we can not do from .libs import my_lib because libs is itself pathfile, we do not need "."
# we can directly import my_lib from libs we do not need any relative import
print("code.py importing functions from: ", __name__)

# To perform a Relative Import we must use from and import keywords(Recommended)
