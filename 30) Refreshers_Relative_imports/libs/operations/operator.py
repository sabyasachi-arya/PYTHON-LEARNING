print("my_lib.py importing functions from: ", __name__)

# from this file we can do relative import because it's in the same folder named libs in which the operation
# folder is in and in operation folder operator.py exist
from ..my_lib import *
# ^^^^^^^ this can also be done
# two dots because libs is in the core project folder and then my_lib is inside of libs
# so, it is a two level deep import, and we can not do
# .my_lib import *  # here we will get an error because it has one dot . but it is a two level deep import
# that simply means import everything (* stands for) from the path
