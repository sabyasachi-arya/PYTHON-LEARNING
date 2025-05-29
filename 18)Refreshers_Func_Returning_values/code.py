def add(x, y):
    print(x + y)


add(10, 12)
result = add(10, 12)
# because his means result =  print(x + y) =  print(10 + 12)
print(result)  # This will give None as output because result variable is already printing out
#  add(10, 12) and print(result) means print(print(add(10, 12)))
print("-----------------------------")
# Now using returning value in function:


def sum_of_2(a, b):
    return a + b


result_1 = sum_of_2(10, 20)
print(result_1)