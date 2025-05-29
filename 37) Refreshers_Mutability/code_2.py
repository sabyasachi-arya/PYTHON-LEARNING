a = "hello"
b = a

a += " world"  # here "a"'s value is getting reassigned a = a + " world"
# and it is happening after "b" is assigned with a so "b" still means previous "a"
# "a"s value was changed  after b was assigned with "a", so only "a"s value will be changed
print(a)
print(b)
