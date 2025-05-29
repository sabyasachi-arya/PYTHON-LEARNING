magic_number = 7


while True:  # that means the code will run infinitely on a loop, if while True is used so the code must contain
    # a loop breaking keyword to exit the loop.
    user_input = input("Would you like to play the game(Y/n) : ")

    if user_input == "n":
        break  # to break the code that means the code will terminate the Run
    # break keyword is used to break the loop , or exit the loop
    # if they type n the code will the while loop, if they type anything else the code will run over and over again
    # because this time: user_input = input("Would you like to play the game(Y/n) : ") is inside the loop
    # so the loop will ask the user automatically every time to type yes or no to run the programme.
    user_num = int(input("Type a number from 1-9 to see if you are lucky or not: "))
    if user_num == magic_number:
        print(f"Congratulations! You found the lucky number: {magic_number}.")
    elif abs(user_num - magic_number) == 1:
        print("Oh! You were off by just one.")
        print(f"Sorry, but {user_num} is not the lucky number.")
    else:
        print(f"Sorry, but {user_num} is not the lucky number.")
