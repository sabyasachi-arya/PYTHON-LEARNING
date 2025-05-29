# Advanced set operations
# Difference::
friends = {"Sourav", "Rohan", "Ishan", "Dip"}
friends_abroad = {"Sourav", "Rohan"}
# two different sets with some similar elements, as we know sets can not have
# duplicate items with that knowledge we can use .difference method
frds_nearby = friends.difference(friends_abroad)
# here the formula is {friends} - {friends_abroad}
# because the friends is a bigger set and friends_abroad is a smaller set
# bigger sets stays outside and smaller one stays inside the normal brackets
# so, we can use this formula otherwise if we do opposite we might get nothing
# because of removing the bigger set from smaller set leaves us nothing : check line no.15-18
print(frds_nearby)
# .difference , finds difference between two sets by determining the duplicate items
# or similar elements in the sets and creates a new set without the similar elements
friends = {"Sourav", "Rohan", "Ishan", "Dip"}
friends_abroad = {"Sourav", "Rohan"}
frds_nearby = friends_abroad.difference(friends)
print(frds_nearby)
# As you can see we just get an empty set of values because we minus bigger set from the
# smaller set here
