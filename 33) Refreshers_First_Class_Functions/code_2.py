def search(seq, exp, finder):  # finder is an example of using first class function
    for e in seq:
        if finder(e) == exp:
            return e

    raise RuntimeError(f"Could not find : {exp}")


friends = [
    {"name": "Rohan", "age": 26},
    {"name": "Sourav", "age": 26},
    {"name": "Saby", "age": 27}
]


def get_friend_name(e):
    return e["name"]


print(search(friends, "Saby", get_friend_name))


