List = ["Saby", "Sourav", "Rohan"]
List.append("Ishan")  # append means to add an element into the list of values,
#  append means appending the list
print(List)
# ___________________________________
# Duplicate Items(below):
# If we add two duplicate elements into a list, because list can contain duplicate items
# therefore we will be able to see same elements twice or more than one time in a list
List = ["Saby", "Sourav", "Rohan"]
List.append("Ishan")
List.append("Rohan")
print(List)
# ____________________________________________________________________________
Tuple = ("Saby", "Sourav", "Rohan")
# Tuple.append("Ishan")  # Tuple does not allow any kind of modification
# ______________________________________________________________________________
Set = {"Saby", "Sourav", "Rohan"}
Set.add("Ishan")  # That's how you add element into a set of values
print(Set)  # because there is no order in set, or set does not follow user order of value sets
# that's why the output will be in different order but a new element will be added
# ________________________________________________________________
# Duplicate Items(below):
Set = {"Saby", "Sourav", "Rohan"}
Set.add("Ishan")
Set.add("Ishan")
print(Set)
# In sets duplicate elements can not coexist
# so if we add two same elements then it only considers it as a one element


