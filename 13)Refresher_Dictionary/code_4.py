friend_ages = {"Rohan": 26, "Sourav": 26, "Saby": 27}

if "Rohan" in friend_ages:
    print(f"Rohan is {friend_ages["Rohan"]} years old.")
else:
    print(f"Rohan is not a friend.")

age = friend_ages.values()
print(age)
# .values() is used to get values of each key in the dictionary,
# it creates another different list, it contains only the values of the key
# as you can see in the output
print(f"{(sum(age)/len(age)):.3f}")