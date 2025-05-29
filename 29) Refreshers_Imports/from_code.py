import libs.my_lib
# importing my_lib file from libs directory which is inside the project
# from_code.py is imported in to_code.py
# check to_code.py


def divide(dividend, divisor):
    if divisor != 0:
        return f"{dividend / divisor:.2f}"
    else:
        return f"You can not divide with 0"


print("Importing functions from : ", __name__)  # __name__ is a global variable in Python that changes depending on
# which file you are in , it will help you to differentiate the file you run and a file you import
# here the output of this __name__ will come __main__ because it is the main file where the __name__ is hardcoded.



