def add(x, y):
    return print(f'{(x+y)} & {x-y}')


nums = (5, 15)
add(*nums)  # * distributes the arguments to each parameter by position

print("-------------------------------------")


def add(x, y):
    return f'{(x+y)} & {x-y}'


nums = {"x": 10, "y": 20}  # a dictionary for value for x and value for y
print(add(nums["x"], nums["y"]))
print(add(x=nums["x"], y=nums["y"]))  # even more specifically
print(add(**nums))  # this ** is getting two keys from nums dictionary and pass those two keys as
# named argument and the value is going to be the value associated with the key

