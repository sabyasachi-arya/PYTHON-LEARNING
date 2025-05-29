a = []  # a = empty list
b = a  # b = a which means b = a = [](same empty list)

print(id(a))  # prints out the id of the allocated memory for the empty list
print(id(b))  # prints out the id of the allocated memory for the a
# because a and b are both have a value of same empty list so their id of allocated space will be
# one and same
print("----------------------------------")

c = []  # c is an empty list
d = []  # d is a different empty list
print(id(c))
print(id(d))
# because cand d are not same empty list that's whu they both have different allocated place in memory
# and that's why they have unique ids of allocation
print("----------------------------------")

e = []
f = e  # e and f are same empty list
e.append(10)  # appending e means f will also be appended
f.append(20)  # and appending f means e will also be appended
print(e)
print(f)

print("----------------------------------")
# so we can change a list after we have created it means that a list is mutable.
# some values are can not be changed that are called immutable.
# ex:
a = (10, 12)  # is a tuple
b = (20, 15)  # is a tuple
# tuples can not be modified after creating neither we can append or modify anyhow
print(id(a))  # memory allocation id of a

a = a + (15,)  # we are not adding an element in 'a' tuple but rather we are creating a new tuple which is now called
# 'a'
print(a)
print(id(a))  # now the id of 'a' will be different because python has created new place for this new tuple
# that's why tuples are immutable because it can not be modified or changed
print("------------------------------")
g = 9.87
h = 9.87

print(id(g))
print(id(h))
# Python has an optimization that already knows when an integer is created,
# it won't be recreated if another identical is getting used
# so there allocation id will be same
# That's why it behaves different than empty list
print("------------------------------")
h = 9.86
print(id(g))
print(id(h))
# changing h will not change g because integers are immutable and g and h are different variable even
# though they have same value but when we change h, h and g are not sharing the same value anymore
# that's why now their allocation space will be different
