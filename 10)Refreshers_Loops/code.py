magic_number = 7
user_input = input("Would you like to play the game(Y/n) : ")
# In the above line the Y means anything the user type apart from "n" will be considered as yes
# if the user types n the programme will close.
# because while is a loop that's why until user types "n" they programme will run on a loop(from line 9-16)
# again and again infinitely, to overcome this issue the code need to ask the user if they want to run the code
# again or not. if they type n the code will stop running.
while user_input != "n":
    user_num = int(input("Type a number from 1-9 to see if you are lucky or not: "))
    if user_num == magic_number:
        print(f"Congratulations! You found the lucky number: {magic_number}.")
    elif abs(user_num - magic_number) == 1:
        print("Oh! You were off by just one.")
        print(f"Sorry, but {user_num} is not the lucky number.")
    else:
        print(f"Sorry, but {user_num} is not the lucky number.")

    user_input = input("Would you like to play the game(Y/n) : ")