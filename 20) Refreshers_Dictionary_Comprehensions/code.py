users = [
    (0, "Rohan", "8733IND"),
    (1, "Saurabh", "9123638733IND"),
    (2, "Sab", "77777AND2IRM"),
    (3, "Abhi", "4723R2AND1")
]  # List of Tuples

username_mapping = {user[1]: user for user in users}  # user[1]=key and user for user in users = value
# user[1] means the name of every user ex: "Rohan", "Saurabh"
# where user for user in users means (put user for every user in users list)
# in a dictionary comprehension the value that you are going to put into your new dictionary
# is actually a key and value pair
# what is this doing is getting the username of every user element tuple and associating with it
# the entire user tuple for each of the user tuple
print(username_mapping)
print(username_mapping["Rohan"])





