friends = ["Modi Ji", "Mamata Didi", "Elon", "Jeff", "Trump", "Messi", "Bill"]
starts_w_m = []

for f in friends:
    if f.startswith("M"):  # a keyword .startswith to check if something is starting with user preference,
        starts_w_m.append(f)

print(starts_w_m)


# -----------------------------------------------------------------------------------
new_friends = ["Modi Ji", "Mamata Didi", "Ronaldo", "Rahul", "Trump", "Messi", "Rohan"]

starts_w_r = [f for f in new_friends if f.startswith("R")]
print(starts_w_r)

# to print ID of the particular lists :(every list holds a different id in the memory because
# for every list python creates a new list in the memory
print(f"new_friends: {id(new_friends)},"
      f"starts_w_r:{id(starts_w_r)}")
