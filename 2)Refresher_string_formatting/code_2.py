# other ways of string formatting
name = "Saby"
greeting = "Hello,{}!"
full_greet = greeting.format(name)
print(full_greet)
print("--------------------------------")
# direct approach
name = "Saby"
greeting = "Hello,{}!!!!!".format(name)
print(greeting)
print("--------------------------------")
# even more direct approach
name = "Saby"
greeting = "Hello,{}!!!!!my boi"
print(greeting.format(name))
print("--------------------------------")
# even more & more direct approach
greeting = "Hello,{}!,my boi"
print(greeting.format("Saby"))
print("--------------------------------")
# even more direct approach
name = "Saby"
greeting = "Hello,{}!!!!!my boi"
print(greeting.format(name))
print("--------------------------------")
# most direct approach(without any variable)....
print("Hello,{}!".format("Rohan"))
