grades = [87, 77, 76, 75, 47]
total = 0
amount = len(grades)  # to the number of elements in a list

for g in grades:
    total += g  # similar doing: total = total + grade
    # add the elemental value of each element to the total variable for every element in the list
print(total / amount)  # average

# now the new total holds the value of which for loop added for every element to the total
