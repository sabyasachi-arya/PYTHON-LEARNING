def double(x):
    return x * 2


sequence = [1, 3, 5, 7]
doubled = [double(x) for x in sequence]
print(doubled)

# Now using map function instead of list comprehension


def double_1(a):
    return a * 2


sequence_1 = [2, 4, 6, 8]
doubled_1 = map(double_1, sequence_1)
# map goes over each value in sequence_1 such as a list,tuple and set, and it applies the doubled_1 function on
# each element and return the final sequence back to you.

print(list(doubled_1))  # you need tho turn the map into a list to see its output otherwise the map will not return
# the list but will return a map object, see the line below
print(doubled_1)
# map is the counterpart of this  [double(x) for x in sequence] list comprehension
# map is vastly used , map function is also available other different programming languages such as
# javascript etc.

# Using Lambda function in map function:
sequence_2 = [3, 9, 18, 81]

doubled_2 = map(lambda x: x * 2, sequence_2)
print(list(doubled_2))
