List = ["Saby", "Sourav", "Rohan"]
List.remove("Saby")  # .remove is used to remove particular element from the list
print(List)
# Another way of removing by just putting the subscript notation instead of writing the
# whole element value or name
List = ["Saby", "Sourav", "Rohan"]
List.remove(List[0])
print(List)
# _______________________________________________________________________________
Tuple = ("Saby", "Sourav", "Rohan")
# Tuple.remove("Saby")  # is wrong because tuple does not allow modification
# print(Tuple)
# remove # from the above lines to see the error
