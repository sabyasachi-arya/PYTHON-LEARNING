from libs.operations import operator
# ^^^^ This is a relative import because this is imported from a folder
# import libs.operations.operator  # this also can be done instead of first import
# that's why these are Relative imports
# from .operations import operator  # we can also do this instead of first line of import both are same
# .operations means python will use this "." to use this same folder as path to find and import the
# operator.py file

print("importable_1.py importing functions from: ", __name__)

# from this file we can do relative import because it's in a folder named libs

# To perform a Relative Import we must use from and import keywords(Recommended)

