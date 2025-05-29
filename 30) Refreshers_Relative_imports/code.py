import importable_1  # this is not Relative import
# but here we cannot do import .importable_1 because this is not in a folder
print("code.py: ", __name__)

# To perform a Relative Import we must use from and import keywords(Recommended)
