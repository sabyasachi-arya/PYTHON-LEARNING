frns_abroad = {"Sourav", "Rohan"}
frns_nearby = {"Dip", "Ishan"}
all_friends = frns_abroad.union(frns_nearby)
# .union adds two sets together
print(all_friends)
# ----------------------------------------------
sub_sci = {"Rohan", "Saby", "Dip"}
sub_business = {"Sourav", "Ishan", "Saby"}
all_sub = sub_business.union(sub_sci)
print(all_sub)
# because sets do not contain duplicate items same items from both the sets will be
# conuted as one