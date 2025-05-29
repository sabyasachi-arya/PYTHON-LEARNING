people = [("Rohan", 26, "PhD"), ("Avishek", 28, "M.R"), ("Sourav", 26, "C.A")]

for name, age, prof in people:
    print(f"{name} is {age} years old and is a {prof}.")
print("--------------------------------------------------------------")
# with some less destructuring:
for name in people:
    print(f"{name[0]} is {name[1]} years old and is a {name[2]}.")
