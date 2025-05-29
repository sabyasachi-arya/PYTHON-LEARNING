magic_number = 7
user_input = input("Type 'y' if to play the game: ")

if user_input in ("y", "Y"):
    user_num = int(input("Type a number from 1-9 to see if you are lucky or not: "))
    if user_num == magic_number:
        print(f"Congratulations! You found the lucky number: {magic_number}.")
    elif (user_num - magic_number) in (1, -1): # this means it will check
        # if the (user_num - magic_number) is either of this two value 1 or -1
        print("Oh! You were off by just one.")
        print(f"Sorry, but {user_num} is not the lucky number.")
    else:
        print(f"Sorry, but {user_num} is not the lucky number.")

print("--------------------------------------------------------------------------------------------------------------")

magic_number = 7
user_input = input("Type 'y' if to play the game: ")

if user_input in ("y", "Y"):
    user_num = int(input("Type a number from 1-9 to see if you are lucky or not: "))
    if user_num == magic_number:
        print(f"Congratulations! You found the lucky number: {magic_number}.")
    elif abs(user_num - magic_number) == 1:  # this means it will convert the value of (user_num - magic_number) into
        # positive. abs() turns any value into positive means absolute value, so if the ^^^^^^^ this thing gives -1 ,
        # then abs() will convert it into 1.
        print("Oh! You were off by just one.")
        print(f"Sorry, but {user_num} is not the lucky number.")
    else:
        print(f"Sorry, but {user_num} is not the lucky number.")
