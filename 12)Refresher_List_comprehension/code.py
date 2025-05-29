# This is an example of short code where a list called nums with 3 elements,
# and a empty list called double, our main objective is to fill up the empty list with
# the elements of the nums list but those value will be doubled:
nums = [1, 3, 7]
double = []

for num in nums:
    double.append(num*2)

print(double)

# --------------------------------------------------------
# Now with list comprehension:
nums = [4, 23, 77]
double = [n * 2 for n in nums]
print(double)

