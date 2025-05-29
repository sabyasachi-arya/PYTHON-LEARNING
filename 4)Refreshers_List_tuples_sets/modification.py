List = ["Saby", "Sourav", "Rohan"]
print(List)
List[0] = "Ishan"  # you can modify a list, here the first element of the list will be replaced by
# new value entered for [0]
print(List)  # in the new modified list you will see the modified value of [0] has replaced
# the older [0] element of the list
# _________________________________________________________________
Tuple = ("Saby", "Sourav", "Rohan")
print(Tuple)
# Tuple[0] = "Ishan" # <--------- Remove the # to see the error
# As we have learned before we can not modify tuple , if we do try to modify tuple
# we will get an error, remove the # from the above and below line to see the error
# print(Tuple)  # <--------- Remove the # to see the error
# ---------------------------------------------------------------------
Set = {"Saby", "Sourav", "Rohan"}
print(Set)
# Set[0] = "Ishan"  # This is also wrong because set does not allow subscript notation
# Remove the # from the above line to see the error
