day_of_week = input("What day is it today? ")

print(day_of_week == "Monday")

# Now the same operation with If Statements, If statements can help to increase the numbers of operations
# and to increase features of a code
day_of_week = input("What day is it today? ")

if day_of_week == "Monday":
    print("Yes!, You are right, Today is Monday.")
# _______________________________________________________________________________________
# Now using Else statements, Else statements are used to increase the number of features of a programme,
# like if not this then this(else), Else can only be used when the "if" statements  is used:
# like you will see in the last code if you type something apart from monday, the code gives out nothing,
# this problem can be solved by else:
day_of_week = input("What day is it today? ")

if day_of_week == "Monday":
    print("Yes!, You are right, Today is Monday.")
else:
    print("No, It's Monday today.")
# _______________________________________________________________________________________________
# Now using Elif statement to bring more features into the code:
day_of_week = input("What day is it today? ")

if day_of_week == "Monday":
    print("Yes!, You are right, Today is Monday.")
elif day_of_week == "Tuesday":
    print("Nope! Tomorrow is Tuesday, today is Monday!")
else:
    print("No, It's Monday today.")
