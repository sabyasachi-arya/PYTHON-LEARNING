users = [
    (0, "Rohan", "8733IND"),
    (1, "Saurabh", "9123638733IND"),
    (2, "Sab", "77777AND2IRM"),
    (3, "Abhi", "4723R2AND1")
]

username_mapping = {user[1]: user for user in users}


print(username_mapping["Sab"])
# this means giving the value "Sab" to user[1] in username_mapping and 'user for user in users' will give out
# the full user "Sab" tuple from users
