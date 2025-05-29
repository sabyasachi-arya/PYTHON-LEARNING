from typing import List
# before using type hinting list we need to import List from typing
# this are the in build python features files


def list_avg(seq: List) -> float:
    # Type hinting where seq(is parameter): List ,this means the arguments will be a list
    # -> float means the function list_avg will return a float value
    return sum(seq)/len(seq)