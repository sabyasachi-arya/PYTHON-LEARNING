magic_number = 7
user_input = input("Type 'y' if to play the game: ")
# .lower() is a easy choice to solve this problem of user typing uppercase or lowercase but
# another way to solve the problem is to tell the code to accept both as argument or input by in keyword:
if user_input in ("y", "Y"):  # this means it will check if the user input is either of this two
    user_num = int(input("Type a number from 1-9 to see if you are lucky or not: "))
    if user_num == magic_number:
        print(f"Congratulations! You found the lucky number: {magic_number}.")
    else:
        print(f"Sorry, but {user_num} is not the lucky number.")
