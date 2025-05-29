h, *t = [1, 2, 3, 4, 5]
print(h)
print(t)
# similarly
print("----------")
a, b, *z = [7, 8, 9, 10, 11]
print(a)
print(b)
print(z)
# * before a variable means it is going to contain all the other values which are unused
# here a and b are designated to 7 and 8 so, from after 8 all the other values are stored in z
print("--------------")
*e, f = [7, 8, 9, 10, 11]
print(e)
print(f)
# if the first designated variable is with * then all the other value except the last one will
# be stored to e and last value will be stored to f
print("--------------")
*e, g, f = [7, 8, 9, 10, 11]
print(e)
print(g)
print(f)
# similarly g and f will be last two values and *e will contain all the previous values
print("--------------")
*e, g, f = [7, 8, 9, 10, 11]
print(*e)
print(g)
print(f)
# printing the *e will not give the list as output, it will give out normal value like f and g
