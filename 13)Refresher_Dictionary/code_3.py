friend_ages = {"Rohan": 26, "Sourav": 26, "Saby": 27}


for f in friend_ages:
    print(f)  # prints out friends names
print("----------------------------------------------")
for f in friend_ages:
    print(f"{f}: {friend_ages[f]} years old.")
print("----------------------------------------------")
for f, a in friend_ages.items():  # .items keyword helps to create 2 or more
    # separate variables for each key and value
    print(f"{f}: {a} years old.")

