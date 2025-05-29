users = [
    (0, "Rohan", "8733IND"),
    (1, "Saurabh", "9123638733IND"),
    (2, "Sab", "77777AND2IRM"),
    (3, "Abhi", "4723R2AND1")
]

username_mapping = {user[1]: user for user in users}

username_input = input("Enter your username: ")
password_input = input("Enter your password: ")

_ID, username, password = username_mapping[username_input]  # check code.py and line no.16
# username_mapping[username_input] will give out an output like this (0, 'Rohan', '8733IND') after getting the username_input.
# (0, 'Rohan', '8733IND') also means 0, 'Rohan', '8733IND' ,
# because in every one output like this only a particular tuple is coming out and as we know in case of only
# tuple a () normal tuple brackets are not needed, or () these are just ignorable,
# that means three values are coming out as output from this: username_mapping[username_input]
# Ex: 0(user[0]), 'Rohan'(user[1]), '8733IND'(user[2]), so these three value will be assigned to three new variables
# Three variable is assigned such as _ID is an ignorable variable for IDs[user[0]],
# username for the user[1] and
# password for the passwords ex.:"8733IND"[user[2]]
if password_input == password:
    print(f"Welcome,{username_input}!")
else:
    print("Password does not match.")
# because for loop is inside of username_mapping[username_input], for every element tuple in user tuple list
# line 23 - 26 will run for every element ,
# what's going on:
# first username_input will get the username from the user
# second the password_input will get password from the user
# then the username will be used as subscript notation for username_mapping(Dictionary comprehension)
# such as username_mapping[username_input]
# then this username_mapping[username_input] will give three values ex: 0, 'Rohan', '8733IND' will come out
# for username_mapping["Rohan"]
# then these three values will be assigned to three new variables such as:
# _ID, username, password = username_mapping[username_input] = 0, 'Rohan', '8733IND'
# _ID, username, password = 0, 'Rohan', '8733IND'
# Now if the password_input variable and password variable which is retrieved from the particular username_input by
# the user and by doing username_mapping[username_input] this function , are matched then this string
# print(f"Welcome,{username_input}!") will print out.
# if these two variables(password and password_input) does not match then it will print out this:
# print("Password does not match.")
